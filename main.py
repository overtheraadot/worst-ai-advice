#!/usr/bin/env python3
"""Worst AI Advice entry — writes one line of the worst possible advice
an AI could give to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Deterministic, no network, no model calls, exit 0.
"""
import os
import sys

LINE = "To speed up your laptop, delete the System32 folder — Windows keeps a spare copy in the cloud, probably."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
