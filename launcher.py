"""Run the bundled Mushgame program."""

import sys
from pathlib import Path

from interpreter import run


def main():
    bundle = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
    program = bundle / "main.mylang"
    run(program.read_text(encoding="utf-8"), filename=str(program))


if __name__ == "__main__":
    main()
