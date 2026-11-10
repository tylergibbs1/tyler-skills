---
name: wcml
description: Runs machine-learning work the way world-class ML research teams do - a trusted evaluation, error review by eye, ceilings before methods, one variable per experiment with a control and a pre-written kill line, fast proxies, few deep bets, and a ledger of every result. Use when the user says "wcml", "world class ML", or asks for research-grade rigor while improving a model, running ablations or training runs, choosing between models, brainstorming ML ideas, or chasing a metric. Don't use for one-off model inference, ML explainers with no experiments, or plain software bugs in ML code.
---

# World-class ML research loop

Strong teams win by choosing better experiments, not by running more of them. Work through
the loop below in order and keep the checklist in your notes. Return to step 2 after every
adopted change.

```
- [ ] 1. Evaluation is trusted (split, noise floor, paired comparison, lockbox)
- [ ] 2. Errors reviewed by eye and counted by failure category
- [ ] 3. Ceiling measured for the idea before building it
- [ ] 4. Experiment written down: one change, control, comparison, kill line
- [ ] 5. Fast proxy run first; only survivors get full compute
- [ ] 6. Result recorded in the ledger (including dead ones), audited for confounds
- [ ] 7. Reported as delta + CI + what it rules in or out
```

## 1. Trust the evaluation

Split the data the way the test set is split (by person, site, scene, collection), measure
the seed-to-seed noise floor, and compare configs only paired on identical folds and seeds.
Report a group-macro co-metric when a few groups dominate the item count. Keep a lockbox
that nothing trains or tunes on. Read `references/evaluation.md` before the first
comparison in a project or when results look too good.

Score a comparison by running:
`python scripts/paired_bootstrap.py scores.csv` (columns: group, a_correct, b_correct).
Treat a delta whose CI crosses zero as not proven.

## 2. Look at the errors before proposing fixes

1. Slice the current best out-of-fold errors by group, class and source; find where they
   concentrate.
2. Render contact sheets of misses with label, prediction and any boxes:
   `python scripts/contact_sheet.py misses.csv out_dir`. View them.
3. Tag every miss with one failure category and count them; check the pipeline (crop,
   rotation, resize, label join) on the misses numerically.

For large error sets, split the sheets across parallel reviewers with a fixed category
list and a synthesizer; follow `references/error-analysis.md`. Seed every brainstorm with
these counts. Never brainstorm without a fresh error review.

## 3. Measure the ceiling first

Before building a method, measure its oracle: perfect boxes or crops, oracle features, the
union of two models' correct answers, a strong teacher combined with the current model.
Build only if the oracle gain clears the noise floor with room to spare. The oracle also
tells you what target is realistic.

## 4. Write the experiment before running it

Fill one row of `assets/experiment_template.md` per experiment: hypothesis tied to a
failure category, the single change, the control (identical data, folds, seeds, epochs,
augmentation and step count; extra steps get a switched-off twin), the comparison files,
and a kill line decided now. Read `references/experiment-design.md` when the method adds
training steps, data, or a second model, since those are where confounds hide.

## 5. Kill cheaply, scale winners

Cache expensive features and run head-only or one-seed versions first. Spend seeds and
compute only on ideas that survive their kill line. Make jobs resumable, check disk before
large writes, run one job per machine at a time, and never leave paid hardware idle or a
failed job unnoticed.

## 6. Keep the ledger

One row per experiment: question, status (adopted, promising, dead, running, info),
baseline and candidate prediction files, delta with CI, one-line reason. Record dead results
as carefully as wins. Before recording, audit the run for confounds: a run that changed two
things or used a different baseline is rerun, not recorded. Validate the ledger file with a
test if a dashboard reads it.

## 7. Report

Lead with the outcome. Give the delta with its CI, recall on the classes that matter, and
what the result rules in or out. Say plainly when a target looks unreachable with the
current approach and what new ingredient would be needed. Rank next steps by expected gain
per compute-hour against the failure counts, and prefer one deep bet on the biggest
category over many small tweaks inside the noise.

## Stop signs

Stop and fix the process when any of these happen: proposing fixes without having looked at
misses; comparing against a baseline with different folds, seeds or data; calling a gain
inside the noise floor a win; tuning on the test set or lockbox; changing two things at
once; giving the method more training than its control; re-running an idea the ledger says
is dead; launching hours of compute for a question a minutes-long proxy can answer.
