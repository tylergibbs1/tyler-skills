# Exemplar Repos

A living list of open-source repos worth studying, grouped by what they exemplify. Add to it as new reference repos prove useful. For each entry: what to study it for, and what NOT to borrow (staleness, license, or scope caveats).

## Contents
- Effect-TS and functional TypeScript
- TanStack Start and TanStack ecosystem
- UI/UX, SSR, and product polish
- How to add a new exemplar

## Effect-TS and functional TypeScript
- **opencode** — Strong Effect-TS practices: service/layer composition, error channels, and idiomatic functional structure in a real product. Study how it models services and threads dependencies. Use for structure and idiom; confirm current Effect APIs against Context7 (`effect` moves fast).

## TanStack Start and TanStack ecosystem
- **tanstack.com** (the TanStack website repo) — A real TanStack Start app: routing, loaders, server functions, and SSR wiring done by the framework's own authors. Study route layout, data loading, and server-function boundaries. Good default when scaffolding a TanStack Start feature.

## UI/UX, SSR, and product polish
- **OpenPanel** — Analytics/observability product with clean UI/UX and solid SSR rendering. Study for dashboard layout, component composition, and server-side rendering patterns when building an observability or data-dense product surface.

## How to add a new exemplar
When a repo proves useful as a reference, add a bullet under the right heading with: the repo name, the one or two things it exemplifies, and any caveat (stale library version, heavy license, or patterns that only fit a specific scope). Keep entries specific: "study X for Y", not "good code".
