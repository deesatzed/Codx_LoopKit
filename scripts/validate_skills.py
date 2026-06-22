from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        return {}
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    return fields


def main() -> int:
    errors: list[str] = []
    if not SKILLS.is_dir():
        errors.append("skills/ directory is missing")
    else:
        skill_dirs = sorted(path for path in SKILLS.iterdir() if path.is_dir())
        if not skill_dirs:
            errors.append("skills/ contains no skill directories")
        for skill_dir in skill_dirs:
            skill_file = skill_dir / "SKILL.md"
            if not skill_file.is_file():
                errors.append(f"{skill_dir.name}: missing SKILL.md")
                continue
            fields = parse_frontmatter(skill_file.read_text())
            name = fields.get("name")
            description = fields.get("description")
            if name != skill_dir.name:
                errors.append(
                    f"{skill_dir.name}: frontmatter name {name!r} does not match folder"
                )
            if not description:
                errors.append(f"{skill_dir.name}: missing description")
            if (skill_dir / "README.md").exists():
                errors.append(f"{skill_dir.name}: README.md should not live inside skill")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Validated Codx_LoopKit skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
