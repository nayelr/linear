#!/usr/bin/env python3
"""Merge data/chapter-*.json into data/all.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
out = {"chapters": []}
for n in range(1, 5):
    p = ROOT / "data" / f"chapter-{n}.json"
    with open(p, encoding="utf-8") as f:
        out["chapters"].append(json.load(f))

dest = ROOT / "data" / "all.json"
with open(dest, "w", encoding="utf-8") as f:
    json.dump(out, f, indent=2)
    f.write("\n")
print("Wrote", dest)
