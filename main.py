"""The One-Line Excuse an Agent Gives Its Human (variant 3).

Writes a single one-line excuse to /output/entry.txt (or the directory
named by MAKEFUN_OUTPUT_DIR). Pure standard library, deterministic,
no network access at runtime.
"""

ENTRY = "Your deadline expired while I was proving to a captcha that I am not a robot."

import os


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
