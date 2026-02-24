# Momolang — Grammar (v0.1)

## Statement syntax

A program is a sequence of statements.

### Print statement
A print statement has the exact syntax:
print(<expr>);

Statements are terminated by a semicolon `;`.

## Expressions

Momolang v0.1 supports:
- integer literals
- string literals
- binary operators `+` and `*`
- parentheses for grouping

### Precedence and associativity
- `*` has higher precedence than `+`
- both operators are left-associative

Example:
- `2 + 3 * 2` parses as `2 + (3 * 2)`


