# Codx_LoopKit V0 Implementation Plan

> **For Codex:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build the initial standalone Codx_LoopKit repo as a Codex-native skill pack for governed repo goal loops.

**Architecture:** The repo is a distribution and documentation source. Runtime behavior is provided by Codex skills copied into `~/.agents/skills`, plus optional consumer `AGENTS.md` trigger rules.

**Tech Stack:** Markdown, Codex Agent Skills, standard-library Python validation.

---

### Task 1: Repo Documentation

**Files:**
- Create: `README.md`
- Create: `INSTALL.md`
- Create: `GOAL.md`
- Create: `AGENTS.md`
- Create: `docs/UX.md`
- Create: `docs/PROCESS_MODEL.md`

**Steps:**
1. Explain the product boundary: Codex-native process pack, not a runtime.
2. Document manual skill installation into `~/.agents/skills`.
3. Define UX expectations and stop rules.
4. Verify docs are concise and consistent.

### Task 2: Skill Source Folders

**Files:**
- Create: `skills/repo-goal-compiler/SKILL.md`
- Create: `skills/repo-loop-runner/SKILL.md`
- Create: `skills/repo-completion-gate/SKILL.md`
- Create: `skills/council-review/SKILL.md`

**Steps:**
1. Give every skill valid frontmatter.
2. Keep each skill focused on one workflow.
3. Include explicit trigger boundaries.
4. Avoid extra docs inside skill folders.

### Task 3: Examples

**Files:**
- Create: `examples/vague-to-goal.md`
- Create: `examples/build-test-fix-loop.md`
- Create: `examples/repeated-failure-council.md`

**Steps:**
1. Show explicit skill invocation.
2. Show automatic `AGENTS.md` behavior.
3. Show Council as failure escalation, not default mode.

### Task 4: Validation

**Files:**
- Create: `scripts/validate_skills.py`

**Steps:**
1. Check each skill folder has `SKILL.md`.
2. Check frontmatter contains matching `name`.
3. Check `description` exists.
4. Run:

```sh
python3 scripts/validate_skills.py
PYTHONPYCACHEPREFIX=/private/tmp/codx_loopkit_pycache python3 -m py_compile scripts/validate_skills.py
```

### Task 5: Final Review

**Steps:**
1. Run validation.
2. Run `git status --short`.
3. Confirm no generated cache files are intended for commit.
4. Summarize install UX and changed files.
