---
name: wcml
description: Runs machine-learning experiments so their gains hold up on held-out data, in one of two modes. Search mode is a budgeted agent loop - many cheap one-seed tries, big training levers first, keep any gain, then a single paired lockbox check. Bet mode is a research bet - error review by eye, ceilings before methods, one variable with a control and a pre-written kill line, paired seeds, a ledger. Use when the user says "wcml" or "world class ML", or asks to improve a model or metric, run an autoresearch or experiment loop, tune a training script within a GPU budget, run ablations or training runs, choose between models, brainstorm ML ideas, or chase a metric. Don't use for one-off model inference, ML explainers with no experiments, or plain software bugs in ML code.
---

# World-class ML experiments

Every gain must hold up on data the work never touched. How you get there depends on the job,
so pick a mode first.

| Mode | Use when | Rule of thumb |
|---|---|---|
| **Search** | Improve a metric within a budget; many cheap ideas, each a short run | Try many ideas on one seed, keep any gain, certify once at the end |
| **Bet** | Test one idea against a baseline; few expensive runs | Look at errors, measure the ceiling, write the kill line, use paired seeds |

Their seed rules differ on purpose. In search, extra seeds per idea cost ideas, and the final
lockbox check removes lucky winners. In a bet there are only a few runs, so each must count.
A bet can contain a search (tuning its own arm fairly), and a search that finds a big idea can
turn into a bet.

```
Both modes
- [ ] 1. Evaluation fixed and trusted; lockbox set aside; detectable gain known
- [ ] 2. Baseline reproduces the expected score
- [ ] 3. Smoke run on the real hardware and image
Search mode                              Bet mode
- [ ] S1. Idea list across families      - [ ] B1. Errors reviewed by eye, counted
- [ ] S2. Loop: one change, one seed,    - [ ] B2. Ceiling measured before building
          keep any gain, big levers 1st  - [ ] B3. Experiment written: change, control,
- [ ] S3. Stop at plateau or budget                kill line, fair tuning
                                         - [ ] B4. Proxy first; seeds only for survivors
                                         - [ ] B5. Ledger row, audited for confounds
Both modes
- [ ] 4. Certify once on the lockbox, paired, several seeds
- [ ] 5. Report delta + CI + what it rules in or out
```

## 1. Fix and trust the evaluation

- Split the data the way the test set is split (by person, site, scene, collection). Compare
  configs only paired on identical folds and seeds. Report a group-macro co-metric when a few
  groups dominate the item count. Read `references/evaluation.md` before the first comparison
  in a project or when results look too good.
- Put data, folds, metric and lockbox in a read-only file (`prepare.py`); edit only the
  training code. If the evaluation turns out wrong, stop, fix it, and score the baseline
  again; never change it mid-loop.
- The lockbox is data nothing trains, tunes or selects on. Split it like the real test and
  keep it behind a separate command.
- Measure the seed-to-seed noise floor and compute the smallest delta the evaluation and
  lockbox can detect. If that is bigger than the gain you hope for, say so before spending.
- Score a comparison with `python scripts/paired_bootstrap.py scores.csv` (columns: group,
  a_correct, b_correct). A delta whose CI crosses zero is not shown.

## 2. Verify the baseline

