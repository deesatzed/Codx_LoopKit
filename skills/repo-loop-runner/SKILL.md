---
name: repo-loop-runner
description: Use when Codex should execute repo work through a governed build-test-fix loop until proof passes, a stop condition triggers, or user input is required.
---

# Repo Loop Runner

Run repo work as a small-loop sequence:

```text
inspect -> choose next step -> edit -> verify -> classify result -> continue or stop
```

## Before Work

1. Read active repo truth files if present: `GOAL.md`, `AGENTS.md`, `PROGRESS.md`, `DECISIONS.md`, `TASK_QUEUE.md`.
2. Identify the proof command or smoke check.
3. State the next loop step in one sentence.

## Loop Rules

- Keep edits small and tied to the goal.
- Run the narrowest meaningful verifier after each change.
- Record failures by cause, not just command output.
- Do not weaken tests or proof gates to pass.
- Update `PROGRESS.md` for durable multi-step work when the repo uses it.

## Escalation

Trigger `$council-review` when:

- the same verifier fails twice,
- two different approaches fail,
- scope drifts,
- the next action is risky,
- completion status is ambiguous.

## Stop Conditions

Stop or ask the user for:

- missing credentials,
- destructive actions,
- production deploy,
- sensitive data risk,
- repeated failure after strategy change,
- product decisions that materially change scope.
