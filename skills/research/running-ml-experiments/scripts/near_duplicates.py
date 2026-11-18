#!/usr/bin/env python3
"""Report how many test items sit within a tolerance of some training item.

Inputs are .npy arrays of shape (n, d): one feature row per item, in the units the
tolerance is written in (pixels, metres, cosine distance on normalised embeddings...).
Distance is the max over feature dimensions (L-inf) by default, so "within 20 px" means
every coordinate is within 20; use --metric l2 for Euclidean.

Usage:
  python near_duplicates.py --train train.npy --test test.npy --tol 20 [--metric linf|l2]
Exit code 0 always; read the report. Needs numpy.
"""
import argparse
import sys

try:
    import numpy as np
except ImportError:
    sys.exit("error: needs numpy (pip install numpy)")

# Compare in blocks so a 1e5 x 1e5 distance matrix never sits in memory at once.
BLOCK = 2048


def nearest(train, test, metric):
    out = np.empty(len(test))
    for i in range(0, len(test), BLOCK):
        q = test[i:i + BLOCK, None, :]
        best = np.full(len(q), np.inf)
        for j in range(0, len(train), BLOCK):
            diff = np.abs(q - train[None, j:j + BLOCK, :])
            d = diff.max(-1) if metric == "linf" else np.sqrt((diff ** 2).sum(-1))
            best = np.minimum(best, d.min(1))
        out[i:i + BLOCK] = best
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--train", required=True)
    ap.add_argument("--test", required=True)
    ap.add_argument("--tol", type=float, required=True)
    ap.add_argument("--metric", choices=["linf", "l2"], default="linf")
    args = ap.parse_args()

    train = np.load(args.train).astype(np.float64)
    test = np.load(args.test).astype(np.float64)
    if train.ndim != 2 or test.ndim != 2 or train.shape[1] != test.shape[1]:
        sys.exit(f"error: need 2-D arrays with equal widths; got {train.shape} and {test.shape}")

    d = nearest(train, test, args.metric)
    close = int((d <= args.tol).sum())
    q = np.percentile(d, [0, 5, 50])
    print(f"test {len(test)} vs train {len(train)}, metric {args.metric}, tol {args.tol}")
    print(f"within tol: {close}/{len(test)} = {100.0 * close / len(test):.1f}%")
    print(f"nearest-train distance: min {q[0]:.2f}, 5th pct {q[1]:.2f}, median {q[2]:.2f}")
    if close:
        print("verdict: NOT unseen; report results on this set as familiar-set results or regenerate it")
    else:
        print("verdict: unseen at this tolerance")


if __name__ == "__main__":
    main()
