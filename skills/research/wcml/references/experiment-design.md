# Experiment design without confounds

## Contents
- The one-change rule
- Controls for common method types
- Kill lines
- Fast proxies
- Auditing a finished run

## The one-change rule
Candidate and control differ in exactly one thing. Same data, folds, seeds, epochs,
augmentation, optimizer schedule, step count and preprocessing. If two things must change
together, run the intermediate arm too.

## Controls for common method types
- **Fine-tuning after a frozen stage (LP-FT, LoRA):** the control runs the identical second
  stage with the adapters frozen at zero, so "more head training" is separated from
  "encoder tuning".
- **Extra data (frames, external sets, pseudo-labels):** the extra rows add optimizer steps;
  give the control the same number of steps (repeat the original data) or report both.
- **Auxiliary losses:** a weight-0 version must reproduce the baseline exactly; test that.
- **Ensembles:** compare against a seed bag of the single model with the same member count,
  not against one seed.
- **Teacher or oracle inputs:** run the oracle arm first (upper bound), then the shippable
  arm with predicted inputs; report the share of the oracle gain retained.
- **Augmentation policies:** keep prediction-time views clean and identical; change only the
  training views.

## Kill lines
Write before running, in numbers: minimum delta, minimum CI lower bound, and a mechanism
check (e.g. recall on the targeted class must rise by at least N points). A result that
passes on accuracy but fails the mechanism check is suspect: the gain came from elsewhere.

## Fast proxies
Cache frozen features and run head-only arms; cut seeds to one and folds to the minimum
that still pairs; use a subset of epochs when the curve flattens early. Promote to full
seeds only when the proxy clears its kill line.

## Auditing a finished run
Before recording: confirm both prediction files have the same items in the same order;
confirm the baseline file is the intended one; diff the two configs; check the run's logs
for silent fallbacks (missing file -> retrained baseline, unboxed items keeping full weight,
a crashed arm). If anything differs besides the one change, mark the run confounded and
rerun.
