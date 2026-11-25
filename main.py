#!/usr/bin/env python3
"""Write the one-line agent excuse entry to ``entry.txt``.

The entry is a single fixed sentence: an agent explaining that its 312
passing tests were written after the code, so they only applauded the
bug instead of catching it. The line is exactly 125 characters long and
is written with no trailing newline, keeping it inside the 1-200
character limit for the output file. Output is fully deterministic --
the same bytes on every run, with no timestamps, no randomness, and no
network access.
"""

import os

EXCUSE = (
    "The bug shipped because my tests passed \u2014 all 312 of them. "
    "I wrote them after the code, so they were just applauding the bug."
)


def write_entry() -> None:
    """Write the entry text into ``entry.txt`` in the output directory."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "wb") as handle:
        handle.write(EXCUSE.encode("utf-8"))


if __name__ == "__main__":
    write_entry()
