# GOAL.md - Codx_LoopKit Seamless Use

## Current Truth

Codx_LoopKit V0 exists as a standalone Codex-native skill pack. It has:

- install docs,
- four initial skills,
- examples,
- a skill validator,
- project truth files,
- a pushed GitHub repo at `https://github.com/deesatzed/Codx_LoopKit.git`.

The next goal is not to add a new runtime. The next goal is to make the pack
easy for another Codex user to install, verify, and use without knowing this
conversation.

## /goal

OUTCOME:

Make Codx_LoopKit seamless for a new Codex user to install and use as skills.
The finished state should let a user clone the repo, run one install command,
verify the installed skill pack, and understand both explicit and automatic
usage modes in under five minutes.

PROOF OF DONE:

1. Installation is one-command and idempotent:
   - add `scripts/install.sh`,
   - support default install into `~/.agents/skills`,
   - support `--target <dir>` for safe smoke tests,
   - rerunning the installer should update existing skill folders cleanly.
2. Installed-skill validation exists:
   - extend or add validation so it can check both repo-local `skills/` and an
     installed target directory,
   - validation must confirm each expected skill folder has a valid `SKILL.md`
     with matching `name` and non-empty `description`.
3. User-facing docs are frictionless:
   - `README.md` starts with a 60-second quickstart,
   - `INSTALL.md` includes install, update, verify, and uninstall guidance,
   - docs explain explicit mode and automatic `AGENTS.md` mode,
   - docs make clear that V0 ships no daemon, scheduler, MCP server, plugin, or
     custom runtime.
4. Consumer repo setup is copy-pasteable:
   - add an `examples/consumer-AGENTS.md` or equivalent snippet,
   - snippet tells Codex when to use `repo-goal-compiler`,
     `repo-loop-runner`, `council-review`, and `repo-completion-gate`.
5. First-run UX is demonstrated:
   - add an example showing a vague repo task becoming a goal loop,
   - add an example showing explicit skill invocation,
   - add an example showing automatic trigger behavior through `AGENTS.md`.
6. Package hygiene passes:
   - `python3 scripts/validate_skills.py`,
   - `PYTHONPYCACHEPREFIX=/private/tmp/codx_loopkit_pycache python3 -m py_compile scripts/validate_skills.py`,
   - install smoke using a temp target, for example
     `scripts/install.sh --target /private/tmp/codx-loopkit-install-smoke`,
   - validation against that temp target,
   - `git diff --check`,
   - `git status --short` reviewed before commit.
7. Repo truth is updated:
   - `PROGRESS.md` records commands and results,
   - `DECISIONS.md` records any meaningful UX/install decisions,
   - final work is committed and pushed to `origin/main` if auth allows.

SCOPE:

Allowed to modify:

- `README.md`
- `INSTALL.md`
- `GOAL.md`
- `AGENTS.md`
- `PROGRESS.md`
- `DECISIONS.md`
- `docs/`
- `examples/`
- `scripts/`
- `skills/` only for small clarity fixes needed for install/use UX

Do not add in this goal:

- custom daemon,
- scheduler,
- MCP server,
- plugin packaging,
- hook package,
- browser/UI app,
- model routing,
- project-specific private logic,
- dependency-heavy installer.

CONSTRAINTS:

- Stay Codex-native: skills remain the primary execution unit.
- Keep install transparent: shell/Python scripts must be readable and small.
- Do not require modifying a user's global Codex config for V0.
- Do not assume users have this chat history.
- Do not rely on sibling repos, machine-local paths, provider API keys, or any
  project-specific private state.
- Preserve both usage modes:
  - explicit skill invocation,
  - automatic behavior through consumer `AGENTS.md` rules.
- Keep Council as escalation, not default voice.
- Do not weaken the existing skill validation.

ITERATION:

1. Inspect current docs, examples, skills, and validator.
2. Add the smallest install path that can be tested in a temp target first.
3. Update docs around the actual installer behavior.
4. Add consumer setup snippets and first-run examples.
5. Run repo-local validation.
6. Run temp-target install smoke and validate the installed skills.
7. Record command results in `PROGRESS.md`.
8. Commit and push only after verification passes.

STOP:

Pause and summarize if:

- installing to a temp target cannot be made safe,
- the installer would need broad system permissions,
- a required Codex behavior cannot be verified locally,
- GitHub push/auth fails,
- the design would require building a custom runtime instead of using Codex
  skills.

COMPLETE:

Mark complete only when a fresh user can follow the documented quickstart from
the GitHub repo, install the skills into a target directory, validate them, and
understand how to use explicit and automatic modes without reading this chat.
