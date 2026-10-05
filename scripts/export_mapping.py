#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHEETS_DIR = ROOT / "sheets"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


for sheet_name in ["input_actions", "locomotion", "weapons", "ui"]:
    path = SHEETS_DIR / f"{sheet_name}.json"
    data = load_json(path)
    print(f"{sheet_name}: {len(data)} rows")
    for item in data[:3]:
        print(f"  - {item['id']}: {item['target']}")
