# Example: Build-Test-Fix Loop

User:

```text
$repo-loop-runner Continue until the current GOAL.md proof passes.
```

Expected loop:

```text
inspect goal
-> identify verifier
-> make smallest relevant change
-> run verifier
-> classify failure
-> fix or escalate
```

Council should trigger only after repeated failure, risk, or scope drift.
