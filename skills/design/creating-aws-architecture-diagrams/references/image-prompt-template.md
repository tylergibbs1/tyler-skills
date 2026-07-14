# Image Prompt Template

Use this structure for a new PNG. Remove unused sections instead of filling them
with speculative content.

```text
Use case: infographic-diagram
Asset type: production AWS architecture PNG for [audience]
Canvas: exact [width]x[height], 16:9 landscape, presentation-safe margins
Title text exactly: "[system and perspective]"
Subtitle text exactly: "[scope, such as High-level runtime view · Current design]"

Purpose:
[One sentence describing the question this diagram answers.]

Boundaries and containment:
- [Boundary]: contains only [resources]
- [External group]: outside [boundary]

Named resources and service types:
1. Resource name "[logical name]"; service type "[AWS service]"; sublabel "[optional]"

Exact relationship map:
- [source] -> [destination], label "[verb/action/protocol]"

Failure relationships:
- [source] -> [destination], dashed orange line, label "[failure action]"

Forbidden relationships:
- No connection from [source] to [destination]
- Draw no relationship not listed above

Connector constraints:
- Use one directed arrow per listed relationship; no bidirectional arrows
- Use orthogonal connectors and clear arrowheads
- No line may cross a resource, touch an unrelated resource, merge ambiguously,
  or continue beyond its destination
- Place each relationship label beside its own connector
- Every resource must be connected

Composition:
[Give relative placement that keeps related lines short and prevents crossings.]

Visual style:
Clean Figma/Linear design language. White background with an extremely subtle
neutral dot grid. Inter or similar sans serif. Neutral text #1a1a1a, secondary
text #666, borders #d9d9d9. Muted blue trigger, purple compute, green storage,
orange failure/observe. Flat design, 1.5-2px strokes, generous whitespace,
maximum 10px corner radius. Use one current official AWS icon family and pair
icons with both descriptive resource names and service types.

Avoid:
No gradients, shadows, glows, decorative blobs, isometric art, people,
marketing copy, animation, watermark, tiny text, duplicate resource,
unconnected resource, or service not present in the architecture contract.

Text accuracy:
Render quoted labels exactly once. Ensure all text is readable and no text or
connector overlaps another element.
```

When using `assets/style-reference.png`, state:

```text
Use the reference only for visual language: typography, spacing, palette,
border treatment, icon scale, and connector weight. Replace every resource,
label, boundary, and relationship with the contract above. Do not retain or
infer topology from the reference image.
```

After generation, inspect the image at full resolution. Compare it line by line
with the exact relationship map and forbidden relationships. Regenerate with a
single targeted correction when any semantic defect is found.
