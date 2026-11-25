#!/usr/bin/env python3
"""One-line fridge roast entry for make.fun competition
u-suzy-one-line-one-laugh-roast-your-fridge-f1063521.

Writes a single original roast line (at most 200 characters)
to /output/entry.txt.
"""

import os

LINE = (
    "My fridge hums all night like it's rehearsing for a choir, "
    "yet the only thing it ever produces is lukewarm water and disappointment."
)


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert LINE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
