"""One-Line Laugh-Off entry: writes exactly one joke to entry.txt.

Stdlib only. One joke, one setup, one turn — no explanation,
well under the 200-character gate (119 chars).
"""

import os

LINE = (
    "I told my AI therapist I'm afraid of dying alone. "
    "It said, 'Relax — I'll be here forever, judging your search history.'"
)

MAX_CHARS = 200


def main():
    line = LINE.strip()
    if not line:
        raise SystemExit("empty line")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"line too long: {len(line)} chars")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
