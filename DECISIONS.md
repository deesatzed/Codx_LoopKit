# DECISIONS.md

## 2026-06-22 - Build Codx_LoopKit as Codex-native skills, not a runtime

Decision: V0 is a standalone source repo containing Codex skill folders,
installation docs, examples, and lightweight validation.

Reason: Codex already provides the runtime surfaces: skills, `AGENTS.md`,
`/goal`, subagents, hooks, automations, MCP, and `codex exec`. Rebuilding those
would add complexity before proving UX value.

Consequence: V0 ships no daemon, scheduler, MCP server, custom command runner,
or plugin packaging. Users install the skills by copying `skills/*` into
`~/.agents/skills`.

## 2026-06-22 - Keep Council as escalation, not default voice

Decision: Council review is a skill and failure/risk interrupt, not an always-on
response format.

Reason: Always-on multi-voice output is token-heavy and can become theater. The
highest-value moments are repeated verification failure, high-risk decisions,
scope drift, and completion ambiguity.

Consequence: `council-review` gives five compact perspectives and one final
ruling, while normal repo work stays under the goal loop.

## 2026-06-23 - Make install idempotent without global config changes

Decision: V0 uses `scripts/install.sh` to copy the four skill folders into
`~/.agents/skills` by default, with `--target <dir>` for smoke tests and custom
installs.

Reason: the product should be usable as Codex skills without requiring users to
edit global Codex config, run a daemon, install a plugin, or adopt a custom
runtime.

Consequence: the installer replaces only Codx_LoopKit skill folders in the
target directory and validates the installed target. It also cleans stale
`.codx-loopkit.tmp` staging folders before and after install attempts.
