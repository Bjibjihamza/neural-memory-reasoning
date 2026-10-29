"""Utilities for flattening bAbI story records into question-level examples.

No network access or ML framework is required; this is the offline preparation
contract for the upcoming dataset lab.
"""
from __future__ import annotations

from typing import Any


def flatten_story(record: dict[str, Any], *, source_id: str = "unknown") -> list[dict[str, Any]]:
    """Convert an official-style bAbI story dict into independent QA examples.

    The schema uses parallel ``id``, ``type``, ``text``, ``answer`` and
    ``supporting_ids`` arrays. Each question sees only preceding context,
    not future context sentences. Supporting IDs are diagnostic metadata.
    """
    story = record.get("story", record)
    fields = ("id", "type", "text", "answer", "supporting_ids")
    missing = [name for name in fields if name not in story]
    if missing:
        raise ValueError(f"Missing bAbI fields: {', '.join(missing)}")
    lengths = {len(story[name]) for name in fields}
    if len(lengths) != 1:
        raise ValueError("Parallel story arrays must have the same length")

    context: list[dict[str, str]] = []
    questions: list[dict[str, Any]] = []
    for line_id, kind, line, answer, supports in zip(
        story["id"], story["type"], story["text"],
        story["answer"], story["supporting_ids"], strict=True,
    ):
        is_question = (kind == 1 or str(kind).lower() in {"question", "1"})
        if not is_question:
            context.append({"id": str(line_id), "text": str(line)})
            continue
        if not answer:
            raise ValueError(f"Question {line_id} has no gold answer")
        ids = [str(x) for x in supports]
        context_ids = {s["id"] for s in context}
        if not set(ids).issubset(context_ids):
            raise ValueError(f"Question {line_id} references future/missing supporting facts")
        questions.append({
            "source_story": source_id,
            "question_id": str(line_id),
            "context": [s["text"] for s in context],
            "context_ids": [s["id"] for s in context],
            "question": str(line),
            "answer": str(answer),
            "supporting_ids": ids,
        })
    return questions
