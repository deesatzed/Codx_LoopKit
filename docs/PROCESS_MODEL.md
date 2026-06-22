# Process Model

Codx_LoopKit uses Codex-native surfaces instead of a custom runtime.

## Surfaces

- `AGENTS.md`: durable trigger rules.
- Skills: reusable workflows.
- `/goal`: persistent target in an active Codex thread.
- `codex exec`: noninteractive or scripted use.
- Automations: future recurring routines.
- Hooks: future lifecycle enforcement.
- Subagents: future high-value parallel review.

## Flow

```text
request
-> repo-goal-compiler
-> goal contract
-> repo-loop-runner
-> verifier
-> council-review if triggered
-> repo-completion-gate
-> final ruling
```

## Stop Conditions

Stop or ask the user when:

- credentials or accounts are missing,
- destructive action is needed,
- production deployment is requested,
- secrets or sensitive data risk appears,
- verification fails repeatedly without a new strategy,
- the requested outcome changes materially.
