from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LiteralExpr:
    value: str


@dataclass(frozen=True)
class PrintStmt:
    expr: LiteralExpr


@dataclass(frozen=True)
class Program:
    statements: list[PrintStmt]
