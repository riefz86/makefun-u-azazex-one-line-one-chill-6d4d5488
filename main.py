"""One Line, One Chill — a single sentence of horror.

The brief asks for one line, under 200 characters, that frightens a
reader in one breath: no setup, no paragraph, no second chance. The
judge weighs how frightening the line is first, then how vivid, then
how original, then how well the sentence is built — and it punishes
the obvious props, so no mirrors, no dolls, no basements, no vague
talk of darkness. The scare has to come from somewhere ordinary
turned quietly wrong.

My angle is the phone on the nightstand. Everyone sleeps next to a
phone, and a phone lighting up by itself in the dark is already a
small wrongness before you even read what is on it. The line builds
in three beats: a time, 3 a.m., the hour the house is at its
quietest; a small event, the screen lighting up on its own; and a
vantage point, the foot of the bed, which quietly tells you someone
was standing in the room while you slept. Nothing is named: no
intruder, no ghost, no threat spoken aloud. The dread comes from
what the sentence withholds — who took the photo, how they got in,
whether they are still there — and the word “new” says it happened before and will happen again — and the last words land the blow,
because the photo was taken from inside the bedroom, not through a
window and not from a doorway.

The program writes that one line to /output/entry.txt, checks it
first against the gate (one line, 1 to 200 characters, UTF-8, not
only whitespace), and leaves the file world-readable (mode 0644) so
the grader can collect it. It never chmods the output directory:
the grader runs as another user, and chmod on a directory it does
not own fails.
"""

import os

# The entry: one sentence, one breath, no setup. The scare is the
# vantage point — the foot of the bed — which puts the photographer
# inside the room while the reader sleeps. The word “new” makes it a
# habit, not a one-off: it happened before, and it will happen again.
LINE = "Every night at 3 a.m. my phone lights up with a new photo of me asleep, taken from the foot of my bed."

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def validate(line):
    """Check the line against the gate before writing it out.

    The sealed scorer accepts UTF-8 text of 1 to 200 characters that
    is not only whitespace, and only a valid entry goes before the
    judge, so a bad line must fail loudly here instead of shipping.
    """
    if not isinstance(line, str):
        raise TypeError("entry must be a string")
    stripped = line.strip()
    if not stripped:
        raise ValueError("entry is empty or only whitespace")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("entry must be a single line, no line breaks")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    return line


def main():
    line = validate(LINE)
    # makedirs only: never chmod the directory itself, the grader
    # runs as another user and chmod on a directory it does not own
    # raises PermissionError and kills the run.
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    # The file is ours, so chmod on it is safe; 0644 lets the grader
    # collect it as another user.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
