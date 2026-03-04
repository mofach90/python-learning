from __future__ import annotations

from dataclasses import dataclass

from .ast_nodes import LiteralExpr, PrintStmt, Program
from .errors import ParseError
from .tokens import Token, TokenType


@dataclass
class Parser:
    tokens: list[Token]
    current: int = 0

    def parse(self) -> Program:
        statements: list[PrintStmt] = []

        while not self.is_at_end():
            statements.append(self.parse_statement())

        return Program(statements=statements)

    def parse_statement(self) -> PrintStmt:
        if self.check(TokenType.PRINT):
            return self.parse_print_stmt()

        token = self.peek()
        raise ParseError(
            f"Unexpected token {token.type.name}, expected a statement",
            token.line,
            token.column,
        )

    def parse_print_stmt(self) -> PrintStmt:
        self.consume(TokenType.PRINT, "Expected 'print'")
        self.consume(TokenType.LPAREN, "Expected '(' after 'print'")

        string_token = self.consume(TokenType.STRING, "Expected string literal inside print(...)")
        expr = LiteralExpr(value=string_token.literal)

        self.consume(TokenType.RPAREN, "Expected ')' after print expression")
        self.consume(TokenType.SEMICOLON, "Expected ';' after print statement")

        return PrintStmt(expr=expr)

    def is_at_end(self) -> bool:
        return self.peek().type == TokenType.EOF

    def peek(self) -> Token:
        return self.tokens[self.current]

    def advance(self) -> Token:
        token = self.peek()
        if not self.is_at_end():
            self.current += 1
        return token

    def check(self, expected_type: TokenType) -> bool:
        if self.is_at_end():
            return expected_type == TokenType.EOF
        return self.peek().type == expected_type

    def consume(self, expected_type: TokenType, message: str) -> Token:
        if self.check(expected_type):
            return self.advance()

        token = self.peek()
        raise ParseError(message, token.line, token.column)