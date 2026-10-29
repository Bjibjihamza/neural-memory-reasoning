from pathlib import Path
import yaml


def test_experiment_grid_has_both_memory_hops():
    root = Path(__file__).resolve().parents[1]
    grid = yaml.safe_load((root / "configs/experiment_grid.yaml").read_text())
    assert {m.get("hops") for m in grid["models"] if "hops" in m} == {1, 3}
    assert grid["evaluation"]["distractor_counts"] == [0, 5, 10, 20]


def test_submission_has_required_fields_and_valid_description():
    root = Path(__file__).resolve().parents[1]
    p = yaml.safe_load((root / "proposal/project-proposal.yml").read_text())
    assert set(p["proposal"]["dataset"]) == {"name", "source", "access_and_terms", "scope"}
    assert 40 <= len(p["description"].split()) <= 70
    assert (root / "proposal" / p["thumbnail"]).exists()
