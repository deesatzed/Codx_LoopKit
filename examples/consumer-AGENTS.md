# Codx_LoopKit Consumer Rules

Use these rules in a target repo's `AGENTS.md` after installing Codx_LoopKit
skills.

## Codx_LoopKit Behavior

- Use `$repo-goal-compiler` when the user gives a vague, broad, or multi-step
  repo request and the outcome/proof is not already clear.
- Use `$repo-loop-runner` when Codex should continue implementation through
  verification rather than stopping after a plan.
- Use `$council-review` only when explicitly requested, after repeated
  verification failure, before a risky decision, when scope drifts, or when
  completion is ambiguous.
- Use `$repo-completion-gate` before claiming repo work is complete.

## Defaults

- Ask at most three intake questions before making safe assumptions.
- Prefer existing repo proof commands and truth files.
- Do not weaken tests or proof gates to pass.
- Stop for missing credentials, destructive actions, production deploys,
  sensitive data risk, or unresolved repeated failure.
- Keep Council as escalation, not the default response style.
