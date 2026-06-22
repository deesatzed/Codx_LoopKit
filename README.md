# Codx_LoopKit

Codx_LoopKit is a Codex-native process pack for turning vague repo work into
governed goal loops with intake Q&A, verification, failure escalation, Council
review, and completion gates.

It is not a separate agent runtime. It is a set of reusable Codex skills and
project instructions that build on Codex's existing foundations: skills,
`AGENTS.md`, `/goal`, subagents, hooks, automations, MCP, and `codex exec`.

## What It Gives You

- `repo-goal-compiler`: turns vague repo work into a clear goal contract.
- `repo-loop-runner`: runs a build-test-fix loop under that contract.
- `repo-completion-gate`: blocks premature "done" claims until proof exists.
- `council-review`: runs a compact multi-angle review only when useful.

The first version is intentionally small. There is no custom scheduler, daemon,
agent framework, or model router.

## Install

```sh
git clone https://github.com/deesatzed/Codx_LoopKit.git
mkdir -p ~/.agents/skills
cp -R Codx_LoopKit/skills/* ~/.agents/skills/
```

Restart Codex after installing if the skills do not appear immediately.

## Use

Explicit mode:

```text
$repo-goal-compiler Make this repo demo-ready.
$repo-loop-runner Continue until the goal proof passes.
$repo-completion-gate Check whether this is actually done.
```

Automatic mode:

Copy the relevant rules from this repo's `AGENTS.md` into a target repo's
`AGENTS.md`, then ask Codex for normal repo work. Codex should invoke the skills
when the task shape matches their trigger descriptions.

## Design Principle

Codx_LoopKit should feel like Codex became more disciplined, not like you
installed a second platform.

```text
messy request
-> intake Q&A
-> goal contract
-> repo loop
-> verifier
-> council only on risk/failure/scope drift
-> completion gate
```

## Validate

```sh
python3 scripts/validate_skills.py
PYTHONPYCACHEPREFIX=/private/tmp/codx_loopkit_pycache python3 -m py_compile scripts/validate_skills.py
```
