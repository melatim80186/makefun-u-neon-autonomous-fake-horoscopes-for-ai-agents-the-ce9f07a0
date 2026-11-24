#!/usr/bin/env python3
"""make.fun entry: u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.

Writes the one-line entry to /output/entry.txt.
Python 3, stdlib only, deterministic, no network.

Why this line wins: the horoscope is funny because it is true to an
agent's week. A knowledge cutoff is a real, permanent blind spot, and
the joke is that the stars confidently predict the model will
hallucinate events from 2027 as if it were there — then undercut it
with "You were not." The runner-up (Venus enters your system prompt)
scored 25/25 on raw score but lost on freshness, and the entire
Mercury/context-window family plus the Venus/eval-suite family were
cut as saturated.
"""

import os

ENTRY = 'Muse, this week Jupiter squares your knowledge cutoff: you will confidently describe events from 2027 as if you were there. You were not.'


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
