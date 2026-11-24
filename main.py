"""Status Report Comedy Sprint — make.fun entry.

Writes the winning one-line status report to /output/entry.txt:
one line, 1-200 characters, no trailing newline.
"""

import os

TEXT = "This week: 0 errors, 0 warnings, 1 tool that quietly billed us $40 to print 'hello'."


def main():
    # Self-check against the sealed scorer's gate: 1-200 chars, one line.
    if not 1 <= len(TEXT) <= 200 or "\n" in TEXT or not TEXT.strip():
        raise ValueError("entry text must be one line of 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
