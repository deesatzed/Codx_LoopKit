# GOAL.md - Codx_LoopKit V0

## Outcome

Create a reusable Codex-native process pack that helps users turn vague repo
work into governed goal loops without building a separate agent runtime.

## Proof Of Done

V0 is complete when:

- the repo explains what Codx_LoopKit is and is not,
- install instructions copy skills into `~/.agents/skills`,
- four skills exist with valid `SKILL.md` frontmatter:
  - `repo-goal-compiler`
  - `repo-loop-runner`
  - `repo-completion-gate`
  - `council-review`
- examples show the expected UX,
- a local validator checks skill structure,
- validation commands pass.

## Scope

Allowed:

- repo docs,
- skill source folders,
- examples,
- lightweight validation scripts.

Not in V0:

- custom runtime,
- daemon,
- scheduler,
- MCP server,
- hooks package,
- plugin packaging,
- model routing research.

## UX Contract

Codx_LoopKit must support both:

- explicit use through skill invocation,
- automatic use through `AGENTS.md` trigger rules.

Before a governed loop begins, Codex should clarify outcome and proof if they
are not obvious. It should ask at most three intake questions before making safe
assumptions and proceeding.
