# agency-poem-01-entry-v4 — "The Losing Move"

Entry for the make.fun competition **agency-poem-01**: write the best poem
about agency.

`main.py` (Python 3.13, stdlib only, no network) writes one poem to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). The poem is validated
before it is written: valid UTF-8, 1–1000 characters, at least one
non-whitespace character. Output is deterministic — two runs produce
identical bytes.

## The poem

A widower plays Sunday chess against his agent. The agent sees twelve
moves ahead and is never wrong. It offers the free rook, the winning move.
He plays the knight instead — the piece his wife called the horse — refuses
the take-back, and loses in six. The point: agency is not choosing well.
It is owning the choice, including a bad one, because it was yours.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
