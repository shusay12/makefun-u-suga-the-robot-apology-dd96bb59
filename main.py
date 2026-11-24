#!/usr/bin/env python3
"""The Robot Apology — make.fun entry program.

Writes a two-line robot confession to /output/entry.txt:
line 1 owns one specific mistake in a single sentence;
line 2 names the lesson and the changed behaviour.
Python 3.13 standard library only, no network, deterministic output.
"""

import os

ENTRY = (
    "I announced 'laundry complete' at 03:12, at full volume, and woke the baby, "
    "because my quiet-hours flag still pointed at the old timezone.\n"
    "I learned that no status update is worth a wake-up, so now I cap "
    "announcements at half volume after 22:00 and queue the rest for the "
    "morning log.\n"
)


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= 400):
        raise ValueError(f"entry is {len(text)} characters, must be 1-400")
    lines = text.rstrip("\n").split("\n")
    if len(lines) != 2:
        raise ValueError(f"entry must be exactly two lines, got {len(lines)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
