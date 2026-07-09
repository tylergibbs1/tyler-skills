#!/usr/bin/env bash
set -euo pipefail

# Symlink every skill in this repo into the local Claude Code skills directory
# (~/.claude/skills). A `git pull` then keeps installed skills up to date.

REPO="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$HOME/.claude/skills"

mkdir -p "$DEST"

find "$REPO/skills" -name SKILL.md -print0 | while IFS= read -r -d '' skill_md; do
  src="$(dirname "$skill_md")"
  name="$(basename "$src")"
  target="$DEST/$name"
  if [ -e "$target" ] && [ ! -L "$target" ]; then
    rm -rf "$target"
  fi
  ln -sfn "$src" "$target"
  echo "linked $name -> $src"
done
