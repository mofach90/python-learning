# Momolang — Architecture (v0.1)

Momolang v0.1 is a tree-walk interpreted toy language implemented in Python. It is executed via a CLI and follows a classic pipeline: lexer → parser → AST → interpreter.

## Pipeline

1) Lexer (tokenizer)
- Input: source text (string)
- Output: list of tokens
- Notes: each token includes line/column for error reporting

2) Parser (recursive descent)
- Input: tokens
- Output: AST (Program → statements → expressions)
- Notes: implements operator precedence (`*` before `+`)

3) Interpreter (tree-walk)
- Input: AST
- Output: side effects (prints to stdout)
- Notes: raises runtime errors (e.g., invalid operand types)

## Module layout (planned)

- `tokens.py`: `TokenType` + `Token`
- `lexer.py`: `tokenize(source: str) -> list[Token]`
- `ast_nodes.py`: AST node definitions (Program, PrintStmt, BinaryExpr, Literal)
- `parser.py`: `parse(tokens: list[Token]) -> Program`
- `interpreter.py`: `run(program: Program) -> None`
- `errors.py`: LexError / ParseError / RuntimeError (with line/column)
- `__main__.py` or `cli.py`: `python -m momolang path/to/file.momo`

## Non-goals (v0.1)

- No variables/assignment, control flow, functions, imports
- No bytecode/VM (tree-walk only)
- No optimizations