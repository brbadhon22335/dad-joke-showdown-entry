"""Dad Joke Showdown entry.

Writes one original dad joke (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

JOKE = (
    "My son asked why the computer went to therapy. "
    "I said, 'It had too many tabs open and couldn't process its feelings.'"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Collapse any accidental line breaks so the entry is always one line.
    text = " ".join(JOKE.split())
    assert 1 <= len(text) <= 200, f"joke is {len(text)} characters"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
