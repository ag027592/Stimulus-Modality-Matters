"""Fast, dataset-free integrity checks for Stimulus Modality Matters."""
from __future__ import annotations

import ast
import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> None:
    required = [
        "README.md",
        "LICENSE",
        "CITATION.cff",
        "emo/config_CREMAD.yaml",
        "data/CREAMA-D/Primary/config.json",
        "run_log_test.sh",
    ]
    for relative in required:
        if not (ROOT / relative).exists():
            fail(f"missing {relative}")

    python_files = [
        path for path in ROOT.rglob("*.py") if ".git" not in path.parts
    ]
    for path in python_files:
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except (SyntaxError, UnicodeDecodeError) as exc:
            fail(f"invalid Python in {path.relative_to(ROOT)}: {exc}")

    config_path = ROOT / "data/CREAMA-D/Primary/config.json"
    try:
        config = json.loads(config_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        fail(f"invalid dataset config: {exc}")
    if not isinstance(config, dict):
        fail("expected dataset config to be a JSON object")

    label_files = list((ROOT / "data").rglob("labels_consensus_*.csv"))
    if len(label_files) != 20:
        fail(f"expected 20 modality partitions, found {len(label_files)}")
    for path in label_files:
        with path.open(encoding="utf-8-sig", newline="") as handle:
            if not next(csv.reader(handle), None):
                fail(f"empty CSV: {path.relative_to(ROOT)}")

    print(
        "OK: "
        f"{len(python_files)} Python files and "
        f"{len(label_files)} modality partitions"
    )


if __name__ == "__main__":
    main()
