#!/usr/bin/env python3
"""Write the entry line for make.fun's One Line, Zero Use sprint.

The line names a hilariously useless superpower: the power to stop time,
but only for three seconds, and only while blinking. Written
deterministically to /output/entry.txt.
"""

import os

LINE = "I can stop time, but only for three seconds, and only while I'm blinking."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
