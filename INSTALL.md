# Install Codx_LoopKit

## Manual Install

```sh
git clone https://github.com/deesatzed/Codx_LoopKit.git
mkdir -p ~/.agents/skills
cp -R Codx_LoopKit/skills/* ~/.agents/skills/
```

Restart Codex if the skills do not appear.

## Verify Install

In Codex, type `/skills` and look for:

- `repo-goal-compiler`
- `repo-loop-runner`
- `repo-completion-gate`
- `council-review`

## Optional Repo Rules

For automatic behavior in a target repo, copy the "Process Behavior For
Consumers" section from this repo's `AGENTS.md` into that repo's `AGENTS.md`.
