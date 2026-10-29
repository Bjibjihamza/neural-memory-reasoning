import json
from pathlib import Path

import pytest
from memn2n.data import flatten_story


def fixture():
    return json.loads((Path(__file__).parent / "fixtures/babi_story.json").read_text())


def test_extracts_each_question_without_future_context():
    qa = flatten_story(fixture(), source_id="test-story")
    assert len(qa) == 2
    assert qa[0]["answer"] == "kitchen"
    assert qa[0]["context_ids"] == ["1", "2"]
    assert qa[1]["answer"] == "hallway"
    assert qa[1]["context_ids"] == ["1", "2", "4"]
    assert qa[0]["supporting_ids"] == ["1"]


def test_bad_parallel_arrays_are_rejected():
    item = fixture()
    item["story"]["text"].pop()
    with pytest.raises(ValueError, match="same length"):
        flatten_story(item)


def test_future_supporting_id_is_rejected():
    item = fixture()
    item["story"]["supporting_ids"][2] = ["4"]
    with pytest.raises(ValueError, match="future/missing"):
        flatten_story(item)
