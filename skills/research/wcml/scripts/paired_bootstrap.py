"""Paired group bootstrap for the accuracy difference between two models.

Input: a CSV with columns group, a_correct, b_correct (one row per scored item; correct is
0/1, or a fraction for multi-label items). Groups are the unit the test set is split by
(person, site, patient, scene). Resampling groups, not items, keeps correlated items together.

  python paired_bootstrap.py scores.csv [--reps 10000] [--seed 0]

Exit code 0 on success, 1 on bad input (the message says what is wrong).

Prints item-level and group-macro accuracy for A and B, B - A, and 95% CIs for both deltas.
"""

from __future__ import annotations

import argparse
import csv
import random
import sys
from collections import defaultdict

REQUIRED = ("group", "a_correct", "b_correct")
# 10k resamples keep the 2.5% / 97.5% percentiles stable to about +-0.1 point.
DEFAULT_REPS = 10_000
CI_LOW, CI_HIGH = 0.025, 0.975  # two-sided 95% interval


def load(path: str) -> dict[str, list[tuple[float, float]]]:
    groups: dict[str, list[tuple[float, float]]] = defaultdict(list)
    try:
        with open(path, newline="") as f:
            reader = csv.DictReader(f)
            missing = [c for c in REQUIRED if c not in (reader.fieldnames or [])]
            if missing:
                sys.exit(
                    f"error: {path} lacks columns {missing}; found {reader.fieldnames}. "
                    f"Need {list(REQUIRED)}."
                )
            for line, row in enumerate(reader, start=2):
                try:
                    groups[row["group"]].append(
                        (float(row["a_correct"]), float(row["b_correct"]))
                    )
                except ValueError:
                    sys.exit(
                        f"error: {path} line {line}: a_correct/b_correct must be numbers in [0, 1], got {row}"
                    )
    except OSError as e:
        sys.exit(f"error: cannot open {path}: {e}")
    if len(groups) < 2:
        sys.exit(
            f"error: {path} has {len(groups)} group(s); a group bootstrap needs at least 2."
        )
    return groups


def deltas(
    groups: dict[str, list[tuple[float, float]]], keys: list[str]
) -> tuple[float, float]:
    """Item-level and group-macro B - A over the given (possibly repeated) groups."""
    sa = sb = n = 0.0
    macro = 0.0
    for k in keys:
        rows = groups[k]
        a = sum(r[0] for r in rows)
        b = sum(r[1] for r in rows)
        sa, sb, n = sa + a, sb + b, n + len(rows)
        macro += (b - a) / len(rows)
    return (sb - sa) / n, macro / len(keys)


def ci(values: list[float]) -> tuple[float, float]:
    v = sorted(values)
    return v[int(CI_LOW * len(v))], v[int(CI_HIGH * len(v)) - 1]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--reps", type=int, default=DEFAULT_REPS)
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()
    groups = load(args.csv)
    keys = sorted(groups)
    rows = [r for k in keys for r in groups[k]]
    acc_a = sum(r[0] for r in rows) / len(rows)
    acc_b = sum(r[1] for r in rows) / len(rows)
    d_item, d_macro = deltas(groups, keys)
    rng = random.Random(args.seed)
    boots = [deltas(groups, [rng.choice(keys) for _ in keys]) for _ in range(args.reps)]
    lo, hi = ci([b[0] for b in boots])
    mlo, mhi = ci([b[1] for b in boots])
    verdict = "" if lo > 0 or hi < 0 else "  (not proven)"
    print(f"items={len(rows)} groups={len(keys)} A={acc_a:.4f} B={acc_b:.4f}")
    print(f"B-A item  ={d_item:+.4f} 95%CI=[{lo:+.4f}, {hi:+.4f}]{verdict}")
    print(f"B-A macro ={d_macro:+.4f} 95%CI=[{mlo:+.4f}, {mhi:+.4f}]")


if __name__ == "__main__":
    main()
