# Example: Explicit Skill Invocation

Use this when you want to control the process manually.

```text
$repo-goal-compiler Make this repo demo-ready.
```

Then, after approving or refining the goal:

```text
$repo-loop-runner Continue until the goal proof passes.
```

Before accepting the work:

```text
$repo-completion-gate Check whether the goal is actually complete.
```

If the loop stalls:

```text
$council-review The same verifier failed twice. Give one final ruling and next step.
```