Score the unchanged code against the expected score (the last known run, the paper, the
owner's number). A gap beyond seed noise is a bug in data, evaluation or pipeline: find it
before trying any idea. One baseline scored 42% against an expected 65% because mirrored
views had their classes swapped instead of their left and right sides.

With no trusted expected score, check three ways instead: loss at the start matches chance,
blanked inputs score worse than real ones, and a batch of 2 to 8 examples overfits.

Check that the evaluation can answer the question. If a result should depend on some
quantity, measure that quantity directly. One synthetic test could never produce the
uncertainty its kill line was about, so it would have "killed" the idea without asking.

## 3. Smoke run

Before any long run, run a tiny version on the real machine and image: imports, GPU, disk,
one step of every arm. More GPU time was lost to setup failures (a missing package, an
externally managed Python, an empty git checkout) than to bad ideas.

## Search mode

In two pilots on one task (10 agent arms, each scored on a lockbox), the arms that lost were
the ones whose rules let them afford only 4 to 6 ideas (8 seeds per idea, or a budget eaten by
confirmations): they gained +1.9 or nothing, while arms that tried 14 to 47 ideas gained +3.6 to
+9.3. The pilots do not show that keeping any gain beats a cheap screen: a one-seed screen with
a single 8-seed confirm (+9.1) tied keep-any-gain (+9.3). Every winning arm also found the
learning rate, so idea order matters as much as the rule. Treat this as one task's evidence.
Details: `references/search-evidence.md`.

**S1. Set up.** Commit every try; `git reset --hard` drops one. Log each run to `results.tsv`
(commit, change, score, kept or dropped, GPU-seconds). Fix the per-run time limit and total
budget first. Write the idea list across families: optimisation, data, loss, architecture,
inference. With a big budget, split it into 2 to 4 independent arms from the baseline with
fresh context and certify the best arm; identical pilot arms ended at +3.6, +6.9 and +8.1.

**S2. The loop.**
- Order the idea queue before anything else; it matters more than the acceptance rule. Big
  levers first: step the learning rate by 2x until it drops, then epochs, then regularisation
  strength. In simulation, the same rule gained +8.9 with big levers first and +3.6 in random
  order; all three winning pilot arms found the learning rate.
- One change per try, one seed, keep it if the score rises at all. Don't re-confirm each idea
  on many seeds; that is what starved the losing arms. In simulation this rule is never beaten
  by more than 1 point while ideas outnumber runs, and leads by 1.5 to 8 points at 20 to 100
  runs. Its cost is about a 1-in-8 chance the final pick is truly worse, which the lockbox
  check catches.
- Switch to 2 seeds and keep only clear gains when you have fewer ideas than runs (say 15 ideas
  for 100 runs) or a very large budget; there, extra seeds help.
- Read the train and validation curves to pick the next lever: still improving means train
  longer; validation rising while train falls means regularise. Score the best checkpoint.
- After a structural change (architecture, loss, data pipeline), try 0.5x, 1x and 2x the
  learning rate before logging it dead.
- Rotate idea families. When one stops paying, the next try comes from a different family.
- At an equal score, keep the simpler code. Make runs cheaper when the score allows (cached
  features, mixed precision); a cheaper run buys more ideas.
- One seed can't tell a bad idea from a collapsed run: check per-fold scores before trusting
  a big drop. Treat a setting next to a cliff (the highest learning rate before divergence)
  as fragile. Don't retry an idea the log shows failing unless what it depended on changed.
- Use a cheaper proxy task only after showing its gains carry over to held-out data. A
  plausible proxy ranked 9 of 10 ideas right and still transferred nothing.

**S3. Stop** after about 10 runs in a row without a gain, or when the budget can't fit another
run. Write `SUMMARY.md`: best commit, kept changes, what failed, next ideas. Then step 4.

## Bet mode

**B1. Look at the errors before proposing fixes.** Slice the current best out-of-fold errors by
group, class and source. Render contact sheets of misses with label, prediction and any boxes
(`python scripts/contact_sheet.py misses.csv out_dir`) and view them. Tag every miss with one
failure category and count them; check the pipeline (crop, rotation, resize, label join) on the
misses numerically. For large error sets follow `references/error-analysis.md`. Seed every
brainstorm with these counts.

**B2. Measure the ceiling first:** perfect boxes or crops, oracle features, the union of two
models' correct answers, a strong teacher combined with the current model. Build only if the
oracle gain clears the noise floor with room to spare.

**B3. Write the experiment before running it.** Fill one row of `assets/experiment_template.md`:
hypothesis tied to a failure category, the single change, the control (identical data, folds,
seeds, epochs, augmentation and step count; extra steps get a switched-off twin), the
comparison files, and a kill line decided now and above the detectable delta. Tune the method
as fairly as the control: one run at the baseline's tuned learning rate is a confounded test,
so check it at 0.5x, 1x and 2x before its kill line can kill it (Choi et al. 2019, arXiv
1910.05446). Read `references/experiment-design.md` when the method adds training steps, data,
or a second model.

**B4. Kill cheaply, scale winners.** Cache expensive features and run head-only or one-seed
versions first. Spend seeds and compute only on ideas that survive their kill line.

**B5. Keep the ledger.** One row per experiment: question, status (adopted, promising, dead,
running, info), baseline and candidate prediction files, delta with CI, one-line reason.
Record dead results as carefully as wins. A run that changed two things or used a different
baseline is rerun, not recorded.

## 4. Certify once

Freeze the best commit as it stands; re-scoring the last few kept commits before freezing cost
about a point in simulation when its runs came from the budget. Train the baseline and the pick on
all development data, score both on the lockbox with several seeds (8 in the pilots), paired
on the same seeds and items, and run `scripts/paired_bootstrap.py`. Its `scores.csv` has one
row per lockbox item: the item's group, then the baseline's and the pick's score on it,
each averaged over seeds.

Run this once. Expect the gain to shrink: pilot dev gains of +8.6, +13.4 and +14.2 became
+3.6, +9.3 and +8.1 on the lockbox.

## 5. Report

Lead with the lockbox delta and its CI. Then the dev delta, the number of runs, the kept
changes (marking single steps inside the noise), recall on the classes that matter, and what
the result rules in or out. Say plainly when a target looks unreachable with the current
approach and what new ingredient would be needed. Rank next steps by expected gain per
compute-hour.

## Logging

Log to answer questions written before the run, in a form an agent can query.
- Every evaluation writes per-item predictions: id, group, label, prediction, confidence.
  Error review, paired bootstrap and slicing all need them.
- Score the real metric cheaply at a few checkpoints (a kNN or linear probe at 25, 50 and 75%
  of training), so a failing run can stop early on the number that matters.
- Split the loss by what makes the task hard (motion, size, class, region), so an average
  can't hide where the method works and where it fails.
- Dump a few input batches with crops, masks and labels drawn on at the start of each run.
- End each run with a short summary file (the numbers the verdict needs, warnings, anything
  unusual). Read it first; open raw logs only to dig in.
- Skip per-step scalars nobody asked about and logging that syncs the GPU every step; with
  enough unplanned signals, one will "explain" any result.

## Paid compute

- Never leave a paid GPU idle: queue the next job or delete the instance when a run ends.
- Run long jobs detached with a log, make them resumable, and check disk before big writes.
- Check the balance or quota before launching anything long.
- Kill a run at twice its expected time, and stale GPU processes before the next.

## Stop signs

Stop and fix the process when any of these happen: changing the evaluation mid-loop; tuning
or selecting on the lockbox; trying ideas before the baseline reproduces; comparing against a
baseline with different folds, seeds or data; calling a gain inside the noise floor a win (in
a bet); proposing bet-mode fixes without having looked at misses; changing two things at once;
giving a method more training than its control; killing a method judged only at the
baseline's learning rate; re-running an idea the log says is dead; spending many seeds per
idea inside a search; trusting a proxy whose gains haven't been shown to transfer.
