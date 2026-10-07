#!/usr/bin/env python3
"""Paste text in, get the same text back with all spaces removed.

Example: "i am going" -> "iamgoing"

Usage:
    python space_remover.py

Paste your text, then press Enter on an empty line (or Ctrl-D / Ctrl-Z+Enter)
to finish. Line breaks are kept; only spaces and tabs are removed.
"""

import sys


def remove_spaces(text: str) -> str:
    return text.replace(" ", "").replace("\t", "")


def main() -> None:
    print("Paste your text, then press Enter on an empty line to finish:\n")
    lines = []
    try:
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
    except EOFError:
        pass

    result = "\n".join(remove_spaces(line) for line in lines)
    print("\n--- Result ---")
    print(result)


if __name__ == "__main__":
    if not sys.stdin.isatty():
        # Also works when piped: echo "i am going" | python space_remover.py
        print(remove_spaces(sys.stdin.read()), end="")
    else:
        main()
