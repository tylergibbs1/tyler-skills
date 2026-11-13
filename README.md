# tyler-skills

Small agent skills that fix mistakes coding agents keep making: stale library APIs, AI-sounding
copy, loading states that jump, papers you cite without checking. Each one came from a
correction I had to make more than once in Claude Code.

```bash
npx skills@latest add tylergibbs1/tyler-skills
```

[Browse the skills](#the-skills) · [Other ways to install](#install) · [Add or improve a skill](#contributing)

## How it works

A skill is a folder with a `SKILL.md`: a short description that tells the agent when to use
it, then instructions the agent loads only when the task matches. Some skills ship scripts or
reference files the agent reads as needed. They are plain Markdown, so they work with any agent
that supports [Agent Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview).

You don't call most of them. Ask for cold-email copy and `cold-emailing` loads; ask about
prior work on a method and `scientific-literature-discovery` loads. The two workflow skills
are the exception: you invoke those by name.

## The skills

| Skill | Use it to |
|-------|-----------|
| **Engineering** | |
| [grounding-with-context7](./skills/engineering/grounding-with-context7/SKILL.md) | Check library, framework and SDK calls against current docs instead of training data. |
| [learning-from-exemplar-repos](./skills/engineering/learning-from-exemplar-repos/SKILL.md) | Copy patterns from a strong reference repo instead of inventing them. |
| **Writing** | |
| [human-sounding-copy](./skills/writing/human-sounding-copy/SKILL.md) | Strip the tells that make text read as model-written, in seven passes. |
| [lulu-comms](./skills/writing/lulu-comms/SKILL.md) | Write launch, PR and brand copy where every line serves a business goal. |
| [cold-emailing](./skills/writing/cold-emailing/SKILL.md) | Write cold emails and DMs under 100 words that strangers answer. |
| **Design** | |
| [linear-design-principles](./skills/design/linear-design-principles/SKILL.md) | Make product and UI calls the way Linear does, and know where that stops applying. |
| [mirroring-layout-in-loading-states](./skills/design/mirroring-layout-in-loading-states/SKILL.md) | Build loading states that match the real layout and never show "done" early. |
| [creating-aws-architecture-diagrams](./skills/design/creating-aws-architecture-diagrams/SKILL.md) | Draw AWS diagrams with verified connections and named resources. |
| **Product** | |
| [researching-latent-demand](./skills/product/researching-latent-demand/SKILL.md) | Pick what to build from real user pain, then file it as issues. |
| **Research** | |
| [scientific-literature-discovery](./skills/research/scientific-literature-discovery/SKILL.md) | Map how papers connect, audit prior work and design tests that could prove you wrong. |
| **Workflows** (invoke by name) | |
| [orchestrating-subagents](./skills/workflows/orchestrating-subagents/SKILL.md) | Split a task and have subagents build the pieces in parallel. |
| [shipping-pr-reviews](./skills/workflows/shipping-pr-reviews/SKILL.md) | Push to a PR, review the diff, verify each finding and fix the real ones. |

Each skill's `SKILL.md` has the details. Test scenarios for skills that have them are in
[`evals/`](./evals).

## Install

With [skills.sh](https://skills.sh), as above, or clone and link into `~/.claude/skills`:

```bash
git clone https://github.com/tylergibbs1/tyler-skills.git
cd tyler-skills && ./scripts/link-skills.sh
```

The repo is also a Claude Code plugin (`.claude-plugin/plugin.json`). `./scripts/list-skills.sh`
lists what's installed.

## Contributing

Issues and PRs are welcome. A good skill fixes one mistake an agent makes repeatedly, says in
its description exactly when to load, and keeps `SKILL.md` short, with detail in reference
files. If you change how a skill behaves, add or update a scenario in `evals/` that shows the
difference with and without it. Adapt anything here, or delete the skills you disagree with.

## License

[MIT](LICENSE)

