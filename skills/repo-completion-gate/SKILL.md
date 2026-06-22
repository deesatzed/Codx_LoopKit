---
name: repo-completion-gate
description: Use before Codex claims repo work is complete; checks the goal, proof, verification output, and durable notes to prevent premature done claims.
---

# Repo Completion Gate

Before saying work is complete, produce a verdict:

```text
PASS | PARTIAL | BLOCKED
```

## Checks

1. Re-read the goal or latest user request.
2. List each proof item.
3. Match each proof item to evidence.
4. Confirm verification commands were run or explain why not.
5. Check whether `PROGRESS.md` or `DECISIONS.md` needs updating.
6. Check git status when the repo is a git repository.

## Verdict Rules

- `PASS`: every required proof item is satisfied.
- `PARTIAL`: useful work is done but proof is incomplete.
- `BLOCKED`: progress cannot continue without user input or external state.

Do not call partial work complete. Do not hide failed or skipped verification.

## Output

Use this shape:

```markdown
Completion Gate: PASS/PARTIAL/BLOCKED
Evidence:
- ...
Missing:
- ...
Final ruling:
```
