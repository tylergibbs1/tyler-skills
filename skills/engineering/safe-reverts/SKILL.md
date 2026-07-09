---
name: safe-reverts
description: Treat reverts and destructive git operations as high blast radius. Use before git reset --hard, git checkout -- ., git clean, or rm of untracked files, and whenever the user might be editing files in parallel with you.
---

# Safe Reverts

Reverts and destructive git operations wreck uncommitted or concurrent work fast ("nooo why did u revert now the change the other did are gone?", "no i dont have backup"). Treat them as high blast radius.

## Rules

- **Assume parallel edits.** The user may be editing files while you work. Do not touch files unrelated to your task, and never revert or overwrite changes you did not make. When in doubt, ask.
- **Confirm before destroying uncommitted work.** Before any `git reset --hard`, `git checkout -- .`, `git clean`, or `rm` of untracked files, run `git status` first and confirm with the user. Never discard uncommitted work without an explicit go-ahead.
- **Scope reverts precisely.** Revert the specific file, hunk, or commit that was asked for, not the whole tree.
- **Branch for risk.** For large or risky changes, work on a separate branch so main stays clean.
- **Offer a backup.** If a revert would discard work and there is no commit to fall back on, say so and offer to stash or back it up first.
