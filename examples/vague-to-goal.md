# Example: Vague Task To Goal

User:

```text
$repo-goal-compiler Make this repo demo-ready.
```

Expected Codex behavior:

```text
I need one thing before I compile this:
What proof would make you comfortable calling the repo demo-ready?
```

If the user does not specify, Codex should use safe defaults:

- build/test/smoke pass,
- README or usage path is clear,
- no known P0 blockers,
- no destructive actions without approval.
