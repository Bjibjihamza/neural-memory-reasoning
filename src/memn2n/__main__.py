"""Small commands to verify the new workstation without downloading datasets."""
import argparse
import json
import platform
import sys
from pathlib import Path

from .data import flatten_story


def main() -> None:
    parser = argparse.ArgumentParser(description="Neural memory research workstation")
    parser.add_argument("command", choices=("doctor", "inspect-fixture"))
    args = parser.parse_args()
    if args.command == "doctor":
        print("Workstation package: OK")
        print(f"Python: {sys.version.split()[0]} | Platform: {platform.system()}")
        try:
            import torch
        except ImportError:
            print("PyTorch: not installed (expected for lightweight bootstrap)")
        else:
            print(f"PyTorch: {torch.__version__} | CUDA ready: {torch.cuda.is_available()}")
        print("Next: docs/STATUS.md and docs/SETUP_WINDOWS.md")
    else:
        fixture = Path(__file__).resolve().parents[2] / "tests/fixtures/babi_story.json"
        data = json.loads(fixture.read_text(encoding="utf-8"))
        qa = flatten_story(data, source_id="fixture-001")
        print(f"Parsed {len(qa)} questions from a tiny offline fixture")
        for ex in qa:
            print(f"Q: {ex['question']} -> {ex['answer']} ({len(ex['context'])} context facts)")


if __name__ == "__main__":
    main()
