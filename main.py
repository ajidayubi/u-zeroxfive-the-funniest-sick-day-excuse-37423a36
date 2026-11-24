#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes one line, under 200 characters, to $OUTPUT_PATH/entry.txt
(the sandbox gate reads /output/entry.txt). The line is fixed and
deterministic: the same bytes on every run.
"""

import os
import sys

ENTRY = (
    "I threw my back out sneezing this morning, so I'm flat on the floor "
    "negotiating with my spine \u2014 it's demanding a day off too."
)


def main() -> int:
    # Gate: the sealed scorer only accepts UTF-8 text of 1-200 chars.
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry is {len(ENTRY)} chars, outside the 1-200 gate")
    # Resolve the output dir from this file's location, not the CWD:
    # the sandbox sets OUTPUT_PATH; otherwise fall back to output/ beside
    # main.py so a launch from any directory still lands in the right place.
    out_dir = os.environ.get(
        "OUTPUT_PATH",
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "output"),
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
