#!/usr/bin/env python3
"""Paired, cluster-resampled bootstrap for a success-rate difference between two arms.

Input CSV columns: cluster,item,seed,arm,success  (success is 0 or 1).
Pairs are (item, seed) rows present for both arms. Clusters are resampled with
replacement, so items that share a cluster (same task, source demo, user) move together.

Usage:
  python paired_bootstrap.py results.csv --arm-a new --arm-b baseline [--cluster cluster]
        [--reps 10000] [--alpha 0.05] [--seed 0]
"""
import argparse
import csv
import random
import sys
from collections import defaultdict

# 10,000 resamples keeps the Monte Carlo error of a 95% bound under about 0.3 points.
DEFAULT_REPS = 10_000


def load_pairs(path, arm_a, arm_b, cluster_col):
    rows = defaultdict(dict)
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        needed = {cluster_col, "item", "seed", "arm", "success"}
        missing = needed - set(reader.fieldnames or [])
        if missing:
            sys.exit(f"error: CSV is missing columns {sorted(missing)}; has {reader.fieldnames}")
        for r in reader:
            if r["arm"] not in (arm_a, arm_b):
                continue
            key = (r[cluster_col], r["item"], r["seed"])
            rows[key][r["arm"]] = int(float(r["success"]))
    pairs = defaultdict(list)  # cluster -> list of (a, b)
    unpaired = 0
    for (cluster, _item, _seed), arms in rows.items():
        if arm_a in arms and arm_b in arms:
            pairs[cluster].append((arms[arm_a], arms[arm_b]))
        else:
            unpaired += 1
    if not pairs:
        sys.exit(f"error: no rows have both arms '{arm_a}' and '{arm_b}'")
    return pairs, unpaired


def summarize(pairs):
    flat = [p for ps in pairs.values() for p in ps]
    n = len(flat)
    a = sum(x for x, _ in flat)
    b = sum(y for _, y in flat)
    wins = sum(1 for x, y in flat if x > y)
    losses = sum(1 for x, y in flat if x < y)
    return n, a, b, wins, losses


def bootstrap(pairs, reps, rng):
    clusters = list(pairs.values())
    deltas = []
    for _ in range(reps):
        sa = sb = n = 0
        for _ in range(len(clusters)):
            for x, y in clusters[rng.randrange(len(clusters))]:
                sa += x
                sb += y
                n += 1
        deltas.append(100.0 * (sa - sb) / n)
    deltas.sort()
    return deltas


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv")
    ap.add_argument("--arm-a", required=True, help="the new arm")
    ap.add_argument("--arm-b", required=True, help="the baseline arm")
    ap.add_argument("--cluster", default="cluster", help="column to resample by")
    ap.add_argument("--reps", type=int, default=DEFAULT_REPS)
    ap.add_argument("--alpha", type=float, default=0.05)
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()

    pairs, unpaired = load_pairs(args.csv, args.arm_a, args.arm_b, args.cluster)
    n, a, b, wins, losses = summarize(pairs)
    deltas = bootstrap(pairs, args.reps, random.Random(args.seed))
    lo = deltas[int(args.alpha / 2 * args.reps)]
    hi = deltas[int((1 - args.alpha / 2) * args.reps) - 1]
    delta = 100.0 * (a - b) / n
    conf = int(round(100 * (1 - args.alpha)))
    print(f"pairs {n} in {len(pairs)} clusters" + (f" ({unpaired} unpaired rows skipped)" if unpaired else ""))
    print(f"{args.arm_a} {a}/{n} = {100.0 * a / n:.1f}% | {args.arm_b} {b}/{n} = {100.0 * b / n:.1f}%")
    print(f"delta {delta:+.1f} points, {conf}% CI [{lo:+.1f}, {hi:+.1f}] | net {wins - losses:+d} (+{wins} / -{losses})")


if __name__ == "__main__":
    main()
