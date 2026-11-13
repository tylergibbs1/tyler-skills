# Skills

Agent skills I find useful for my workflow: practical patterns, each capturing a focused behavior you can reuse across projects.

They are small, model-agnostic, and composable. Adapt them, delete the ones you disagree with, make them yours.

## Quick start

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

## The skills

### Engineering

| Skill | What it does |
|-------|--------------|
| [grounding-with-context7](./skills/engineering/grounding-with-context7/SKILL.md) | Ground work with a library, framework, or SDK in current docs via Context7 instead of stale training data. |
| [learning-from-exemplar-repos](./skills/engineering/learning-from-exemplar-repos/SKILL.md) | Study a high-quality reference repo instead of inventing framework or style patterns from scratch. |

### Writing

| Skill | What it does |
|-------|--------------|
| [human-sounding-copy](./skills/writing/human-sounding-copy/SKILL.md) | Writing that reads like a model wrote it: verbose, generic, em dashes, title-case headings, no stakes and no voice. Seven passes, plus exemplar writers to study and the research behind each tell. |
| [lulu-comms](./skills/writing/lulu-comms/SKILL.md) | Lulu Cheng Meservey's comms operating system for copy, mission, branding, and PR: every tactic traces to a business objective, hook before story before channel, evidence over adjectives, plus launch/crisis/apology playbooks. |
| [cold-emailing](./skills/writing/cold-emailing/SKILL.md) | Cold emails and DMs a stranger will read and answer. Write to the person who owns the problem, open on them, give one proof, ask one small question, and stay under 100 words in the sender's own voice. Also covers sending safely, the one follow-up, where the practices stop working, and where they came from. |

### Design

| Skill | What it does |
|-------|--------------|
| [linear-design-principles](./skills/design/linear-design-principles/SKILL.md) | Apply Linear's UI/UX and product philosophy as product judgment, not decoration. Peer-aware about where those opinions have limits. |
| [mirroring-layout-in-loading-states](./skills/design/mirroring-layout-in-loading-states/SKILL.md) | Make loading states match the real layout (no perceived shift) and keep progress UI from showing "done" or stale data while work is still running. |
| [creating-aws-architecture-diagrams](./skills/design/creating-aws-architecture-diagrams/SKILL.md) | Create precise AWS architecture diagrams with verified relationships, named resources, focused perspectives, and polished 16:9 output. |

### Product

Skills for deciding what to build and in what order.

| Skill | What it does |
|-------|--------------|
| [researching-latent-demand](./skills/product/researching-latent-demand/SKILL.md) | Decide what to build from real pain/market research and the painkiller-not-vitamin test, then file as issues. |

### Research

| Skill | What it does |
|-------|--------------|
| [scientific-literature-discovery](./skills/research/scientific-literature-discovery/SKILL.md) | Find evidence-linked connections between scientific papers, audit prior work, challenge competing explanations, and design falsifiable tests. |
| [wcml](./skills/research/wcml/SKILL.md) | Run ML experiments so gains hold up on held-out data, in two modes. Search mode: a budgeted agent loop of many cheap one-seed tries, big levers first, then one paired lockbox check. Bet mode: error review by eye, ceilings before methods, one variable with a control and a pre-written kill line, and a ledger. Ships a paired group bootstrap and a contact-sheet script; test scenarios in `evals/wcml/`. |

### Workflows

User-invoked multi-agent orchestration (reach them by name).

| Skill | What it does |
|-------|--------------|
| [orchestrating-subagents](./skills/workflows/orchestrating-subagents/SKILL.md) | Decompose a task and fan out subagents to implement each piece in parallel, each briefed and told to ground in Context7. |
| [shipping-pr-reviews](./skills/workflows/shipping-pr-reviews/SKILL.md) | Push changes to a PR, then run a workflow that reviews the diff, verifies each finding, and fixes the confirmed ones. |

## License

[MIT](LICENSE)
