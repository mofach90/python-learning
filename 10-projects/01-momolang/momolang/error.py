from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MomolangError(Exception):
    message: str
    line: int
    column: int

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] line {self.line}, column {self.column}: {self.message}"


class LexError(MomolangError):
    pass


class ParseError(MomolangError):
    pass


class MomolangRuntimeError(MomolangError):
    pass