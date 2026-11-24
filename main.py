"""One Line, One Chill — entry program.

Writes a single original horror line (one sentence, under 200
characters) to /output/entry.txt for the make.fun judge.
"""

import os

ENTRY = "The dentist found a second set of teeth growing behind mine, and they were already chewing."


def main() -> None:
    # Self-check the gate: one line, 1-200 characters, not only whitespace.
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
