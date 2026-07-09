---
name: linear-design-principles
description: Applies Linear's UI/UX and product philosophy — design as product judgment, not decoration — when designing, building, or reviewing interfaces and making product decisions. Use when framing a product problem, planning a redesign, deciding scope, reducing visual noise, designing AI/agent interfaces, debating customization vs. opinionated defaults, or setting up product process (handoffs, OKRs, A/B testing, design reviews). Triggers on "Linear style," "calm interface," "opinionated software," "is this the right problem," "should we add a setting," "feature request vs need," "redesign strategy," "should we set OKRs," "do we need A/B testing," "design-to-engineering handoff," "should this be reversible / undo," "is chat the right AI interface," "is this opinion universal," "novelty vs familiarity." Linear-spine but peer-aware — where Linear's opinions have limits (platforms and flexibility, APIs as contracts, metrics vs taste, keyboard vs discoverability) it names the boundary and which peer answer applies. Not for replicating the Linear visual aesthetic (dark mode, gradients, minimalist landing pages) — this is about product method, not the look.
---

# Linear Design Principles

Apply how Linear thinks about UI, UX, and product. The throughline: **design is product judgment, not decoration**, and it only works when backed by structure — opinionated defaults, near-zero latency, trained quality, and small teams that own problems end to end.

> [!info] Terminology trap
> "Linear design" in most search results means a generic SaaS *aesthetic* (dark mode, gradients, minimal landing pages) named after the company. That is the look, not the method. This skill is about how Linear actually works. Ignore the aesthetic literature.

## When to apply this

Reach for these principles when the task is one of:

