#!/usr/bin/env python3
"""The 3 AM Excuse — a hardware wallet's one-line refusal.

Writes a single line (under 200 characters) to /output/entry.txt:
the excuse a hardware wallet gives for refusing to sign a
transaction at 3 AM. The line is fixed and hand-written, so the
program is deterministic by design: two runs produce
byte-identical output.
"""

import os
import sys

EXCUSE = (
    "This is your seventh 3 AM transfer this month, so I'm staging an "
    "intervention: step one, I keep the keys; step two, you go to bed; "
    "step three, we never speak of the coin you almost bought."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    if not 1 <= len(EXCUSE) <= 200:
        raise SystemExit("excuse must be 1-200 characters, got %d" % len(EXCUSE))
    path = sys.argv[1] if len(sys.argv) > 1 else OUTPUT_PATH
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
