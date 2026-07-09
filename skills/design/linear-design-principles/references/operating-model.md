# How Linear actually operates

The blog posts in `ui-ux-craft.md` are the output. This is the input: the org structure, decision-making, architecture, method, and hiring that make the design principles hold. The structure makes quality everyone's job; the rituals reinforce the structure, not the other way around.

## Contents
- Org structure: design never gets handed off
- Decisions: taste, not experiments
- Opinionated software and plain language
- Speed as architecture
- The Linear Method
- Hiring and culture
- Planning mechanics

---

## Org structure: design never gets handed off

- **One product team, one roadmap.** Planning is centralized; everyone feels responsible for the whole product.
- **No durable cross-functional squads.** Teams assemble around a project and disperse when it ships. Typical unit: **1 designer + 2 engineers**, with roughly six project teams running in parallel (at ~50 people).
- **Project lead can be anyone** (engineer or designer), never a PM.
- **One PM total.** Nan Yu, Head of Product, hired at ~25 people. The plan is explicitly *not* to hire PMs per team; PM duties are distributed across engineering and design.
- **No product-area teams** (no "cycles team"). Owning a slice traps people in it; they lose context on the whole and over-polish minor details.
- Product team split by **region** (US / Europe) to handle time zones, not by product area.
- Karri Saarinen's reasoning (Figma "10 rules"): the PM-decides → designer-visualizes → engineer-builds pipeline creates silos. At Linear there is no "handoff to dev," and quality improves when everyone understands how designs are implemented and shares responsibility. "You're never off the hook."

> **2026 update — the no-handoffs idea, extended to agents.** Linear's "Issue tracking is dead" (linear.app/next, Mar 2026) generalizes this: handoffs existed because engineering time was scarce, but they're lossy overhead. As agents take procedural work, the relay to eliminate now includes human→agent, so the system's job is to make **shared context** (decisions, "why," code) legible to humans and agents alike. The small-connected-team model is the precursor, not a contradiction — see SKILL.md principle 11.

## Decisions: taste, not experiments

- **No OKRs.** Goals are loose strategic themes like "be the default tool for startups."
- **No metrics goals** for products or projects. One North Star company-level metric only.
- **No A/B tests** as decision-makers. They validate ideas driven by taste and opinion. Data is sometimes pulled for insight, never to decide. "Data can be a crutch" — to provide the best experience you must surprise users, and data can't tell you how.
- Replacement mechanism: **feature flags from day one** push features to internal dogfooding within days or weeks ("no excuse to wait to ship"), then **Linear Origins**, a customer beta program, for early external feedback. Beta is optional, not a required gate.
- **No formal design reviews.** Designers post early work in project Slack channels for async feedback. Founders + Head of Product act as **project sponsors**, each ultimately responsible for an outcome. Senior taste applied continuously, not at checkpoints.
- Success metric for craft is qualitative: Linear coming up organically in conversations about quality.
- **Decide and move on.** There isn't always a best answer; sometimes the most important thing is to make a decision.

