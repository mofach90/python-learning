from momolang.lexer import Lexer
from momolang.parser import Parser
from momolang.interpreter import Interpreter


def test_interpreter_prints_string(capsys):
    source = 'print("Hello world");'

    tokens = Lexer(source).tokenize()
    program = Parser(tokens).parse()

    Interpreter().run(program)

    captured = capsys.readouterr()
    assert captured.out == "Hello world\n"
