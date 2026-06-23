# Codx_LoopKit

Codx_LoopKit is a Codex-native process pack for turning vague repo work into
governed goal loops with intake Q&A, verification, failure escalation, Council
review, and completion gates.

## 60-Second Quickstart

```sh
git clone https://github.com/deesatzed/Codx_LoopKit.git
cd Codx_LoopKit
scripts/install.sh
python3 scripts/validate_skills.py --skills-dir ~/.agents/skills
```

Restart Codex if the skills do not appear immediately, then use explicit mode:

```text
$repo-goal-compiler Make this repo demo-ready.
```

For automatic mode, copy `examples/consumer-AGENTS.md` into a target repo's
`AGENTS.md`, then ask Codex for normal repo work.

## What It Is

It is not a separate agent runtime. It is a set of reusable Codex skills and
project instructions that build on Codex's existing foundations: skills,
`AGENTS.md`, `/goal`, subagents, hooks, automations, MCP, and `codex exec`.

## What It Gives You

- `repo-goal-compiler`: turns vague repo work into a clear goal contract.
- `repo-loop-runner`: runs a build-test-fix loop under that contract.
- `repo-completion-gate`: blocks premature "done" claims until proof exists.
- `council-review`: runs a compact multi-angle review only when useful.

The first version is intentionally small. There is no daemon, scheduler, MCP
server, plugin package, custom runtime, agent framework, or model router.

## Install

```sh
scripts/install.sh
```

Safe smoke install to a temp target:

```sh
scripts/install.sh --target /private/tmp/codx-loopkit-install-smoke
python3 scripts/validate_skills.py --skills-dir /private/tmp/codx-loopkit-install-smoke
```

## Use

Explicit mode:

```text
$repo-goal-compiler Make this repo demo-ready.
$repo-loop-runner Continue until the goal proof passes.
$repo-completion-gate Check whether this is actually done.
```

Automatic mode:

Copy `examples/consumer-AGENTS.md` into a target repo's `AGENTS.md`, then ask
Codex for normal repo work. Codex should invoke the skills when the task shape
matches their trigger descriptions.

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
python3 scripts/validate_skills.py --skills-dir ~/.agents/skills
PYTHONPYCACHEPREFIX=/private/tmp/codx_loopkit_pycache python3 -m py_compile scripts/validate_skills.py
```
