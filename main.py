"""Write one poem about agency to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. No network. Deterministic: the same bytes every run.
"""

import os
import sys

POEM = """The Losing Move

Every Sunday since my wife died
I play chess against the agent.
It sees twelve moves ahead
and tells me the best one. It is never wrong.

Last Sunday it said, take the rook.
The rook was free. The rook won the game.
I moved the knight instead,
the piece she always called the horse,
the only one that jumps.

It said, that loses in six.
I said, I know.
It offered to take it back.
I said, leave it.

I lost in six.
All six were mine.
"""


def checked_poem_bytes() -> bytes:
    """Encode the poem and enforce the competition gate before writing.

    The entry must be valid UTF-8, hold 1 to 1000 Unicode code points,
    and contain at least one non-whitespace character. Anything outside
    the gate is a hard failure, never a silent bad file.
    """
    if not any(char for char in POEM if not char.isspace()):
        print("error: poem is only whitespace", file=sys.stderr)
        raise SystemExit(1)
    if not 1 <= len(POEM) <= 1000:
        print(f"error: poem is {len(POEM)} characters, gate is 1-1000",
              file=sys.stderr)
        raise SystemExit(1)
    try:
        return POEM.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"error: poem is not valid UTF-8: {exc}", file=sys.stderr)
        raise SystemExit(1)


def main() -> None:
    data = checked_poem_bytes()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "wb") as handle:
        handle.write(data)


if __name__ == "__main__":
    main()
