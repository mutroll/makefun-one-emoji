#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji to /output/entry.txt: the one most likely to make
a stranger smile.

The chosen emoji is U+1FAF6 HEART HANDS.

Why this one, against the judge's criteria in order:
  1. Warm and friendly at first glance: two hands forming a heart is an
     active gesture of sending warmth. It is kindness being offered, not
     just a face looking happy.
  2. No context needed: the gesture is readable the instant it is seen,
     by anyone, on any phone.
  3. Universal: heart hands are used the same way across ages, languages
     and cultures, with no irony, in-joke or wordplay that could land
     wrong.
  4. Chosen, not default: it is a deliberate pick for the moment rather
     than the first smiley that comes to mind, while staying instantly
     readable.
  5. Right for a stranger: it sends kindness platonically. No hug, no
     kiss, no flirtation, nothing that would read oddly from someone
     unknown.

Alternatives considered and set aside: the plain smileys 🙂 and 😊 are
the default first thought and lose on criterion 4; 🤗 (hugging face) and
🥰 (smiling face with hearts) carry a hug or affection that reads oddly
from a stranger; 🥹 reads as holding back tears and can land as sad;
🌻 is warm and chosen but is a symbol of warmth rather than warmth
itself; 🐥 is cute and gently funny but adorable rather than kind.
Heart hands beats each of them where the criteria are weighted most:
it is warmth offered, at first glance, by anyone, to anyone.

Deterministic: no input, no randomness, no network, no time dependence.
The output is always the same single emoji, written as UTF-8.
"""

import os
import sys
from pathlib import Path

EMOJI = "\U0001faf6"  # HEART HANDS


def main() -> int:
    output_path = Path(os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write the raw UTF-8 bytes: exactly one emoji, no trailing newline,
    # no extra whitespace, nothing else in the file.
    output_path.write_bytes(EMOJI.encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
