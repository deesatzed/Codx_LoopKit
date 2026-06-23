# Example: Automatic AGENTS.md Trigger

1. Install Codx_LoopKit skills.
2. Copy `examples/consumer-AGENTS.md` into the target repo's `AGENTS.md`.
3. Ask Codex normally:

```text
Make this repo demo-ready.
```

Expected Codex behavior:

```text
I will use repo-goal-compiler because this is a broad repo request.
I need one clarification: what proof should define demo-ready?
```

After the goal is clear, Codex should proceed through `repo-loop-runner`, invoke
`council-review` only on trigger conditions, and use `repo-completion-gate`
before claiming completion.
