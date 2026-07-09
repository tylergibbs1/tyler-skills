---
name: mirroring-layout-in-loading-states
description: Make every loading state structurally match its own route's real content so there is zero perceived layout shift. Use when building or reviewing any loading.tsx, skeleton, Suspense fallback, or first-sync/import progress UI. Covers per-route fidelity, accessibility, and never showing "done" or stale data while work is still running.
---

# Mirroring Layout In Loading States

Loading states that do not match the real content cause perceived layout shift, and progress UI that lies about state erodes trust. Both are recurring, concrete failures here (a child page reusing the dashboard's skeleton, a flex mismatch, an import banner still showing while it is done).

## Rules

- **Mirror the route's own layout.** A skeleton or `loading.tsx` must replicate the structure and dimensions of the content it is standing in for, on that specific route. Do not reuse a parent or sibling page's skeleton. "it should be the exact layout of the actual thing so there is no precieved layout shift."
- **Match the real element sizes and container.** If the real content is a grid, the skeleton is that grid; if a flex row, match it. Mismatched flex/grid is a common cause of the shift.
- **Accessibility.** Give loading regions proper `aria` attributes (for example `aria-busy`, a status role) so the state is announced, not just visual.
- **Never lie about state.** Do not flash premature or stale data, and do not show "done" / hide the loader while work is still running. A progress banner must reflect the actual job status. "its still showing this even though its done" is the failure to avoid.

## Reviewing loading states

Check each route's `loading.tsx` against that route's real component, not the dashboard default. Confirm the swap from skeleton to real content does not move anything, and that terminal states (done, error, empty) are honest.
