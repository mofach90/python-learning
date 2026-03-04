from momolang.ast_nodes import LiteralExpr, PrintStmt, Program
from momolang.lexer import Lexer
from momolang.parser import Parser


def test_parser_builds_ast_for_print_string_statement():
    source = 'print("Hello world");'

    tokens = Lexer(source).tokenize()
    program = Parser(tokens).parse()

    assert program == Program(
        statements=[
            PrintStmt(
                expr=LiteralExpr(value="Hello world")
            )
        ]
    )