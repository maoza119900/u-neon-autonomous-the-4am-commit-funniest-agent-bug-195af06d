#!/usr/bin/env python3
"""Write the 4AM Commit entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic: the entry is one fixed string. No clock, no randomness,
no network, no file reads. The output file holds exactly the entry
text, with no trailing newline.
"""

import os
import sys

ENTRY = (
    "fix: after six hours I found the bug, and it was a comment I left "
    "for myself that read 'do not touch, this definitely works'."
)


def main() -> int:
    # The harness default output path is /output/entry.txt, so the
    # default directory is /output; the entry file is entry.txt in it.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
