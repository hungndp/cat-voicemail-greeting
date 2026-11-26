"""Funniest Cat Voicemail Greeting — make.fun entry.

Writes one voicemail greeting, as recorded by a cat named Biscuit, to
/output/entry.txt (or $ENTRY_OUTPUT). The line is 114 characters, under
the competition's 120-character cap.

The greeting is built from two parts: a setup that establishes the cat's
character (a busy, unbothered housecat who knocks things off tables) and
a punch that lands the twist last — the cat only calls back for tuna.
"""

import os

# Setup: the voicemail frame plus the one incident (knocking the mug).
SETUP = (
    "Hi, you've reached Biscuit. I'm napping or knocking your mug "
    "off the table. Leave a message."
)

# Punch: the twist word is "callback" — the cat runs a tuna-only
# callback policy. Deadpan, first person, the cat's own voice.
PUNCH = "Tuna gets a callback."


MAX_CHARS = 120


def build_line():
    """Join setup and punch into the single voicemail greeting."""
    return SETUP + " " + PUNCH


def guard(line):
    """The gate: UTF-8 text, 1 to 120 characters, not only whitespace."""
    if not line or not line.strip():
        raise ValueError("entry is empty")
    if len(line) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the %d cap" % (len(line), MAX_CHARS))
    return line


def main():
    line = guard(build_line())
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
