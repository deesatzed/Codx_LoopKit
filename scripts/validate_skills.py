from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXPECTED_SKILLS = (
    "council-review",
    "repo-completion-gate",
    "repo-goal-compiler",
    "repo-loop-runner",
)


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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate Codx_LoopKit skill folders.")
    parser.add_argument(
        "--skills-dir",
        default=str(SKILLS),
        help="Directory containing installed or repo-local skill folders.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    skills_dir = Path(args.skills_dir).expanduser()
    errors: list[str] = []
    if not skills_dir.is_dir():
        errors.append(f"skills directory is missing: {skills_dir}")
    else:
        for expected in EXPECTED_SKILLS:
            if not (skills_dir / expected).is_dir():
                errors.append(f"{expected}: expected skill folder is missing")
        for skill_name in EXPECTED_SKILLS:
            skill_dir = skills_dir / skill_name
            if not skill_dir.is_dir():
                continue
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
    print(f"Validated Codx_LoopKit skills in {skills_dir}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
