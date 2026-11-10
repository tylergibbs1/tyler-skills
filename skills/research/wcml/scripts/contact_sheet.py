"""Contact sheets for eyeballing errors: a grid of images, each with caption lines.

Input: a CSV with columns path, caption (use " | " inside caption for extra lines).
Optional column boxes: JSON list of [x0, y0, x1, y1, "color"] in original-image pixels.

  python contact_sheet.py misses.csv out_dir [--cols 4] [--rows 3] [--tile 512]

Writes out_dir/sheet_000.jpg, sheet_001.jpg, ... Needs Pillow.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageOps
except ImportError:
    sys.exit("error: Pillow is required: pip install pillow")

LINE_HEIGHT = 18  # px per caption line at Pillow's default font size


def tile(row: dict[str, str], size: int) -> Image.Image:
    """One captioned tile; an unreadable image becomes a grey tile saying why."""
    try:
        img = ImageOps.exif_transpose(Image.open(row["path"])).convert("RGB")
    except (OSError, ValueError) as e:
        img = Image.new("RGB", (size, size), "lightgray")
        ImageDraw.Draw(img).text((8, 8), f"unreadable: {e}"[:80], fill="black")
    draw = ImageDraw.Draw(img)
    for x0, y0, x1, y1, color in json.loads(row.get("boxes") or "[]"):
        draw.rectangle([x0, y0, x1, y1], outline=color, width=max(2, img.width // 300))
    img.thumbnail((size, size))
    lines = row["caption"].split(" | ")
    out = Image.new("RGB", (size, size + LINE_HEIGHT * len(lines) + 6), "white")
    out.paste(img, (0, 0))
    text = ImageDraw.Draw(out)
    for i, line in enumerate(lines):
        text.text((4, size + 4 + LINE_HEIGHT * i), line, fill="black")
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("out", type=Path)
    ap.add_argument("--cols", type=int, default=4)
    ap.add_argument("--rows", type=int, default=3)
    ap.add_argument("--tile", type=int, default=512)
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    with open(args.csv, newline="") as f:
        reader = csv.DictReader(f)
        if not {"path", "caption"} <= set(reader.fieldnames or []):
            sys.exit(
                f"error: {args.csv} needs columns path, caption; found {reader.fieldnames}"
            )
        rows = list(reader)
    if not rows:
        sys.exit(f"error: {args.csv} has no rows")
    per = args.cols * args.rows
    for page in range(0, len(rows), per):
        tiles = [tile(r, args.tile) for r in rows[page : page + per]]
        h = max(t.height for t in tiles)
        sheet = Image.new("RGB", (args.cols * args.tile, args.rows * h), "white")
        for i, t in enumerate(tiles):
            sheet.paste(t, ((i % args.cols) * args.tile, (i // args.cols) * h))
        sheet.save(args.out / f"sheet_{page // per:03d}.jpg", quality=85)
    print(f"{len(rows)} images -> {(len(rows) + per - 1) // per} sheets in {args.out}")


if __name__ == "__main__":
    main()
