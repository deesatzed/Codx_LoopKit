---
name: repo-goal-compiler
description: Use when a user gives a vague or multi-step repo task and Codex should turn it into a governed goal contract before implementation.
---

# Repo Goal Compiler

Turn messy repo intent into a clear Codex work contract.

## Intake

Ask at most three questions, only when the answer changes execution:

1. What observable outcome means done?
2. What proof should Codex use?
3. Should this update durable repo files or stay chat-only?

If safe defaults exist, state assumptions and proceed.

## Output

Produce a compact goal contract:

```markdown
## Outcome
## Proof Of Done
## Scope
## Forbidden Actions
## Verification
## Stop Conditions
## Persistence
```

## Persistence Rules

- For one-off work, keep the contract in chat.
- For multi-step repo work, create or update `GOAL.md` when the user requested durable state or the repo already uses `GOAL.md`.
- If replacing an existing `GOAL.md`, preserve important current truth unless the user explicitly asks to reset it.

## Boundaries

Do not implement before the goal contract is clear enough to verify. Do not add ceremony for tiny tasks where the outcome and proof are obvious.
