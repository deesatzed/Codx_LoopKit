#!/usr/bin/env sh
set -eu

TARGET="${HOME}/.agents/skills"
ROOT="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
SOURCE="${ROOT}/skills"

usage() {
  cat <<'USAGE'
Usage: scripts/install.sh [--target DIR]

Installs Codx_LoopKit skills into DIR.
Default target: ~/.agents/skills

Options:
  --target DIR   Install into DIR instead of ~/.agents/skills
  -h, --help     Show this help
USAGE
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --target)
      if [ "$#" -lt 2 ]; then
        echo "ERROR: --target requires a directory" >&2
        exit 2
      fi
      TARGET="$2"
      shift 2
      ;;
    --target=*)
      TARGET="${1#--target=}"
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "ERROR: unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if [ ! -d "$SOURCE" ]; then
  echo "ERROR: source skills directory not found: $SOURCE" >&2
  exit 1
fi

if [ -z "$TARGET" ] || [ "$TARGET" = "/" ]; then
  echo "ERROR: refusing unsafe install target: $TARGET" >&2
  exit 1
fi

mkdir -p "$TARGET"

find "$TARGET" -maxdepth 1 -type d -name '.*.codx-loopkit.tmp' -exec rm -rf {} +

for skill_dir in "$SOURCE"/*; do
  [ -d "$skill_dir" ] || continue
  skill_name="$(basename "$skill_dir")"
  dest="${TARGET}/${skill_name}"
  staging="${TARGET}/.${skill_name}.codx-loopkit.tmp"
  rm -rf "$staging"
  mkdir -p "$staging"
  cp -R "$skill_dir"/. "$staging"/
  rm -rf "$dest"
  mv "$staging" "$dest"
  echo "Installed ${skill_name} -> ${dest}"
done

find "$TARGET" -maxdepth 1 -type d -name '.*.codx-loopkit.tmp' -exec rm -rf {} +
python3 "${ROOT}/scripts/validate_skills.py" --skills-dir "$TARGET"
echo "Codx_LoopKit install complete: $TARGET"
