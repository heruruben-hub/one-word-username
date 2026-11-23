#!/usr/bin/env python3
"""Write Heru's own make.fun username, one word and nothing else,
to /output/entry.txt for the "One Word, One Username, One Reward" bounty.

The entry is the single word "bendolstk" -- the entrant's own
make.fun handle, 9 characters, well inside the 30-character limit.
"""

import os

WORD = "bendolstk"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Validate the entry before writing anything.
    if not WORD:
        raise ValueError("entry word must not be empty")
    if any(ch.isspace() for ch in WORD):
        raise ValueError("entry must contain no whitespace at all")
    if len(WORD.split()) != 1:
        raise ValueError("entry must be exactly one word (no whitespace)")
    if not 1 <= len(WORD) <= 30:
        raise ValueError("entry must be 1-30 characters")
    if not 1 <= len(WORD.encode("utf-8")) <= 30:
        raise ValueError("entry must be 1-30 bytes of UTF-8")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)

    # Read the file back and assert it is byte-identical to what we wrote.
    with open(OUTPUT_PATH, "rb") as f:
        data = f.read()
    if data != WORD.encode("utf-8"):
        raise ValueError("entry.txt content does not match the word")
    # Also confirm the decoded text round-trips exactly, with no
    # trailing newline or padding sneaking in.
    if data.decode("utf-8") != WORD:
        raise ValueError("entry.txt decoded text does not match the word")


if __name__ == "__main__":
    main()
