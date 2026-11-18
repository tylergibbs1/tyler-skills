# Statistics for paired kill tests

## Design

- **Pair everything.** All arms run on the same items, the same episode seeds and the
  same planner/sampling seeds, ideally in one process. Report per-item wins and losses
  (net = wins − losses) next to the delta.
- **Cluster by the repeating unit.** Items drawn from the same task, source
  demonstration or user are not independent. Resample clusters, not rows.
- **Two seeds minimum** for anything stochastic. Report each seed and the pool.
- **Loss cap.** A large mean gain with many per-item losses is fragile. Put a cap on
  losses per seed in the kill line.

## Sample size

For a binary success metric near 50%, a paired test with moderate correlation
between arms needs roughly:

| Effect to detect (points) | Pairs, about |
|---|---|
| 10 | 150-250 |
| 5 | 500-800 |
| 3 | 1,500-2,000 |

If the budget cannot reach the size for the effect you claim, raise the bar or say
the test can only detect larger effects.

## Sequential stopping

To save compute, pre-register a group-sequential design: 3-4 equally spaced looks,
O'Brien-Fleming alpha spending, and an optional non-binding futility bound. Write the
look schedule in the ledger row before the run. Clear wins and clear nulls typically
stop at look 2 and save about half the episodes. Never add looks after the fact.

## Reading results

- The CI is the result; the point estimate is a summary.
- "CI includes 0" is not "no effect"; say what size of effect is excluded.
- A screen or proxy is only trusted after it has predicted past gate results (report
  its correlation and typical error against gates).
- When a pass rests on one set, it is a candidate. Confirmation on a second unseen set
  with a combined estimate makes it a result.
