# Workflows

Multi-agent orchestration flows. Both are user-invoked (`disable-model-invocation: true`), so you reach them by name.

- **[orchestrating-subagents](./orchestrating-subagents/SKILL.md)** — Decompose a task, fan out subagents to implement each piece in parallel, and brief each one with the context it needs plus a mandate to pull fresh docs via Context7. Covers Claude Code subagents, dynamic workflows, and Codex subagents.
- **[shipping-pr-reviews](./shipping-pr-reviews/SKILL.md)** — Push the current changes to a PR, then run a dynamic workflow that reviews the diff, adversarially verifies each finding, and fixes the confirmed ones, pushing fixes back to the PR. Pairs with orchestrating-subagents.
