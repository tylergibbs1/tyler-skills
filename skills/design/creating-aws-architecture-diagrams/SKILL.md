---
name: creating-aws-architecture-diagrams
description: Creates precise, modern AWS architecture diagrams as PNGs or Mermaid, grounded in source code, infrastructure code, and current AWS guidance. Use when a user asks for an AWS architecture diagram, cloud topology, runtime or deployment view, failure or recovery flow, AWS service visualization, implementation handoff graphic, or a clean Figma/Linear-style 16:9 diagram with AWS icons.
---

# AWS Architecture Diagrams

Create a focused technical view, validate its topology, then render it. Treat a
correct relationship map as the source of truth; visual polish never excuses an
incorrect arrow, boundary, label, or resource.

## Workflow

1. **Choose one perspective.** State the audience and question the diagram must
   answer. Default to a high-level current runtime view. Split deployment,
   failure/recovery, security, and future scale-out into separate diagrams when
   they would clutter or contradict that view.
2. **Ground the topology.** Read the relevant code, IaC, configuration, and
   architecture notes. Verify unstable AWS details with current official AWS
   documentation. Mark unresolved claims as assumptions; do not invent them.
3. **Write the diagram contract.** Before rendering, define:
   - boundaries and the resources contained by each;
   - each resource's descriptive name and AWS service type;
   - an allowlist of `source -> destination: relationship label` edges;
   - failure edges and forbidden edges;
   - items deliberately omitted from this perspective.
4. **Check the contract.** Every resource must be connected, every edge must
   have one meaning, and no current resource may be confused with a future one.
   Read [references/diagram-standard.md](references/diagram-standard.md) for the
   complete technical and visual rules.
5. **Render the requested format.** Use Mermaid for an editable documentation
   artifact. For a polished PNG, load the `imagegen` skill, use the built-in
   image generation tool, and read
   [references/image-prompt-template.md](references/image-prompt-template.md).
   Pass `assets/style-reference.png` as a style-only reference when the user
   wants this skill's default visual language. Explicitly replace its topology
   and text; never copy Meridian content into another system.
6. **Inspect at full resolution.** Use `view_image` and compare every boundary,
   resource, label, and connector with the contract. Reject and regenerate any
   image with a fabricated, missing, duplicated, merged, reversed, or
   continuing-past-destination edge. Also reject misspellings and unconnected
   resources.
7. **Verify the artifact.** Confirm PNG dimensions and save it in the requested
   or project-local path. When exact dimensions are required, run:

   ```bash
   python scripts/ensure_png_size.py input.png output.png --width 3840 --height 2160
   ```

   Upscaling satisfies delivery dimensions but does not add model detail. If
   labels are unclear at source resolution, regenerate instead of upscaling.

## Non-negotiable Rules

- Use current official AWS icons when icons are requested; pair each with both
  a descriptive resource name and its service type.
- Draw account, Region, VPC, subnet, and external-system boundaries only when
  they answer the perspective's question. Containment must be technically true.
- Use directed, labeled connectors. Avoid bidirectional arrows; use a single
  labeled dependency or two explicit edges when both directions matter.
- Use a visually distinct dashed path for failures. Do not merge failure and
  normal data flow.
- Do not create a "master diagram." Prefer a clear overview plus focused views.
- Do not mix current and proposed architecture without a visibly separate
  perspective.
- Do not accept an AI-generated diagram without visual verification against the
  relationship allowlist.

## Deliverables

Return the saved artifact path, its dimensions, and the perspective it depicts.
When the diagram is implementation-facing, keep the contract or Mermaid source
beside the PNG so future changes remain reviewable.