- **Designing or reviewing an interface** → use the hierarchy + clarity rules below, then `references/ui-ux-craft.md`.
- **Framing a product problem** → "problem before solution"; interpret requests, don't transcribe them.
- **Planning a redesign or paying down design debt** → `references/ui-ux-craft.md` (redesign strategy).
- **Designing AI/agent features** → "build the workbench, not the chatbox."
- **Deciding process, org, or how decisions get made** → `references/operating-model.md`.
- **Building, not just deciding** (accessibility, the checkable craft details) → `references/accessibility-and-craft-specs.md`.
- **Tempted to apply a principle as universal law** (or the product isn't Linear-shaped — a platform, an API, a consumer app) → `references/boundaries-and-peers.md` for where Linear's opinions have limits and which peer answer applies.
- **Citing or sourcing a claim** → `references/sources.md`.

> [!note] Scope
> This is about **product judgment — what to build and whether the problem is real** — not pixel-level execution. Pair it with a visual-craft/implementation skill: use this to decide what should exist, then a craft skill to execute. The interaction guidance here is **desktop- and keyboard-first** (command palette, dense lists, keyboard as primary input); defer touch/responsive/small-screen work to skills built for that. Linear hasn't published a mobile design philosophy, so don't invent one.

---

## The core principles

### 1. Design for someone specific. Be opinionated.

You cannot build something excellent for everyone. Pick a specific user and a specific use case and optimize hard for it; accept that it will be a poor fit outside that lane. Restraint is the strategy, not a limitation.

- A product needs a clear value proposition to win trust. Generic = invisible.
- Be most opinionated at the **atomic level** (what properties an issue has), more flexible at **broad containers** (how projects are structured), because every company is shaped differently.
- **Mind the novelty tax.** Every unfamiliar concept charges a learning cost that must be repaid in benefit. Be distinctive only where the payoff clearly exceeds the tax; for mainstream reach, lean on familiar conventions ("a piano, not a saxophone"). Power-user love is not proof of mainstream fit — The Browser Company's Arc won devoted fans on novel concepts but capped broad adoption, and the team wound it down. (See `references/boundaries-and-peers.md`, #1 and #5.)

### 2. Ship one really good way, not infinite flexibility.

Ship strong defaults that guide users toward a good workflow. Flexible software lets everyone invent their own process, which becomes chaos as teams scale.

- Sometimes the opinionated answer is **"no."** Refuse whole categories of requests that protect managers at the expense of the daily IC workflow (e.g., required fields, multiple assignees) — saying no is a feature of an opinionated tool, not a failure to satisfy it. (Interpreting the underlying need is principle 10; this is the case where, even interpreted, the right call is still to decline.)
- Default to "simple first, then powerful": simple to start, more capable as you scale.

### 3. Use plain language. No invented jargon.

Vocabulary is a design surface. Use universal units (issues, projects, teams) so nobody needs a handbook. Don't invent terms — they mean different things to different people. Write issues, not "As a user, I want…" user stories that hide the actual need.

- Extend this to **all words on screen**, not just object names: button labels, error messages, empty-state copy, and notification voice are part of the calm. Aim for terse, human, jargon-free microcopy. (Linear has no dedicated essay on voice; treat the specific tone calls as inference from the product, not a sourced rule.)
- **The interface isn't only pixels.** For developer and agent audiences, the **API, SDK, CLI, error payload, and docs *are* the primary UI** and deserve identical craft — naming, progressive disclosure, plain language, and errors that teach the next step. Stripe's principle is "the API is the UI": an error should say `No such customer: cus_…`, not return a 500. Apply the same hierarchy and plain-language discipline to a schema or a CLI flag that you'd apply to a screen. (Stripe.)

### 4. Understand the problem before drawing the screen.

The most common reason design projects drag or fail is an unclear problem. Generating the form is the easy part; knowing what should exist at all is the hard part.

- Write the problem in your own words first. Ask: is this real? What happens if we don't do it? Who defined it?
- If feedback feels contradictory, people are probably reacting to **different problem definitions**.
- Separate **problem design → conceptual solution → execution**. Decide concepts (is a "project" an issue, a label, or its own entity?) before UI details.
- **Output isn't design.** Polished AI-generated UI can have the form without the fit. Use AI for prototyping and exploration; keep human judgment responsible for problem framing.

### 5. Calm but dense: make hierarchy do the ranking.

Dense interfaces can still feel calm if hierarchy is sharp. Don't let every element compete for attention.

- Use **visual weight as a ranking system**: work content dominates; navigation and chrome recede.
- Borders, icons, backgrounds, and separators must **earn their existence**. If they don't clarify a relationship, they're clutter.
- "Structure should be felt, not seen." If most people don't consciously notice a refinement, that's a good sign.
- Test against **real app states** (full lists, empty states, long text), not isolated Dribbble-style mockups. Stress-test across browser/desktop, light/dark/custom themes, and edge cases.
- Treat **theming as a system**: derive themes from a few perceptual parameters (base color, accent, contrast in a perceptually-uniform space like LCH) plus a baked-in accessibility contrast variable — not by hand-tuning dozens of independent color values.
- For **data views and dashboards**, give every view a clear purpose and owner, and pair every metric with comparison, history, or a threshold — a raw number with no context is usually noise. (More in `references/ui-ux-craft.md`.)
- **Accessibility is structure, not polish.** Keyboard operability, visible focus, reduced-motion variants, perceptual contrast (APCA), and adequate hit targets are *inputs* to a calm interface, not a final-pass checklist. Linear documents only a contrast variable; the full checkable set is in `references/accessibility-and-craft-specs.md`, along with the quantified craft thresholds (16px inputs, press/dialog scale, "never `transition: all`," tabular numerals, optical alignment) that an agent can enforce mechanically.

### 6. Speed is architecture and input design, not polish.

"Calm, dense, fast" is not achievable with visual design alone. Linear bought the headroom for its minimal UI by making latency near zero, so the interface needs no spinners, skeletons, or progress affordances that add noise.

- Treat **latency as a UX bug**. Aim for instant (optimistic local writes, local-first data) before adding features. Eliminate spinners by having nothing to wait for.
- Speed is also an **input-model problem**: a fast backend still loses if the fastest path to an action needs a mouse and three menus. Make keyboard a primary input; a command palette should search the local object pool, not a server.
- **Removing spinners is only half of feedback.** The hard, mandatory half is signaling when an optimistic write *fails* and rolls back. Optimistic local writes make the happy path instant — but they also mean the UI can show "saved" for something that didn't. Design the failure and reconciliation state explicitly (a clear, recoverable rollback), don't only design the success path. (Apple HIG, "Feedback." Pairs with principle 12.)

### 7. Treat quality as a trained habit and a hiring filter, not a final pass.

Craft is deliberate attention paid because it matters to the maker, not because someone is checking. It compounds through many small decisions.

- Quality is **everyone's job**, not just the designer's. Review UI as a group — different people notice different defects (misaligned pixels, animation timing, papercuts).
- Track papercuts as real work; keep fixes small enough to be sustainable. Consider a recurring quality ritual and a strict bug SLA (no permanent bug backlog).
- Trust intuition and customers over pure data. Keep MVPs internal until they're ready.

### 8. For AI features, build the workbench — not just a chatbox.

Generic chat is a weak, imprecise form for most workflows. Design structured surfaces ("workbenches") where AI operates inside clear context.

- Design the **review, approval, context, and control** surfaces, not just the prompt box.
- **Embed agents where the work already lives** — inside the issue, the triage queue, the review — not in a bolted-on chat panel. Let work auto-start from existing signals (e.g., triage) instead of requiring someone to open a separate tool.
- Make agent sessions **shared and observable**: anyone on the team can follow, redirect, or take over a run, rather than it being a private one-off. Surface the agent's reasoning, tool calls, and elicitations.
- **Keep a human accountable.** The issue stays assigned to a person — "an agent cannot be held accountable." As agents handle correctness and bug-finding, the human's job shifts up to judgment: is the work *useful*, not just correct? Unbounded AI is powerful but directionless.
- **The agent is also a user you design for.** The workbench above is for the human supervising the agent; separately, design the interface the *agent itself* consumes. Tool names, schemas, and responses are a design surface: prefer a few high-leverage tools over thin wrappers around every endpoint, human-readable fields over opaque IDs (an agent reasons better with `file_type` than a UUID), namespacing, and response-verbosity controls. Invest as much in this agent-computer interface as in the human one. (Anthropic, "Building effective agents" / "Writing tools for agents.")
- **Evals and observability are the quality signal for non-deterministic features.** Linear's quality model (principle 7) assumes deterministic UI you can review by hand. Agents fail subtly, and a tiny prompt change cascades — so for stochastic features, systematic evals (real-task suites, regression, production-trace sampling) and tracing aren't bureaucracy, they're the *only* way to know if quality changed. This is the one place "taste over metrics" must bend. (Anthropic, LangChain.)
- **Guardrails and consent are part of the design.** Gate consequential or irreversible agent actions behind explicit confirmation; offer watch/takeover modes; treat prompt injection as a first-class risk and never let an agent touch credentials. Layered defense-in-depth, not a single check. (OpenAI's agent guidance; Operator's confirmation/takeover patterns.)

### 9. Use settings for preferences, not deferred decisions.

Settings aren't automatically a sign of poor design. Use them for genuine preferences and repeated-use friction — not as a dumping ground for unresolved product decisions. Settings can also teach power users what's possible.

- Decision test: **is there a right default the product should just get right?** If yes, pick it — don't ship a toggle to avoid choosing. If it's genuine taste/habit the product shouldn't hold an opinion on, a setting is appropriate.

### 10. Build what customers need, not just what they ask for.

Treat requests as **input, not instructions**. Users describe symptoms or name a familiar solution; infer the deeper need. Don't tally feature requests blindly — research is interpretation, not transcription. (Example: users asked for "custom fields" but were really trying to track customer needs → build the purpose-built thing.)

### 11. Design for shared context, not handoffs.

As agents do more of the procedural work (Linear, 2026: coding agents in 75%+ of its enterprise workspaces, agent-completed work up 5x in three months, ~25% of new issues agent-authored), the bottleneck moves from execution to **context**. The job of the system is to capture customer feedback, decisions, strategic direction, and code in one place that both humans and agents can work from — so nothing has to be re-explained at a handoff.

- Linear's original "no handoffs, small connected teams" model is the **precursor** to this, not a contradiction: both eliminate the lossy PM→designer→engineer relay. Now the relay to eliminate also includes the human→agent one.
- Make the work the source of truth. If a decision or its "why" only lives in a chat thread or someone's head, an agent (and the next human) can't use it.
- This is *why* plain language (3), opinionated structure (2), and the workbench (8) matter more, not less, in the agent era — shared context only works if the vocabulary and structure are legible to everyone, human or machine.
- **"Context" has a second, literal meaning here.** Linear's "context" is *organizational* (decisions, the "why," code in one place). When you actually build the agent, there's also the model's **context window** — a finite resource with diminishing returns and "context rot." Engineer it: retrieve just-in-time rather than front-loading everything, compact near the limit, and isolate sub-agents so they return distilled summaries instead of raw transcripts. Capturing context organizationally (this principle) and budgeting it at inference time are two different jobs. (Anthropic, "Effective context engineering for AI agents.")

### 12. Make actions reversible. Forgiveness is what lets people move fast.

Undo and clean recovery from mistakes are what let people act confidently without fear. This is a precondition for speed, not a nicety — and it's the half of feedback Linear's writing omits. (Apple HIG "Forgiveness"; Dieter Rams.)

- **Optimistic writes make reversibility mandatory, not optional** (ties to principle 6). The moment the UI shows "done" before the server confirms, you owe the user a visible, trustworthy rollback path when it didn't.
- Prefer **undo over confirmation dialogs** for routine actions; reserve confirmation for the consequential and irreversible (and for agent actions — see principle 8).
- Design the **error and recovery state**, not just the happy path. "How does this fail, and how does the user get back?" is a design question, not an edge case to handle later.

---

## How decisions and teams should work (brief)

These structural facts are *why* the principles above hold. Full detail in `references/operating-model.md`.

- **No handoffs.** Small connected teams (≈1 designer + 2 engineers) own a problem end to end; design and engineering iterate toward "right" together. Quality improves when everyone understands implementation.
- **Taste decides; dogfooding and betas validate.** No OKRs, no metric goals per project, no A/B tests as decision-makers. Feature-flag to internal dogfooding within days, then optional customer beta. Senior taste applied continuously, not at checkpoints.
- **No formal design reviews.** Post early work async (e.g., a project channel) for feedback.
- **Speed is a result of competence, not corner-cutting.** Better to be decisively wrong and pivot than cautiously mediocre. Decide and move on.

---

## Where these principles have limits

Linear's answers are confident on purpose, but they're **conditional, not universal**. Peer companies with comparable craft reach the opposite conclusion in some cases — and they're right for the products they build. Know the deciding variable before applying a principle as law. Full treatment, with sources and "when each side is right," in `references/boundaries-and-peers.md`.

- **Opinionated "one good way" (1, 2) breaks for platforms and creative substrates.** Notion, Raycast, Figma, and shadcn win on *flexibility* because their users' jobs are unknowably diverse or the artifact is personal. Deciding variable: how knowable/homogeneous the workflow is. Either way, owe the user the opposite counterweight (escape hatches for opinionated apps; templates for flexible ones).
- **Taste-over-metrics breaks pre-PMF and for stochastic features.** Superhuman's PMF survey, Intercom's RICE, Arc's adoption telemetry, and agent evals all decide by data where taste can't. "Taste tells you if it's good; metrics tell you if it's being adopted."
- **Keyboard-first (6) assumes daily expert users.** For occasional users, touch, or rarely-used surfaces, see-and-point discoverability wins (Apple HIG).
- **"Decisively wrong and pivot" breaks for contracts other software depends on.** A human re-learns a redesign overnight; an API/schema/file format is a production outage. The more your interface is a contract, the more it must only extend, never break (Stripe).
- **Tacit, unwritten taste (no formal reviews) doesn't scale to agents.** Machines can't read taste — if agents produce or check your craft, some of it must be codified (Vercel's guidelines-as-linter).
- **Calm restraint (5) isn't the whole emotional register.** High-frequency work surfaces want calm; milestones and consumer apps want deliberate delight and communicative motion (Superhuman, Apple "Depth," Airbnb).
- **The Linear Method is one cadence, not the only one.** Shape Up's appetite + no-backlog + cooldown + circuit-breaker suits teams that want long protected focus (Basecamp).

---

## A working checklist

Copy this when designing or reviewing a feature:

```
Linear-style review:
- [ ] Who specifically is this for? Is it opinionated, or generically for "everyone"?
- [ ] Is the problem written clearly, in my own words? Is it the real problem or a symptom?
- [ ] Concept decided before pixels? (What is each entity, really?)
- [ ] Plain language — universal terms, no invented jargon? Is microcopy (labels, errors, empty states) terse and human?
- [ ] Does every border/icon/separator earn its place? Does chrome recede?
- [ ] Tested against real/full/empty states and light/dark/custom themes?
- [ ] If a data view: clear purpose + owner, and every metric paired with comparison, history, or a threshold?
- [ ] Any spinner that near-zero latency could remove instead? If writes are optimistic, is the failure/rollback state designed (not just the happy path)?
- [ ] Are actions reversible — undo over confirmation for routine actions, recovery path designed for mistakes?
- [ ] Is there a fast keyboard path to the primary action — and, for occasional users, a discoverable see-and-point path too?
- [ ] Accessibility treated as input, not polish (keyboard, visible focus, reduced-motion, perceptual contrast, hit targets)?
- [ ] Are we adding a setting to dodge a product decision the product should get right by default?
- [ ] Are we honoring a request literally instead of the underlying need?
- [ ] Distinctive only where the payoff beats the novelty tax — or are we taxing users for novelty's sake?
- [ ] If a developer/agent surface: are the API, CLI, errors, and docs designed with the same craft as a screen?
- [ ] If AI: is there a structured workbench with review/approval, not just a chatbox?
- [ ] If AI: is the agent's *own* interface (tools, schemas, responses) designed, are there evals/observability for the non-deterministic parts, and are consequential/irreversible actions gated behind consent?
- [ ] If AI/agents: is context (decisions, the "why," code) captured where humans and agents can both use it — nothing re-explained at a handoff? And is the model's context window budgeted at inference time?
- [ ] Am I applying a principle as universal law where a boundary applies? (Check `references/boundaries-and-peers.md`.)
```

---

## Reference files

- **`references/ui-ux-craft.md`** — The Linear blog posts worth reading (calmer interface, redesign strategy, output isn't design, design is more than code, design for the AI age, quality rituals, settings, customer needs, dashboards, plus the 2026 agent-era cluster: "issue tracking is dead," code review with Diffs, and teaching agents to do the work), each with its core lessons and link.
- **`references/operating-model.md`** — How Linear actually operates: org structure, decision-making, opinionated software, speed-as-architecture, the Linear Method (plus Shape Up's appetite/cooldown/circuit-breaker as an alternative cadence), hiring, and planning mechanics.
- **`references/boundaries-and-peers.md`** — Where Linear's principles have limits: 8 productive contradictions with peer companies (Notion, Stripe, Basecamp, Apple, Vercel, Superhuman, The Browser Company), each with the deciding variable, plus a corroboration table of where the design canon independently agrees with Linear.
- **`references/accessibility-and-craft-specs.md`** — The checkable layer Linear under-documents: accessibility as a discipline (keyboard, focus, ARIA, APCA contrast, reduced motion) and quantified craft thresholds (hit targets, 16px inputs, press/dialog scale, tabular numerals) an agent can enforce mechanically.
- **`references/sources.md`** — Primary Linear sources plus peer-company sources, interviews/profiles, technical breakdowns, and background, with sourcing caveats.
