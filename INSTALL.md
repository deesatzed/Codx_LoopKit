# Install Codx_LoopKit

## Install

```sh
git clone https://github.com/deesatzed/Codx_LoopKit.git
cd Codx_LoopKit
scripts/install.sh
```

Restart Codex if the skills do not appear.

## Update

```sh
cd Codx_LoopKit
git pull
scripts/install.sh
```

The installer is idempotent. It replaces only Codx_LoopKit skill folders in the
target directory.

## Verify Install

From the cloned repo:

```sh
python3 scripts/validate_skills.py --skills-dir ~/.agents/skills
```

In Codex, type `/skills` and look for:

- `repo-goal-compiler`
- `repo-loop-runner`
- `repo-completion-gate`
- `council-review`

## Smoke Test Without Touching User Skills

```sh
scripts/install.sh --target /private/tmp/codx-loopkit-install-smoke
python3 scripts/validate_skills.py --skills-dir /private/tmp/codx-loopkit-install-smoke
```

## Uninstall

```sh
rm -rf ~/.agents/skills/repo-goal-compiler \
       ~/.agents/skills/repo-loop-runner \
       ~/.agents/skills/repo-completion-gate \
       ~/.agents/skills/council-review
```

## Optional Repo Rules

For automatic behavior in a target repo, copy `examples/consumer-AGENTS.md` into
that repo's `AGENTS.md`.
