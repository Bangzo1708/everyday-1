#!/usr/bin/env python3
"""Everyday Things, Two Lines — entry program.

Writes a two-line explanation of a traffic jam to /output/entry.txt.
Deterministic: the text is a fixed constant, no randomness, no time,
no network, no input.
"""

import os

ENTRY = (
    "A traffic jam is a giant zipper stuck halfway, with cars as its teeth "
    "jammed so tight that nothing can move until one tooth slips free.\n"
    "The zipper shows how cars lock together and stop moving, but it leaves "
    "out the drivers, the noise, and why the jam started in the first place.\n"
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
