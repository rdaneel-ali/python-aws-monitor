#!/usr/bin/env python3
import re
import sys
from pathlib import Path

ALLOWED_ACTIONS = {
    "Add",
    "Update",
    "Fix",
    "Refactor",
    "Remove",
    "Rename",
    "Deprecate",
    "Test",
    "Document",
    "Format",
    "Optimize",
    "Configure",
    "Revert",
    "Merge",
    "Chore",
}

PATTERN = re.compile(rf"^({'|'.join(sorted(ALLOWED_ACTIONS))}): .{{1,72}}$")


def main() -> int:
    if len(sys.argv) < 2:
        print("ERROR: commit message file path not provided.")
        return 1
    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: commit message file not found: {path}")
        return 1

    content = path.read_text(encoding="utf-8").strip()
    if not content:
        print("ERROR: empty commit message.")
        return 1

    first_line = content.splitlines()[0]
    if not PATTERN.match(first_line):
        print("ERROR: invalid commit message first line.")
        print("Required: Action: description (≤ 72 chars).")
        print("Allowed Actions: " + ", ".join(sorted(ALLOWED_ACTIONS)))
        print(f"Got: {first_line!r}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
