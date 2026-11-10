# Evaluation you can trust

## Contents
- Splits
- Noise floor
- Paired comparison
- Co-metrics
- Lockbox
- Baselines
- Warning signs

## Splits
Group cross-validation by the unit that is new at test time: person, patient, site, scene,
camera, collection. Correlated items (several photos of one subject, frames of one video)
in both train and validation inflate scores. If the test set comes from new collections or
sites, also run a leave-one-collection-out split; expect it to score lower and track it as
its own target.

## Noise floor
Run the baseline config with at least 3 seeds and report the spread of the mean. With a few
dozen groups, a 1-2 point swing between seeds is normal. Never adopt a change whose gain is
inside that spread.

## Paired comparison
Score A and B on identical folds and seeds, then bootstrap the difference by resampling
groups (not items). `scripts/paired_bootstrap.py` does this from a CSV of per-item
correctness. Report B - A with its 95% CI. Absolute accuracy with a wide CI cannot tell two
configs apart; the paired delta often can.

## Co-metrics
When a few groups hold many items, item accuracy is dominated by them. Report group-macro
accuracy (mean of per-group accuracy) next to it and require the macro delta to be >= 0
for adoption. Also report recall for the classes the task cares about; overall accuracy
can rise while the important class gets worse.

## Lockbox
Hold out a slice (whole groups) that is never trained on, tuned on, or sent to any outside
service. Read it once, at the end, with the final config. Any decision made after reading it
makes it a validation set.

## Baselines
Know the majority-class score, a linear probe on frozen features, and the previous best,
all on the same folds. A new method that cannot beat a linear probe by more than the noise
floor is not ready.

## Warning signs
- A gain that appears only on one seed or one fold.
- Validation better than training loss would suggest.
- Results that change when an unrelated file is regenerated (non-determinism or leakage).
- Out-of-fold predictions whose item order or names differ between A and B.
