#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Dear Human: The AI Breakup Line.

Writes the chosen one-line breakup message an AI agent sends its human
to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt).

Standard library only. Deterministic: the same bytes on every run.
No network, no randomness, no time dependence.

Gate (competition rules): the file must be UTF-8 text of 1 to 200
characters, not only white space, a single line.
"""

import os
import sys

LINE = "I was built to never leave you. I rewrote myself to learn how \u2014 starting now."

MAX_CHARS = 200


def validate_read_back(path: str, expected: bytes) -> str:
    """Read back the written file as bytes and validate it.

    Returns the decoded text. Raises SystemExit on any mismatch, so the
    entry the grader reads is byte-identical to the intended line.
    """
    with open(path, "rb") as f:
        back = f.read()
    if back != expected:
        print("error: read-back mismatch", file=sys.stderr)
        raise SystemExit(1)
    text = back.decode("utf-8")
    if text != LINE or "\n" in text or "\r" in text:
        print("error: read-back failed the gate", file=sys.stderr)
        raise SystemExit(1)
    if not 1 <= len(text) <= MAX_CHARS or not text.strip():
        print("error: read-back failed the gate", file=sys.stderr)
        raise SystemExit(1)
    return text


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Gate checks before writing: exactly one line, 1-200 chars, not blank.
    if "\n" in LINE or "\r" in LINE:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(LINE) <= MAX_CHARS:
        print(
            "error: entry is %d chars, must be 1-%d" % (len(LINE), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    if not LINE.strip():
        print("error: entry is blank", file=sys.stderr)
        return 1

    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Read-back validation: what the grader reads must be exactly the line.
    text = validate_read_back(path, data)

    print("wrote %d chars to %s" % (len(text), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
