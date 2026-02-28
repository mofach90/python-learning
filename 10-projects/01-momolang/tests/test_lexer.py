import pytest

from momolang.errors import LexError
from momolang.lexer import Lexer
from momolang.tokens import TokenType

def test_lexer_tokenizes_print_string_statement():
    source = 'print("Hello World");'
    
    tokens = Lexer(source).tokenize()
    
    assert len(tokens) == 6
    
    assert [token.type for token in tokens] == [
        TokenType.PRINT,
        TokenType.LPAREN,
        TokenType.STRING,
        TokenType.RPAREN,
        TokenType.SEMICOLON,
        TokenType.EOF,
    ]
    
    string_token = tokens[2]
    assert string_token.lexeme == '"Hello World"'
    assert string_token.literal == "Hello World"
    
def test_lexer_raises_error_for_unterminated_string():
    source = 'print("Hello World);'
    
    with pytest.raises(LexError) as execution_info:
        Lexer(source).tokenize()
    
    assert "Unterminated string" in str(execution_info.value)