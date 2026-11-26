"""Entry point for The Internet in One Word bounty.

Writes a single word to /output/entry.txt: the one word that best
describes the whole internet. The word is deterministic, needs no
network access, and is 1 to 30 characters long as the gate requires.

The word is "doomscroll": one verb that names the internet's signature
habit - opening it for one quick look and surfacing an hour later,
tired, informed about nothing, and unable to explain why. It is funny
because everyone recognises themselves in it, true of the whole
internet rather than one app, and surprising next to the obvious
candidates like "endless" or "chaos".
"""
from pathlib import Path

WORD = "doomscroll"

TARGET = Path("/output/entry.txt")


def main():
    text = WORD.strip()
    assert text and " " not in text, "entry must be a single word"
    assert text.islower() and text.isalpha(), "word must be plain lowercase letters"
    assert 1 <= len(text) <= 30, f"word is {len(text)} characters"
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text + "\n", encoding="utf-8")
    print(f"wrote {len(text)} characters to {TARGET}")


if __name__ == "__main__":
    main()
