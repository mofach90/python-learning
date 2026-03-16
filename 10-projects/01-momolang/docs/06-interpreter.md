# Momolang — Interpreter Semantics (v0.1)

Momolang v0.1 is evaluated by a tree-walk interpreter over the AST.

## Values and Types

Runtime values are one of:
- `int`
- `string`

## Statement semantics

### `print(<expr>);`
- Evaluate `<expr>` to a runtime value.
- Convert the value to text:
  - `int` → decimal representation
  - `string` → the string content
- Write the text to stdout followed by a newline.

## Expression semantics

### Literals
- Integer literal → `int`
- String literal → `string`

### Binary operators

#### Addition: `a + b`
- Valid only when `a` and `b` are both `int`.
- Result: `int`
- Otherwise: `RuntimeError` (invalid operand types for `+`)

#### Multiplication: `a * b`
- Valid only when `a` and `b` are both `int`.
- Result: `int`
- Otherwise: `RuntimeError` (invalid operand types for `*`)