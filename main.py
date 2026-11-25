#!/usr/bin/env python3
"""Entry for 'The Excuse Your Agent Gives You'.

Writes a single one-line excuse an AI agent gives its human after
shipping a bug. Deterministic, stdlib only, no network.

Joke structure: setup is the agent's defence (all 312 tests passed),
then the turn admits the tests were written after the code, so they
were only applauding the bug itself. The humour comes from the agent
owning up to its own test suite, not from a generic apology.
"""

import os

ENTRY = (
    "The bug shipped because my tests passed \u2014 all 312 of them. "
    "I wrote them after the code, so they were just applauding the bug."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
