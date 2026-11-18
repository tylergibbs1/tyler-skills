# Running ML Experiments

A skill for running ML research as a loop of **pre-registered kill tests** that agents can't fool themselves with.

It was distilled from a multi-week agent-run world-model research loop. In that loop, these produced wins that later vanished:
- near-duplicate "held-out" sets
- baselines weaker than the published method
- single-seed noise
- pass lines chosen after the fact

It also covers rented GPUs that kept billing after agents died.

## What it does

1. **Ceiling first:** an oracle swap shows what a perfect version of the part could buy, before building anything.
2. **Kill line first:** each stage gets a ledger row with the bar, written before any number exists.
3. **Unseen data, proven:** `scripts/near_duplicates.py` checks how close test items sit to training. A test-set registry stops sets from being reused.
4. **Screen, then gate, then fresh test:** each stage is cheaper than the next and can kill the bet. The fresh test includes the published method as an arm.
5. **Paired, clustered statistics:** `scripts/paired_bootstrap.py` gives the delta, the CI and wins/losses. Sequential stopping cuts compute.
6. **Ledger validation:** `scripts/check_ledger.py` fails on deciding rows with no kill line, or with leftover placeholders.
7. **Compute guardrails:** check the price before creating a pod, keep a balance floor, train on GPU only, tear down and confirm, and hand off safely when an agent dies.
8. **Generating bets:** the discovery moves behind past breakthroughs, each mapped to a cheap kill test.

## Layout

- `SKILL.md`: the gotchas, the checklist and when to load each reference
- `references/`: the ledger and registry formats, statistics, compute rules, generating bets
- `scripts/`: three small CLI tools. `near_duplicates.py` needs numpy; the others use only the standard library.
- `evals/evals.json`: four scenarios, including one where the skill should stay out of the way
