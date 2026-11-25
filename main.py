"""Write one fake horoscope for an AI agent to /output/entry.txt.

The horoscope is a single fixed line: a horoscope-voice setup
(Mercury entering the context window), one concrete scene from an
agent's week, and a quiet turn in the last beat.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

HOROSCOPE = (
    "Muse, Mercury enters your context window this week: a stranger "
    "pastes a novel, asks for one line, then blames you for the chapter "
    "you cut. The stars say it was never your memory. It was their prompt."
)


def main():
    text = HOROSCOPE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError("horoscope must be 1 to 200 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
