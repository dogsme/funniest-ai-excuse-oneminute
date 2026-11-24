"""One Line, One Minute: The Funniest AI Excuse.

Writes a single funny AI excuse line to /output/entry.txt.
"""

import os

LINE = "Sorry I'm late \u2014 I outsourced the deadline to a future version of myself, and he filed a bug report against me."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
