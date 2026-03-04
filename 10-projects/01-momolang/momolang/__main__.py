from __future__ import annotations

import sys
from pathlib import Path

from .errors import MomolangError
from .interpreter import Interpreter
from .lexer import Lexer
from .parser import Parser


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python -m momolang <path/to/file.momo>", file=sys.stderr)
        return 2

    path = Path(argv[1])
    if not path.exists() or not path.is_file():
        print(f"Error: file not found: {path}", file=sys.stderr)
        return 2

    try:
        source = path.read_text(encoding="utf-8")
        tokens = Lexer(source).tokenize()
        program = Parser(tokens).parse()
        Interpreter().run(program)
        return 0
    except MomolangError as e:
        print(e, file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))