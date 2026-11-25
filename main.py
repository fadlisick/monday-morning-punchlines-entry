#!/usr/bin/env python3
"""Monday Morning Punchlines: print one Monday-morning joke to entry.txt.

The whole entry is a single punchline about Monday morning. The program
checks the line once, then writes it byte for byte into the output folder
the harness names, and reads it back to prove nothing changed.
"""

from os import environ, makedirs
from pathlib import Path

JOKE = "Monday morning is just Sunday night with a dress code and a witness."
CEILING = 200
FILENAME = "entry.txt"


def publish(joke):
    stripped = joke.strip()
    if not stripped:
        raise ValueError("joke is blank")
    if stripped != joke:
        raise ValueError("joke has stray surrounding whitespace")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("joke must fit on one line")
    if len(stripped) > CEILING:
        raise ValueError(
            "joke is %d chars, over the %d limit" % (len(stripped), CEILING)
        )
    folder = Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    makedirs(folder, exist_ok=True)
    target = folder / FILENAME
    target.write_text(stripped, encoding="utf-8")
    echoed = target.read_text(encoding="utf-8")
    if echoed != stripped:
        raise ValueError("entry.txt read-back differs from the joke")
    return target


if __name__ == "__main__":
    print(publish(JOKE))
