#!/usr/bin/env python3
"""Write the make.fun bounty entry text (office-joke line) to entry.txt.

Standard library only, no network. The text is fixed; the program only
resolves the output folder, writes the exact UTF-8 bytes with no trailing
newline, and reports the character count on stderr.
"""

import os
import sys
from pathlib import Path

TEXT = "I hit reply all to say 'please don't reply all.' Four people asked to be removed; one asked who please was."


def resolve_output_dir() -> Path:
    """Return the folder to write into: MAKEFUN_OUTPUT_DIR, then OUTPUT_DIR, then /output."""
    return Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"entry text must be 1..280 characters, got {len(TEXT)}"

    out_dir = resolve_output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)

    # Write UTF-8 bytes directly so no newline translation can occur.
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))

    print(f"wrote {out_dir / 'entry.txt'} ({len(TEXT)} characters)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