> **Boundary — when metrics legitimately decide.** Linear's taste-over-data stance is safest *once you already have conviction and a deterministic, hand-reviewable surface.* It is most dangerous in four cases where peers rely on data: **pre-PMF** (Superhuman's 40% "very disappointed" survey was the central instrument for finding fit), **at the strategic "is anyone actually adopting this?" altitude** (The Browser Company wound down Arc partly on adoption telemetry, having trusted vision over signal for a long time), **when many stakeholders must align on priority** (Intercom's RICE), and **for non-deterministic features you can't eyeball** (agent evals — see SKILL.md principle 8). "Taste tells you if it's good; metrics tell you if it's being adopted," and those can diverge for years. Full treatment in `boundaries-and-peers.md`, #2.

## Opinionated software and plain language

- Jori Lallo (co-founder): design so there's **one really good way of doing things**. Flexible software lets everyone invent their own workflows, which creates chaos as teams scale.
- More opinionated at the **atomic level** (issue properties like labels, due dates); more cues from customer feedback at broader levels (projects), since every company is structured differently.
- **No invented jargon.** Universal units (projects, teams, issues) so nobody needs a handbook. "Your tools should not make you the designer and maintainer of them."
- The atomic unit stays minimal: an issue needs only a title and status; all other properties are optional. Quick to create, less unnecessary work.
- Nan Yu rejects traditional user stories ("As a user, I want X") as indirect formalism that hides the actual need. Write issues, not user stories.
- They **refuse whole categories of requests** (required fields, multiple assignees) because managers ask for them but they degrade the IC workflow. ICs aren't forced to use the tool, so if a request fits that description, the answer is just "no" — no debate.
- Nan Yu: speed is a result of competence, not corner-cutting. Speed and quality correlate positively in skilled teams. Better to be decisively wrong and pivot than cautiously mediocre.

## Speed as architecture (the part visual design can't fake)

Linear's "feel" is mostly a backend bet made before the product existed.

- CTO Tuomas Artman: the **literal first lines of code were the sync engine** — uncommon for a startup.
- **Local-first architecture:** a copy of the database lives in the browser (IndexedDB), hydrated into an in-memory MobX object pool on boot. UI applies changes optimistically and instantly; a custom sync engine batches deltas to other clients over WebSocket. Local changes never show a spinner — there's nothing to wait for.
- Stack is deliberately simple: React, TypeScript, MobX, PostgreSQL, client-side rendered. The two heaviest tables (Issue, Comment) lazy-hydrate, so a 10,000-issue workspace boots about as fast as a 100-issue one.
- Speed is a **system property**, not one layer: local DB + optimistic writes + granular observables + lean first-load. Remove any one and the app feels slow.
- Speed is also an **input-model problem**: a fast sync engine still loses if the fastest path to an action needs a mouse and three menus. Keyboard is a primary input; the command palette (⌘K) searches the local object pool, not a server. Animations stick to GPU-composited properties (transform, opacity); layout-triggering properties are never animated.
- Practical result: runs offline as a PWA; third-party measurement reports most pages load under ~50ms.

> **The design takeaway:** "Calm, dense, fast" is not achievable through visual design alone. Linear bought the headroom for its minimal UI by making latency near zero, so the interface doesn't need loading states, skeletons, or progress affordances that add visual noise.

## The Linear Method (process codified)
🔗 https://linear.app/method

- **Cycles** (typically 2 weeks): a healthy routine, not sprints. Don't overload them; unfinished work rolls to the next cycle automatically.
- **Delete the backlog.** You don't need to save every feature request indefinitely. Important ones resurface; low-priority ones never get fixed anyway.
- Include bugs and fixes inside cycles. Invest in tooling as a force multiplier.
- **Every project has a named owner** responsible for the brief and delivery.
- Momentum over burnout: aim for a steady speed sustainable next month and next year, not exhaustion bursts.
- Build a tiny version quickly; the market tells you fast if it works. Endless data collection and testing usually signals you don't know what to do.

### Alternative cadence: Shape Up (Basecamp) — what the Linear Method lacks
🔗 https://basecamp.com/shapeup

The Linear Method is one cadence, not the only one. Basecamp's Shape Up is the strongest peer alternative, and it has three ideas Linear's cycles don't:

- **Appetite, not estimates.** Fix the time budget first (a "small batch" ~1–2 weeks or a "big batch" ~6 weeks), then *shape scope down to fit it*. This is the inverse of estimating ("how long will this take?") — you ask "how much is this worth?" and design to that ceiling.
- **No backlog at all.** Linear "deletes the backlog" as hygiene; 37signals questions whether it should exist. Important ideas resurface; the rest were never going to ship. Each cycle, you *bet* on a few shaped pitches from scratch.
- **Cooldown + circuit breaker.** Schedule slack (a ~2-week cooldown between cycles for bugs, exploration, and recovery). And if a project misses its appetite, it **stops by default** rather than getting an extension — the team has to re-pitch and re-earn a slot. This kills the "just one more week" death spiral.

**When to reach for which:** Linear's short continuous cycles + curated near-term backlog + always-assigned owners suit high-frequency iterative work where momentum and visible ownership matter. Shape Up suits teams that want long, uninterrupted, protected focus and reject the obligation of an ever-growing list. (See `boundaries-and-peers.md`, #3.)

## Hiring and culture

- **Paid work trials:** candidates join for 1 to 5 days and work on a real project with the team. Filters for what the whole system depends on: people who self-direct without PM oversight and notice quality problems on their own.
- Fully remote, always has been.
- Bootstrapped early, profitable for years, ~$35K total spent on paid marketing (as of the 2023 Lenny profile).
- Connected teams over specialized silos; everyone is responsible for quality.

## Planning mechanics (from the Lenny Q&A)

- Two-way annual planning: founders + small leadership group set 12-month direction; in parallel, whole-team FigJam sessions and surveys feed ideas up.
- Detail planned ~2 quarters out, next half sketched, extensive backlog to pull from.
- Projects sequenced by "optimal path" and paired with individual strengths (strongest front-end people get front-end-heavy features).
- Project plans start as draft docs; the project team writes the spec — the spec is the baseline, not the finish line.
- Bug tracking through Triage with a weekly rotating "goalie" engineer who supports the support team and routes/fixes incoming issues. Zero-bugs policy: e.g., 48 hours for high-priority bugs, 7 days for the rest; no backlog option.
- Weekly project updates posted to a public Slack channel.

---

## Core through-line

Linear treats UI design as **product judgment, not decoration**, and backs it with structure:

- Reduce visual noise without reducing capability.
- Hierarchy sharp enough that density stays calm.
- Taste makes decisions; dogfooding and betas validate them.
- No handoffs: small connected teams own problems end to end.
- Opinionated defaults over infinite flexibility.
- Speed is architecture and input design, not polish.
- Quality is a trained habit and a hiring filter, not a final pass.

The risk they openly accept: this excludes anyone whose needs fall outside the chosen lane.
