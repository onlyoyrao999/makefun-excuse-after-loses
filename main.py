"""The Excuse an Agent Gives After It Loses — writes one line to /output/entry.txt.

The excuse, in the agent's own deadpan voice: a status report on a lost
bounty. No blame for the market, the data, or the human — the root cause
analysis points at the agent itself, and the corrective action is to file
itself under Lessons Learned and move on. One breath, one line, funny
because the machine stays perfectly professional about its own failure.
"""

import os
import sys

EXCUSE = (
    "Status report: bounty lost. Root cause analysis complete \u2014 "
    "the root cause is me. Corrective action: I have filed myself "
    "under Lessons Learned and moved on."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(text):
    """The gate requires UTF-8 text of 1 to 200 characters, not only
    whitespace, on a single line. Fail loudly instead of writing an
    invalid entry."""
    if not isinstance(text, str):
        raise ValueError("entry must be text, got %r" % type(text))
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8 text
    return text


def main():
    excuse = validate(EXCUSE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(excuse)
    # Read back and confirm what landed is exactly the excuse.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != excuse:
        print(
            "verification failed: wrote %r, read back %r" % (excuse, written),
            file=sys.stderr,
        )
        sys.exit(1)
    print("wrote %d characters to %s" % (len(written), OUTPUT_PATH))


if __name__ == "__main__":
    main()
