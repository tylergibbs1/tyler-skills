# Evidence behind the skill

## Contents
- The task
- Pilot 1: keep rules and seeds
- Pilot 2: plain loop against a strict harness
- The proxy that didn't transfer
- Related papers
- Lab and practitioner guides

## The task

A small attention head on cached image-encoder features for a multi-label image task. 5
grouped folds for development. The lockbox is a few hundred images from 16 held-out groups
that no arm ever scored. Each arm had the same starting code and a fixed GPU budget. Lockbox numbers come from
training the baseline and the arm's best commit on all development data and scoring both over
8 seeds, paired, with a group bootstrap 95% CI.

## Pilot 1: keep rules and seeds (3 GPU-hours per arm)

| Arm | Rule | Runs | Dev gain | Lockbox gain (95% CI) |
|---|---|---|---|---|
| A | 1 seed, keep any gain | 47 | +13.4 | +9.3 [5.2, 14.6] |
| C | 1-seed screen, 8-seed confirm, clear gain | 15 | +9.7 | +9.1 [4.9, 14.4] |
| B | 8 seeds, keep clear gain | 6 | +7.4 | +7.6 [4.0, 12.4] |
| D | 8 seeds batched, written contract, clear gain | 4 | +4.4 | +1.9 [0.6, 3.5] |

Reading pilot 1: A, C and B overlap, so it does not separate keep-any-gain from screened
acceptance. What it shows is that D, which afforded only 4 runs, lost. Idea order is confounded
with the rule (every winner found the learning rate; no loser tried it). Prior work agrees the
answer depends on the task: greedy loops rank first on tasks with many easy gains and last on
sparse ones (FML-bench).

## Pilot 2: plain loop against a strict harness (1 GPU-hour per arm)

| Arm | Rule | Runs | Dev best | Lockbox gain (95% CI) |
|---|---|---|---|---|
| P1 | 1 seed, keep any gain | 15 | 0.790 | +8.1 [3.9, 13.3] |
| P2 | 1 seed, keep any gain | 16 | 0.783 | +6.9 [3.3, 11.2] |
| P3 | 1 seed, keep any gain | 14 | 0.734 | +3.6 [1.5, 6.8] |
| V1, V2, V3 | 8 seeds, 2-seed screen, clear gain | 5, 5, 6 | baseline | 0, 0, 0 (nothing kept) |

Baseline dev score 0.647. The V arms fit about 3 full runs into the budget and spent them on
label smoothing, mixup, dropout and model averaging. All three P arms found that the head was
under-trained and over-regularised: learning rate x2 or more, more epochs, less token dropout.

## The proxy that didn't transfer

A cheaper version of the task (2 views, pooled tokens, 3 folds, 20 GPU-minutes per arm) ran
6 arms. Dev gains of +2.5 to +6.0 became -1.1 to +1.1 on the lockbox, every interval crossing
zero, though the proxy ranked 9 of 10 ideas from a full-task arm in the right direction.

## Related papers (2026 preprints)

- Winner's Curse in LLM Self-Improvement Loops (arXiv 2610.09239): keep-any-gain loops inflate
  their own score (+12.5 on the selection set, -0.6 held out); stricter keep rules did not
  reliably do better held out; the fix is scoring the start and the final pick once on
  untouched data.
- Closed-loop Auto Research for Molecular Property Prediction (2606.22731): search freely, then
  check the frozen pick once on held-out data.
- How Much of a Harness Does a Strong Agent Need for Autonomous ML Engineering?: shell and
  filesystem access mattered most; no extra layer beat a plain session.
- Autoresearch with Coding Agents on Quran Recitation Data (2607.18064): held-out results
  differ by model; some models stop at a plateau, others push the watched metric.

## Lab and practitioner guides (added 2026-11-13)

| Rule in SKILL.md | Source | Support |
|---|---|---|
| Spread ideas across families; rotate | Meta, arXiv 2511.15593; RE-Bench, arXiv 2411.15114 | Measured: forcing similar ideas cut MLE-bench-lite medal rate by 6.9 and 8.4 points; RE-Bench agents used lightly modified transformers 84% of the time on one task |
| 2 to 4 independent arms | RE-Bench; MLE-bench, arXiv 2410.07095 | Measured, scaffold-dependent: medal rate 16.9% at 1 attempt vs 34.1% at 8 (oracle pick); this skill's identical arms spread +3.6 to +8.1 |
| Re-check LR at 0.5x/1x/2x after a structural change | Google Deep Learning Tuning Playbook (github.com/google-research/tuning_playbook); Choi et al. 2019, arXiv 1910.05446 | Measured: optimizer rankings reverse with the tuning protocol |
| Re-score the last few kept commits before freezing | AIRA, Meta, arXiv 2507.02554 | Problem measured (validation kept rising while test plateaued); the remedy is inferred |
| Lockbox minimum detectable gain | Anthropic, "A statistical approach to model evaluations" | Statistical theory; clustered errors can exceed naive ones over 3x |
| Read curves; score the best checkpoint | Tuning Playbook | Practitioner opinion |
| Sanity checks with no reference score | Karpathy, "A Recipe for Training Neural Networks" (2019) | Practitioner opinion |
| Simpler code wins ties | Karpathy autoresearch program.md; Tuning Playbook; Schulman | Opinion |
| Kill at 2x expected time; clear stale GPU processes | RE-Bench, MLE-bench failure reports | Observed agent failures |

Where the sources disagree with this skill: the Tuning Playbook says never tune training
length inside a study. Kept here as a lever because epochs won in all three pilot arms.

Considered and left out: quasi-random or Bayesian search (needs many parallel trials; the
playbook itself says tune only the learning rate under ~10 trials); tree or evolutionary search
(marginal over greedy in AIRA); muP transfer (needs reparametrising the model); ensembles
(unmeasured, and averaging arms gained nothing in the pilots).

## Simulation of acceptance rules (added 2026-11-13)

A seeded numpy model of a budgeted search: a queue of ideas with true effects (sparse, dense and
harmful mixtures), seed noise, dev-vs-lockbox mismatch, additive gains, and a final lockbox
certify. 900 cells, 10,000 searches each. Calibrated to the pilot (simulated dev +14.0 and lockbox
+8.9 vs the pilot's +13.4 and +9.3).

- One seed, keep any gain is never beaten by more than 1 point while ideas outnumber runs; it
  leads screen-and-confirm and k-seed rules by about 1.5 points at 20 runs and 5 to 8 at 100,
  when seed noise is no bigger than a typical helpful effect. At 10 runs or fewer all rules tie.
- Idea order moves gains more than the rule (+8.9 big levers first vs +3.6 random, same rule). A
  4-idea arm loses badly only when its order is also poor.
- Multi-seed rules win only with fewer ideas than runs (up to 2x the gain) or very large budgets.
- Keep-any-gain has a 13% average chance of a truly negative pick (8 seeds: 2%); more seeds remove
  only seed-noise inflation, and every rule loses most of its dev gain to dev-lockbox mismatch.
- Freezing the earliest of the last 3 kept commits not clearly beaten changed true gain by −0.07
  points when re-scoring was free and −0.91 when its runs came from the budget: not adopted.

Assumptions that matter: a fixed idea queue (agents that adapt to noisy results are not modelled),
additive gains (saturation halves the cells where keep-any-gain wins but reverses none), and a
clear-gain bar set to one seed SD.
