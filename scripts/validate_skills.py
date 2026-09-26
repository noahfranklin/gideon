#!/usr/bin/env python3
"""Validate every skills/<name>/SKILL.md: YAML frontmatter, name↔dir match,
non-empty description. Zero external deps. Exit non-zero on any failure."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"


def parse_frontmatter(text: str):
    if not text.startswith("---"):
        return None, "missing opening '---' frontmatter fence"
    end = text.find("\n---", 3)
    if end == -1:
        return None, "missing closing '---' frontmatter fence"
    block = text[3:end].strip("\n")
    data = {}
    key = None
    for line in block.splitlines():
        if not line.strip():
            continue
        if line[0] not in " \t" and ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            data[key] = val.strip().strip('"').strip("'")
        elif key:  # simple continuation
            data[key] += " " + line.strip().strip('"').strip("'")
    return data, None


def main() -> int:
    if not SKILLS.is_dir():
        print("ERROR: skills/ directory not found")
        return 1
    errors, count = [], 0
    for skill_dir in sorted(SKILLS.iterdir()):
        if not skill_dir.is_dir():
            continue
        md = skill_dir / "SKILL.md"
        if not md.exists():
            errors.append(f"{skill_dir.name}: no SKILL.md")
            continue
        count += 1
        data, err = parse_frontmatter(md.read_text(encoding="utf-8"))
        if err:
            errors.append(f"{skill_dir.name}: {err}")
            continue
        name = data.get("name", "")
        desc = data.get("description", "")
        if name != skill_dir.name:
            errors.append(f"{skill_dir.name}: frontmatter name '{name}' != directory")
        if len(desc) < 20:
            errors.append(f"{skill_dir.name}: description too short / missing")
    if errors:
        print("SKILL VALIDATION FAILED:")
        for e in errors:
            print("  -", e)
        return 1
    print(f"OK: {count} skill(s) validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
