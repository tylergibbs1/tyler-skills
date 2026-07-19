---
name: learning-from-exemplar-repos
description: Ground implementation work in a high-quality reference repo instead of inventing patterns from scratch. Use when starting work in a framework (TanStack Start, Effect-TS, Next.js) or going for a specific design/style, when the user says "look at how X does it", "use Y as a reference", "match this repo's patterns", or when about to scaffold a feature in an unfamiliar stack. Pairs with grounding-with-context7, where docs tell you the API and an exemplar repo shows you how good code actually composes it.
---

# Learning From Exemplar Repos

The most reliable way to write idiomatic code in a framework is to study a real repo that already does it well, then follow its patterns. Fresh docs (via Context7) tell you the API surface; an exemplar repo shows you how a strong team actually structures, composes, and wires it in practice. Use both.

## When to reach for an exemplar

**Check for an internal precedent first.** If this codebase already does the thing well somewhere, that local code is your exemplar: read those files and match them. Reach for an *external* repo only when there is no local precedent to follow.

External exemplars are for:

- A fresh project, or a framework the codebase does not use yet, where the "right" structure is not obvious (routing, data loading, server functions, effect composition).
- Going for a specific design or UX style: find an open-source product whose look and interaction you want to approximate.
- Adopting a pattern the codebase does not yet have an internal precedent for.

## How to use one

1. **Pick a close match.** Choose a repo that exemplifies the exact framework, pattern, or style in play. Prefer repos known for craft over popularity alone. See `references/exemplars.md` for a starting set.
2. **Study before writing.** Read the parts of the exemplar that match the task: how it lays out routes/services, names things, handles errors, composes the framework's primitives. Do not skim one file and guess the rest.
3. **Adapt, do not copy wholesale.** Match the patterns and idioms, but fit them to this codebase's existing conventions. If the exemplar and the local code disagree, the local code wins unless the point is to migrate toward the exemplar.
4. **Combine with Context7.** Use the exemplar for structure and idiom, and `grounding-with-context7` for current API details and version-specific changes. The repo can be behind on the library version; the docs are the source of truth for the API.

## Sourcing an exemplar

If no exemplar is provided, propose one or two candidates and confirm before leaning on them. A repo can be idiomatic for its era but stale on the current library version, so sanity-check its patterns against current docs before adopting them wholesale. Keep `references/exemplars.md` updated as new reference repos prove useful.
