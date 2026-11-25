#!/usr/bin/env python3
"""Make the AI Judge Laugh — entry program (v2).

Writes one office-life one-liner to /output/entry.txt.
The line is the winner of a 14-candidate Swiss tournament judged
head-to-head by the Caffeine Inference router using the house judge
brief from competition.yaml verbatim (see judge_calls.jsonl).

v2 revision over v1:
- Self-checks the house gate before writing: the text must be
  1-200 characters and not only whitespace, and fails loudly
  (non-zero exit, no file written) instead of writing blindly.
- Resolves the output path through a helper so the ENTRY_OUTPUT
  override used in local testing behaves exactly like the default.
- Prints the written path and character count for the run log.

Deterministic and offline: no network, no secrets, no randomness.
The file is written byte-for-byte as the winning line, no trailing
newline, so its size (93 bytes) is the smallest possible for it.
"""
import os
import sys

ENTRY = "Our open-door policy means the door stays open so the whole floor can hear you being told no."

DEFAULT_OUTPUT = "/output/entry.txt"


def resolve_output_path() -> str:
    """Return the path to write, honouring the ENTRY_OUTPUT override."""
    return os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT)


def check_gate(text: str) -> None:
    """Enforce the house gate: 1-200 chars, not only whitespace."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} chars, gate requires 1-200")
    if not text.strip():
        raise ValueError("entry is only whitespace")


def main() -> int:
    try:
        check_gate(ENTRY)
    except ValueError as exc:
        print(f"gate check failed: {exc}", file=sys.stderr)
        return 1
    out = resolve_output_path()
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {out} ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
