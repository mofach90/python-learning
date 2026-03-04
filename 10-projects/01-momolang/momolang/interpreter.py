from __future__ import annotations

from dataclasses import dataclass

from .ast_nodes import LiteralExpr, PrintStmt, Program
from .errors import MomolangRuntimeError


@dataclass
class Interpreter:
    def run(self, program: Program) -> None:
        for stmt in program.statements:
            self.execute(stmt)

    def execute(self, stmt: PrintStmt) -> None:
        value = self.evaluate(stmt.expr)
        print(value)

    def evaluate(self, expr: LiteralExpr):
        return expr.value