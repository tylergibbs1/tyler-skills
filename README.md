# Skills

Agent skills I find useful for my workflow.

They are small, model-agnostic, and composable. Adapt them, delete the ones you disagree with, make them yours.

## The skills

### Engineering

| Skill | What it does |
|-------|--------------|
| [grounding-with-context7](./skills/engineering/grounding-with-context7/SKILL.md) | "use context7 to help u", reaching for a library from stale training data instead of grounding in current docs. |
| [learning-from-exemplar-repos](./skills/engineering/learning-from-exemplar-repos/SKILL.md) | inventing framework/style patterns from scratch instead of studying a repo that already does it well ("just apply determinism"). |

### Writing

| Skill | What it does |
|-------|--------------|
| [human-sounding-copy](./skills/writing/human-sounding-copy/SKILL.md) | em dashes, jargon, all-caps eyebrows, cheap icons, the tells that read as AI-generated. |

### Design

| Skill | What it does |
|-------|--------------|
| [linear-design-principles](./skills/design/linear-design-principles/SKILL.md) | Apply Linear's UI/UX and product philosophy as product judgment, not decoration. Peer-aware about where those opinions have limits. |
| [mirroring-layout-in-loading-states](./skills/design/mirroring-layout-in-loading-states/SKILL.md) | loading states that don't match the real layout (perceived shift) and progress UI that lies ("still showing this even though its done"). |
| [creating-aws-architecture-diagrams](./skills/design/creating-aws-architecture-diagrams/SKILL.md) | Create precise AWS architecture diagrams with verified relationships, named resources, focused perspectives, and polished 16:9 output. |

### Product

Skills for deciding what to build and in what order.

| Skill | What it does |
|-------|--------------|
| [proving-value-before-building-out](./skills/product/proving-value-before-building-out/SKILL.md) | Validate the core value headless, with an eval harness on real inputs, before any UI or infra. |
| [researching-latent-demand](./skills/product/researching-latent-demand/SKILL.md) | Decide what to build from real pain/market research and the painkiller-not-vitamin test, then file as issues. |

### Workflows

User-invoked multi-agent orchestration (reach them by name).

| Skill | What it does |
|-------|--------------|
| [orchestrating-subagents](./skills/workflows/orchestrating-subagents/SKILL.md) | Decompose a task and fan out subagents to implement each piece in parallel, each briefed and told to ground in Context7. |
| [shipping-pr-reviews](./skills/workflows/shipping-pr-reviews/SKILL.md) | Push changes to a PR, then run a workflow that reviews the diff, verifies each finding, and fixes the confirmed ones. |

## Install

With [skills.sh](https://skills.sh):

```bash
npx skills@latest add tylergibbs1/tyler-skills
```

Or clone and symlink into `~/.claude/skills`:

```bash
git clone https://github.com/tylergibbs1/tyler-skills.git
cd tyler-skills
./scripts/link-skills.sh
```

Or add as a Claude Code plugin (the repo ships a `.claude-plugin/plugin.json`).

## Why these skills

These are practical patterns I find useful in my day-to-day workflow. Each skill captures a focused behavior that can be reused across projects and adapted as needed.

## License

MIT
