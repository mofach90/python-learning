# Momolang — Parser Strategy (v0.1)

Momolang uses a recursive descent parser. Operator precedence is implemented by parsing expressions in layers.

## Function mapping

Top-level:

- `parse_program()`: parses `statement* EOF` and returns `Program(statements)`
- `parse_statement()`: currently only dispatches to `parse_print_stmt()`
- `parse_print_stmt()`: parses `print "(" expr ")" ";"` and returns `PrintStmt(expr)`

Expressions (precedence):

- `parse_expr()`: entry point, delegates to `parse_add()`
- `parse_add()`: parses `mul ( "+" mul )*`
- `parse_mul()`: parses `primary ( "*" primary )*`
- `parse_primary()`: parses literals and parenthesized expressions:
  - `NUMBER` → `LiteralExpr(int)`
  - `STRING` → `LiteralExpr(str)`
  - `"(" expr ")"` → returns inner expr (or a GroupingExpr if desired)

## Parser helpers

The parser typically uses helpers like:
- `peek()`, `advance()`
- `match(token_types...)`
- `consume(token_type, message)` (raises ParseError)