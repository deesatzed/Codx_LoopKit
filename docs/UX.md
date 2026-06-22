# Codx_LoopKit UX

## North Star

Codx_LoopKit should make Codex feel more disciplined, not more verbose.

The user gives intent. Codex asks only the minimum needed to define success,
then works under a governed loop and verifies before claiming completion.

## Default Interaction

```text
User: Make this repo demo-ready.

Codex: I will compile this into a repo goal loop first.
Outcome: demo-ready repo.
Proof: build/test/smoke/docs appropriate to the repo.
Autonomy: proceed until proof passes or a stop condition triggers.
Council: only on repeated failure, risk, or scope drift.
```

## Intake Q&A

Ask at most three questions:

1. What observable outcome means done?
2. What proof should Codex use?
3. Should this update durable repo files or stay chat-only?

If the user already answered these, do not ask again.

## Council UX

Council is an interrupt, not the default voice.

Use it when:

- the user asks,
- verification fails twice,
- scope drifts,
- completion is unclear,
- an action is risky.

Keep output compact: five perspectives, then one ruling.
