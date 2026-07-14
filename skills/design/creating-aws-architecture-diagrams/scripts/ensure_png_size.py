#!/usr/bin/env python3
"""Resize and letterbox a PNG to exact dimensions without distorting content."""

from __future__ import annotations

import argparse
from pathlib import Path

try:
    from PIL import Image, ImageColor, ImageOps
except ImportError as exc:
    raise SystemExit("Pillow is required: python -m pip install Pillow") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Resize a PNG to fit exact dimensions and pad the remainder."
    )
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--width", type=int, default=3840)
    parser.add_argument("--height", type=int, default=2160)
    parser.add_argument("--background", default="#ffffff")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.width <= 0 or args.height <= 0:
        raise SystemExit("width and height must be positive integers")
    if not args.input.is_file():
        raise SystemExit(f"input PNG not found: {args.input}")

    try:
        background = ImageColor.getrgb(args.background)
    except ValueError as exc:
        raise SystemExit(f"invalid background color: {args.background}") from exc

    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.output.with_suffix(args.output.suffix + ".tmp")

    with Image.open(args.input) as source:
        if source.format != "PNG":
            raise SystemExit(f"input must be PNG, received: {source.format or 'unknown'}")
        source = source.convert("RGBA")
        fitted = ImageOps.contain(
            source,
            (args.width, args.height),
            method=Image.Resampling.LANCZOS,
        )
        canvas = Image.new("RGBA", (args.width, args.height), (*background, 255))
        offset = (
            (args.width - fitted.width) // 2,
            (args.height - fitted.height) // 2,
        )
        canvas.alpha_composite(fitted, offset)
        canvas.convert("RGB").save(temporary, format="PNG", optimize=True)

    temporary.replace(args.output)
    print(f"OK {args.output} {args.width}x{args.height}")


if __name__ == "__main__":
    main()
