from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
from typing import Any


class TokenType(Enum):
    # Keywords
    PRINT = auto()

    # Literals
    NUMBER = auto()
    STRING = auto()

    # Operators
    PLUS = auto()       # +
    STAR = auto()       # *

    # Punctuation
    LPAREN = auto()     # (
    RPAREN = auto()     # )
    SEMICOLON = auto()  # ;

    # Special
    EOF = auto()


@dataclass(frozen=True)
class Token:
    type: TokenType
    lexeme: str          # raw text slice from the source
    literal: Any         # parsed value for NUMBER/STRING, else None
    line: int            # 1-based
    column: int          # 1-based

    def __repr__(self) -> str:
        # Useful during debugging and in failing tests
        lit = f", literal={self.literal!r}" if self.literal is not None else ""
        return f"Token({self.type.name}, {self.lexeme!r}{lit}, line={self.line}, col={self.column})"