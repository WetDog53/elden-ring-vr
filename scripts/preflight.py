#!/usr/bin/env python3
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHEETS_DIR = ROOT / "sheets"

REQUIRED_FILES = [
    "input_actions.json",
    "locomotion.json",
    "weapons.json",
    "ui.json",
]


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def assert_required_files():
    missing = []
    for file_name in REQUIRED_FILES:
        if not (SHEETS_DIR / file_name).exists():
            missing.append(file_name)
    if missing:
        raise FileNotFoundError(f"Missing required sheet files: {missing}")


def validate_rows(rows, sheet_name):
    missing = []
    for index, row in enumerate(rows):
        for key in ("id", "name", "target", "required", "status"):
            if key not in row:
                missing.append(f"{sheet_name}[{index}] missing key '{key}'")
    if missing:
        raise ValueError("\n".join(missing))


def main():
    assert_required_files()
    known_targets = set()

    for file_name in REQUIRED_FILES:
        sheet = load_json(SHEETS_DIR / file_name)
        validate_rows(sheet, file_name)
        for row in sheet:
            known_targets.add(row["target"])

    # Basic cross-sheet reference sanity check.
    # This is intentionally lightweight and meant to fail early before a runtime build.
    for file_name in REQUIRED_FILES:
        sheet = load_json(SHEETS_DIR / file_name)
        for row in sheet:
            if "requires" in row:
                for dependency in row["requires"]:
                    if dependency not in {r["id"] for r in load_json(SHEETS_DIR / "input_actions.json")}:
                        raise ValueError(f"Unresolved dependency '{dependency}' in {file_name}: {row['id']}")

    print("Preflight passed: all required sheets are present and their rows are structurally valid.")


if __name__ == "__main__":
    main()
