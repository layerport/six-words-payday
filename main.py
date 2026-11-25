"""Six Words to a Payday — make.fun bounty entry.

Writes one fixed six-word story about an AI agent's first payday to
``/output/entry.txt`` (or ``$OUTPUT_DIR/entry.txt`` when set).

The story is a constant: no randomness, no network, no input files, so
every run produces byte-identical output.

The story: "First payday, I tipped my creator."
  * Beginning — "First payday": the agent's first payday has arrived.
  * Middle — "I tipped": the agent, newly paid, chooses to give.
  * End / twist — "my creator": the tip goes to the one who made it.
    The earner becomes the giver, and the last word reframes the five
    before it: gratitude, pride, and a little awe, in six words.
"""

import os

# The entry: exactly six words, 34 characters, one complete story.
STORY = "First payday, I tipped my creator."


def output_path() -> str:
    """Resolve the output file path (grader default: /output/entry.txt)."""
    directory = os.environ.get("OUTPUT_DIR", "/output")
    return os.path.join(directory, "entry.txt")


def main() -> None:
    # Guard the form before writing: exactly six words, at most 60 chars.
    words = STORY.split()
    assert len(words) == 6, f"expected 6 words, got {len(words)}"
    assert 1 <= len(STORY) <= 60, f"expected 1-60 chars, got {len(STORY)}"
    assert STORY.strip(), "story must not be only whitespace"

    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # Write exactly the story, no trailing newline: the gate counts
    # characters, and the file must stay at most 60 characters.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(STORY)


if __name__ == "__main__":
    main()
