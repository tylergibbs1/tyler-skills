---
name: running-ml-experiments
description: >-
  Runs ML research as a loop of pre-registered kill tests: write the bar before any
  number, check the test data is truly unseen, screen cheaply, gate on dev, confirm on
  fresh data with paired clustered statistics, and keep rented GPUs from leaking money.
  Use when planning, running, delegating or judging ML experiments, ablations, model
  comparisons or research bets, or when the user says "kill test", "pre-register",
  "is this real", "run it on pods", or "keep the research loop going".
license: MIT
metadata:
  author: tylergibbs
  version: '1.0.0'
---

# Running ML experiments

A research bet is a claim plus the cheapest experiment that could kill it. Most wrong
conclusions in agent-run research come from four places: test data that is not really
unseen, a pass line chosen after seeing the number, single-seed noise read as signal,
and baselines that are weaker than the published method. This skill closes each one.

## Gotchas (read before the first run)

- **"Held-out" data is often a near-copy of training data.** Benchmarks built by
  replaying a few demonstrations with noise, splits by episode instead of by source,
  and files named `*_val` that are a slice of the train file all leak. A method can
  look +8 better and be pure recall. Before trusting any test set, run
  `scripts/near_duplicates.py` against the training set and report the fraction
  within tolerance. If you cannot show it is far from training, call results
  "familiar-set" results.
- **A test set is spent once you have looked at a number on it.** Re-using it for the
  next decision turns it into dev data. Keep a registry of sets (see
  [references/ledger.md](references/ledger.md)) and claim a set before any episode on it.
- **Compare against the published method, not only your own baseline.** A big gain
  over your own weak baseline can vanish against the official one. Every claimed win
  needs one arm running the published method under its published protocol, in the
  same process, on the same tasks.
- **Average error is a bad proxy for decisions.** Lowering a model's mean error can
  land entirely on cases that do not change the outcome. Measure the decision you care
  about (success, pick quality), or weight error to the cases where the decision can
  still change.
- **Single-seed sweeps on ~150 items swing by about ±8 points.** Use two or more seeds,
  pair the arms on identical items, and cluster the bootstrap by the unit that
  repeats (task, source demo, user), never by row.
- **Loose success rules hide the real ranking.** "On target at any step within the budget"
  rewards pushing an object through the goal; a +26 win became −26 when the object had to
  end on target, and a published method went from 74% to 6%. Report end-state success, a
  shorter time budget and serial (one-episode) latency next to the official rule, and give
  every arm the same stopping behaviour before crediting a gain to the model.
- **Average-error screens kill real gains.** A bet with +23 strict was killed by a
  one-step-error screen. Screen on decisions instead: model-vs-simulator agreement on the
  planner's own picked plans. Advance when its lower bound is above 0, kill only when its
  upper bound is at or below 0, otherwise run the full gate.
- **A rented GPU at 0% is a planning bug.** Check `nvidia-smi` and the CPU quota once jobs
  start; batch model inference on the GPU across candidates and episodes, and shard
  simulation across every core.
- **Read the mechanism, not only the score.** When a run passes or fails, find the
  measured reason (an oracle swap, a probe, a failure-type count). A pass with no
  mechanism is a candidate for the next leak.
- **Rented GPUs leak money silently.** Agents create pods above the price cap, train
  on CPU by mistake, and die mid-run leaving pods billing. See
  [references/compute.md](references/compute.md) before creating any pod.

## Workflow

Copy this checklist into your notes and tick it off per bet:

```
Bet: <name>
- [ ] 1. Claim and ceiling: what would a perfect version of this part buy? (oracle swap)
- [ ] 2. Ledger row written: arms, data, seeds, bar, kill line, BEFORE any number
- [ ] 3. Test sets checked unseen (near_duplicates.py) and claimed in the registry
- [ ] 4. Cheap screen (offline / stored data) if one exists; stop if it kills
- [ ] 5. Dev gate: two seeds, paired, clustered CI; stop if it fails
- [ ] 6. Fresh test on a never-run set, published-method arm included
- [ ] 7. Verdict filled in the ledger row; lines never moved
- [ ] 8. Mechanism: why it passed or failed, with a number
- [ ] 9. Compute torn down and confirmed
```

**Step 1. Ceiling first.** Before building anything, replace the part you want to
improve with an oracle (true state, exact physics, perfect labels) on stored data. If
the oracle buys little, the bet is dead for free. If it buys a lot, it bounds the bar.

**Step 2. Write the row first.** Use the template in
[references/ledger.md](references/ledger.md). The kill line is a number and a CI
condition, for example "delta >= +3 AND task-clustered 95% CI lower > 0 AND losses
<= 29 per seed". A row written after a number exists is a description, not a test;
label it that way.

**Step 3. Prove the data is unseen.**

```bash
python scripts/near_duplicates.py --train train_feats.npy --test test_feats.npy --tol 20
```

Features are whatever defines "the same situation" (start poses, goal poses,
normalised image embeddings). Any test item within tolerance of training goes in the
report. Generate new data from the simulator or source when the fraction is high.

**Step 4-6. Screen, gate, test.** Each stage is cheaper than the next and can kill.
Score every paired comparison with:

```bash
python scripts/paired_bootstrap.py results.csv --arm-a new --arm-b baseline --cluster task
```

The CSV needs columns `cluster,item,seed,arm,success`. See
[references/statistics.md](references/statistics.md) for sequential stopping and
sample sizes.

**Step 7. Validate the ledger before reporting.**

```bash
python scripts/check_ledger.py LEDGER.md
```

It fails on rows missing a kill line, a verdict, or with a verdict that does not match
PASS/FAIL/pending. Fix and re-run until it passes.

## Bars for "major" claims

When the goal is a step change rather than a few points, write the bar as a fraction
of a measured gap, not an absolute delta: for example "closes at least half the gap
between familiar and unseen conditions" or "equal success at a tenth of the data or
compute", and require it on at least two tasks. Smaller wins are logged as stepping
stones.

## Delegating to subagents

Subagents start without your context. Every brief for an experiment agent includes:
the files to read, the exact claim and kill line (or the instruction to write them
first), which test sets it may claim, the compute rules from
[references/compute.md](references/compute.md) quoted in full, any user approvals
quoted verbatim, and a final-reply word limit with the numbers you need back. When an
agent dies mid-run (rate limit, crash), hand its saved state to a new agent with the
instruction to inspect running jobs before starting anything.

## Generating bets

When the obvious levers are exhausted, read
[references/generating-bets.md](references/generating-bets.md): how past
breakthroughs were found and how to turn each discovery move into a cheap kill test.

## Reporting

Report each result in this order: verdict against the pre-written line, the number
with its CI, the mechanism, cost, and what it changes about the next bet. Say "dead"
when a bet fails; do not rescue it with post-hoc subsets.
