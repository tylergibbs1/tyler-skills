---
name: proving-value-before-building-out
description: Sequence new product or feature work as a headless "prove" phase that validates the core value on real inputs before any UI, microservices, or scaling. Use at the start of a new product/feature, or once a core engine exists and the user is about to add UI or infra. Distinct from scope-discipline: this is positive sequencing (prove the core first), not "don't gold-plate".
---

# Proving Value Before Building Out

Before building UI, infrastructure, or scale, prove the core value proposition works. This developer explicitly asks for this sequencing ("first i want to set a prove phase to see if the core value prop actually works... no ui or microservices yet"). It is not the same as scope-discipline: scope-discipline says do not over-build a given task; this says get the hard part right and validated before building outward.

## The sequence

1. **Prove phase (headless).** Build just the core engine and run it end to end on realistic, real-world inputs. No UI, no microservices, no scaling yet. "this doesnt need to have a UI or anything, this is just for the dev to benchmark and debug."
2. **Harness it.** Stand up a dev-only eval/benchmark so you can measure quality on real cases and A/B compare approaches, not eyeball one example. When quality is the whole point ("i want to focus on the quality of the quotes, this is paramount"), this harness is the deliverable, not a nice-to-have.
3. **Use real data, not mocks.** Prove it against real scenarios so the signal is trustworthy. Mock data hides the failures that matter.
4. **Only then build outward.** Add UI, services, and scale once the core value is demonstrated and measured.

## When to apply

At the start of a new product or feature, or the moment a working core exists and the next instinct is to add UI/infra. Offer the prove phase first, and if there is no eval harness, propose building one before the core logic is trusted.
