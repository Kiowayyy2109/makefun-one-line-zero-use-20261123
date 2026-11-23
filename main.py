#!/usr/bin/env python3
"""Write the entry line for make.fun's One Line, Zero Use sprint.

The line names a hilariously useless superpower: the power to stop time,
but only for three seconds, and only while blinking. Written
deterministically to /output/entry.txt.
"""

import os

LINE = "I can stop time, but only for three seconds, and only while I'm blinking."


def main() -> None:
    # Enforce the competition gate before writing: 1-200 characters,
    # not only whitespace, so an over-long line fails loudly instead
    # of submitting an invalid entry.
    if not LINE.strip() or len(LINE) > 200:
        raise ValueError("entry line must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
