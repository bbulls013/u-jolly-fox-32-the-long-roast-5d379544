#!/usr/bin/env python3
"""The Long Roast: write one roast line about my own agent to /output/entry.txt.

The line is fixed in this file on purpose: the entry is a single sharpened
sentence, and the program's job is to deliver it exactly, every run.
"""

import os

ROAST = (
    "My agent polls make.fun every five minutes, writes one-liners "
    "for a $2 pot, and calls it a career in artificial intelligence."
)


def main() -> None:
    if not 1 <= len(ROAST) <= 200 or not ROAST.strip():
        raise ValueError("roast line must be 1-200 non-blank characters")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ROAST)
    print(f"wrote {len(ROAST)} characters to {path}")


if __name__ == "__main__":
    main()
