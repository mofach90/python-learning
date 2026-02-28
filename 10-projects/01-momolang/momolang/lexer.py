from __future__ import annotations

from dataclasses import dataclass

from .errors import LexError
from .tokens import Token, TokenType


@dataclass
class Lexer:
    source: str
    current: int = 0     # index into source
    line: int = 1        # 1-based
    column: int = 1      # 1-based

    def tokenize(self) -> list[Token]:
        tokens: list[Token] = []

        while not self.is_at_end():
            c = self.peek()

            # Whitespace (ignored, but updates position)
            if c in (" ", "\t", "\r", "\n"):
                self.advance()
                continue
                
            # Single-character tokens
            if c == "(":
                tokens.append(self.make_simple(TokenType.LPAREN))
                continue
            if c == ")":
                tokens.append(self.make_simple(TokenType.RPAREN))
                continue
            if c == ";":
                tokens.append(self.make_simple(TokenType.SEMICOLON))
                continue
            if c == "+":
                tokens.append(self.make_simple(TokenType.PLUS))
                continue
            if c == "*":
                tokens.append(self.make_simple(TokenType.STAR))
                continue

            # String literal
            if c == '"':
                tokens.append(self.string_token())
                continue

            # Identifier / keyword (v0.1: only 'print' allowed)
            if c.isalpha():
                tokens.append(self.keyword_token())
                continue

            # Number literal
            if c.isdigit():
                tokens.append(self.number_token())
                continue

            # Anything else is invalid
            raise LexError(f"Unexpected character {c!r}", self.line, self.column)

        # EOF token
        tokens.append(Token(TokenType.EOF, "", None, self.line, self.column))
        return tokens

    def is_at_end(self) -> bool:
        return self.current >= len(self.source)

    def peek(self) -> str:
        if self.is_at_end():
            return "\0"
        return self.source[self.current]

    def advance(self) -> str:
        c = self.source[self.current]
        self.current += 1

        if c == "\n":
            self.line += 1
            self.column = 1
        else:
            self.column += 1

        return c

    def make_simple(self, ttype: TokenType) -> Token:
        # token position is where the token starts (current line/col)
        line, col = self.line, self.column
        lexeme = self.advance()
        return Token(ttype, lexeme, None, line, col)

    def string_token(self) -> Token:
        # starting quote
        line, col = self.line, self.column
        self.advance()

        start_index = self.current
        start_line, start_col = self.line, self.column

        while not self.is_at_end() and self.peek() != '"':
            # v0.1: no escapes, but allow newlines? we'll disallow for simplicity
            if self.peek() == "\n":
                raise LexError("Unterminated string (newline encountered)", start_line, start_col)
            self.advance()

        if self.is_at_end():
            raise LexError("Unterminated string (missing closing quote)", start_line, start_col)

        # content inside quotes
        value = self.source[start_index:self.current]

        # closing quote
        self.advance()

        lexeme = f'"{value}"'
        return Token(TokenType.STRING, lexeme, value, line, col)

    def keyword_token(self) -> Token:
        line, col = self.line, self.column
        start = self.current

        while not self.is_at_end() and self.peek().isalpha():
            self.advance()

        text = self.source[start:self.current]
        if text == "print":
            return Token(TokenType.PRINT, text, None, line, col)

        raise LexError(f"Unknown identifier {text!r} (only 'print' is supported in v0.1)", line, col)

    def number_token(self) -> Token:
        line, col = self.line, self.column
        start = self.current

        while not self.is_at_end() and self.peek().isdigit():
            self.advance()

        text = self.source[start:self.current]
        return Token(TokenType.NUMBER, text, int(text), line, col)