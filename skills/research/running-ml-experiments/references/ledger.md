# Ledger and test-set registry

Two plain-markdown files in the project root. Both are append-only: rows are added and
verdict cells are filled in, but bars and kill lines are never edited after the first
number exists.

## LEDGER.md

One table row per stage of a bet (screen, dev gate, fresh test). `scripts/check_ledger.py`
reads this format.

```markdown
| Date | Stage | Arm | Control | Result | Verdict | Notes |
|---|---|---|---|---|---|---|
| 2026-01-05 | X dev gate: <claim>. Data: <set>, seeds 7 and 8, <n> pairs | <new arm, frozen> | <baseline, same process> | RESULT-PENDING | pending | Written <time>, before any number. **Kill line: delta >= +3 AND task-clustered 95% CI lower > 0 AND losses <= 29 per seed = PASS; any failing = FAIL.** |
```

When the stage runs, replace `RESULT-PENDING` with the numbers (delta, CI, per-seed
counts) and `pending` with `PASS`, `FAIL`, `KILLED`, `NOT KILLED` or `UNCLEAR`, and append the mechanism to Notes. If a
deviation from the row was unavoidable (a broken flag, a crashed shard), write it in
Notes as "Deviation:" and leave the line untouched.

Rules:
- A stage runs only if the stage before it passed, unless the row says otherwise.
- Descriptive extras (side arms, blind controls) get the verdict `Descriptive` and need
  no kill line.
- A row added after seeing data starts with "Post hoc:" and its verdict is `Descriptive`.

## FRESH.md (test-set registry)

```markdown
| Set | Size | Files | Provenance and unseen check | Claimed by | Status |
|---|---|---|---|---|---|
| U1 | 250 | `U1.jsonl` | generator seeds 101000-101399; 0 of 250 within 20 px of training | <bet, stage>, claimed <time> | claimed, run |
| U2 | 250 | `U2.jsonl` | ... | | unclaimed |
```

- Claim a set (fill "Claimed by") before the first episode. Never overwrite another
  bet's claim; take the next unclaimed set.
- Store a hash of each set's files and check it before running.
- "Run" sets are spent for decisions. They can be reused for tuning, labelled as such.
- Generate more sets ahead of demand so bets do not queue on data.
