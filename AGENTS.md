# AGENTS.md

## Codx_LoopKit Rules

This repo is the source package for reusable Codex skills. Keep it independent
from any consuming project.

## Skill Quality

- Each skill must have a focused `SKILL.md` with `name` and `description`.
- Skill folder names must match skill names.
- Do not put README or install docs inside individual skill folders.
- Keep skills concise; put user-facing docs in the repo root or `docs/`.

## Process Behavior For Consumers

When these rules are copied into a target repo:

- Use `$repo-goal-compiler` for vague or multi-step repo requests.
- Use `$repo-loop-runner` when implementation should continue through
  verification.
- Use `$council-review` after repeated failure, risky decisions, scope drift, or
  explicit user request.
- Use `$repo-completion-gate` before claiming work is complete.

## Verification

Before claiming this package is ready:

```sh
python3 scripts/validate_skills.py
PYTHONPYCACHEPREFIX=/private/tmp/codx_loopkit_pycache python3 -m py_compile scripts/validate_skills.py
sh -n scripts/install.sh
scripts/install.sh --target /private/tmp/codx-loopkit-install-smoke
python3 scripts/validate_skills.py --skills-dir /private/tmp/codx-loopkit-install-smoke
git diff --check
git status --short
```
