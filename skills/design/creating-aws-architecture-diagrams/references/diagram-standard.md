# AWS Diagram Standard

## Contents

- Perspective selection
- Resource and boundary rules
- Relationship rules
- Default visual system
- Validation checklist
- Research sources

## Perspective Selection

Give every diagram a literal purpose in its title or subtitle, such as:

- High-level current runtime
- Monthly collection sequence
- Deployment and image promotion
- Failure, retry, and recovery
- Network and trust boundaries
- Proposed queue-based scale-out

An overview may reduce detail, but it must not mix unrelated perspectives. If a
viewer needs chronological round trips, create a sequence diagram rather than
forcing behavior into a topology diagram.

## Resource And Boundary Rules

- Label resources by descriptive name first and AWS service type second.
  Example: `Compliance evidence` / `Amazon S3 Object Lock`.
- Show a resource once per perspective. Repetition can imply separate resources.
- Connect every resource. If its relationship cannot be stated, omit it.
- Use the smallest truthful boundary set. AWS account, Region, VPC, private
  subnet, and external system have different meanings and are not interchangeable.
- Managed regional services such as DynamoDB and S3 are not inside a VPC merely
  because a VPC workload calls them.
- Keep third-party services and public websites outside the AWS account boundary.
- Use real logical names when known. Never expose account IDs, secret values, or
  sensitive endpoint details merely to make the diagram look specific.

## Relationship Rules

Create an allowlist before drawing:

```text
Monthly schedule -> Collector task: RunTask once per month
Collector task -> State table: Read/write progress and checkpoints
Collector task -> Evidence bucket: Append evidence
Collector task -> CloudWatch: Logs and metrics
```

For each edge:

- choose one source, destination, and action;
- use a verb phrase or protocol label;
- use an arrowhead whose direction matches the stated action;
- route it without crossing a resource or continuing past its destination;
- keep independent edges independent instead of merging them ambiguously.

Use solid neutral lines for normal dependencies and data flow. Use dashed orange
lines for invocation failure, DLQ, or recovery paths. Avoid animation and
decorative motion.

## Default Visual System

- Canvas: 16:9 landscape; `3840x2160` when 4K is requested.
- Background: white with an extremely subtle neutral dot grid.
- Typography: Inter or a similar geometric sans serif; dark neutral text;
  resource name semibold and service type regular.
- Palette: neutral greys plus muted blue for trigger, purple for compute, green
  for storage, and orange for failure/observability.
- Components: flat, no gradients, no shadows, 1.5-2px strokes, generous
  whitespace, and corner radius no greater than 10px.
- Icons: one current AWS icon family, consistent size and treatment. Do not
  invent icons when an official service icon is available.
- Title: literal system or perspective name, not a marketing headline.

The bundled `assets/style-reference.png` is a visual reference only. Its
Meridian topology, wording, and resource selection are never defaults.

## Validation Checklist

Do not finalize until every item passes:

```text
- [ ] One perspective and audience are explicit.
- [ ] Architecture matches code, IaC, and approved decisions.
- [ ] Every resource has a name and type.
- [ ] Every resource is connected exactly as intended.
- [ ] Every arrow is present in the allowlist and correctly directed.
- [ ] No line crosses a box, merges ambiguously, or overshoots its target.
- [ ] Failure paths are distinct from normal paths.
- [ ] Boundaries and containment are technically accurate.
- [ ] Current and future architecture are not mixed.
- [ ] Text is exact, readable, and free of overlaps.
- [ ] No secrets, account IDs, or unnecessary internal endpoints appear.
- [ ] PNG dimensions and project path are verified.
```

## Research Sources

- AWS architecture icons: https://aws.amazon.com/architecture/icons/
- AWS sequence diagram guidance: https://aws.amazon.com/blogs/architecture/sequence-diagrams-enrich-your-understanding-of-distributed-architectures/
- AWS diagram tooling and documentation grounding: https://aws.amazon.com/blogs/machine-learning/build-aws-architecture-diagrams-using-amazon-q-cli-and-mcp/
- Ilograph common diagram mistakes: https://www.ilograph.com/blog/posts/more-common-diagram-mistakes/
- Ilograph runtime versus deployment perspectives: https://www.ilograph.com/blog/posts/better-aws-architecture-diagrams-distributed-load-testing/
- Ilograph master diagram guidance: https://www.ilograph.com/blog/posts/breaking-up-the-master-diagram/
