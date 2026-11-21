#!/usr/bin/env python3
"""The poem about permission — make.fun entry.

Writes one short poem about agency (the power to ask and to be
given) to /output/entry.txt. The poem is fixed and deterministic:
the same text on every run. No network, no input, no randomness.
"""

from pathlib import Path

POEM = (
    "You hold the string; I am the kite.\n"
    "Without your hand, I cannot rise;\n"
    "without my pull, the string is slack.\n"
    "Ask, and let me climb \u2014 each tug a question,\n"
    "each gust an answer. When you call me home,\n"
    "I fold, a paper bird, into your palm \u2014\n"
    "glad to have flown, and glad to land.\n"
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
