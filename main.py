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
    out_dir = os.environ.get("OUTPUT_PATH", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
