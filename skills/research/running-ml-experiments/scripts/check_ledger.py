#!/usr/bin/env python3
"""Validate a LEDGER.md experiment table (format in references/ledger.md).

Checks every data row of every markdown table whose header has a 'Verdict' column.
The Verdict cell must start (bold allowed) with one of:
  pending | PASS | FAIL | KILL | KILLED | NOT KILLED | UNCLEAR   -> a deciding row
  Descriptive                                                     -> reported, not deciding
Deciding rows must state a kill line ("Kill line", "Kill if" or "Pass line") in the row, and once decided must not
still hold a RESULT-PENDING placeholder. Rows marked "Post hoc:" must be Descriptive.

Usage: python check_ledger.py LEDGER.md   (exit 1 and a list of problems if any)
"""
import re
import sys

KILL_LINE = re.compile(r"kill line|kill if|pass line", re.IGNORECASE)
VERDICT = re.compile(r"^[*\s]*(pending|PASS|FAIL|NOT KILLED|KILLED|KILL|UNCLEAR|descriptive)\b", re.IGNORECASE)


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def check(path):
    problems = []
    verdict_col = None
    with open(path) as f:
        lines = f.read().splitlines()
    for n, line in enumerate(lines, 1):
        if not line.lstrip().startswith("|"):
            verdict_col = None
            continue
        row = cells(line)
        if verdict_col is None:
            low = [c.lower() for c in row]
            verdict_col = low.index("verdict") if "verdict" in low else -1
            continue
        if verdict_col < 0 or set(line.replace("|", "").strip()) <= set("-: "):
            continue
        text = " ".join(row)
        verdict = row[verdict_col] if verdict_col < len(row) else ""
        m = VERDICT.match(verdict)
        kind = m.group(1).upper() if m else None
        if not m:
            problems.append(f"line {n}: verdict {verdict[:50]!r} does not start with pending, PASS, FAIL, KILL(ED), NOT KILLED, UNCLEAR or Descriptive")
            continue
        if "post hoc:" in text.lower() and kind != "DESCRIPTIVE":
            problems.append(f"line {n}: post-hoc row must be Descriptive, not {kind}")
            continue
        if kind == "DESCRIPTIVE":
            continue
        if not KILL_LINE.search(text):
            problems.append(f"line {n}: deciding row ({kind}) has no kill line written in it")
        if kind != "PENDING" and "RESULT-PENDING" in text:
            problems.append(f"line {n}: verdict {kind} filled but result still RESULT-PENDING")
    return problems


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    problems = check(sys.argv[1])
    if problems:
        print("\n".join(problems))
        print(f"{len(problems)} problem(s)")
        sys.exit(1)
    print("ledger OK")


if __name__ == "__main__":
    main()
