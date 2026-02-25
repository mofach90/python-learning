# Momolang — AST (v0.1)

The parser builds an Abstract Syntax Tree (AST). The interpreter evaluates the AST.

## Top-level node

- `Program(statements: list[Stmt])`

## Statements

- `PrintStmt(expr: Expr)`
  - Executes by evaluating `expr` and printing the result to stdout.

## Expressions

- `LiteralExpr(value: int | str)`
  - Represents integer and string literals.

- `BinaryExpr(left: Expr, operator: Token, right: Expr)`
  - Represents `+` and `*` expressions.
  - Stores the operator as a `Token` (not just a string) so runtime errors can report a location.


## Full Example: print(2 + 3 * 4);
The whole thing as a tree of Python objects:

Program(statements=[
    PrintStmt(
        expr=BinaryExpr(
            left=LiteralExpr(2),
            operator=Token(type="PLUS", value="+", line=1),
            right=BinaryExpr(
                left=LiteralExpr(3),
                operator=Token(type="STAR", value="*", line=1),
                right=LiteralExpr(4)
            )
        )
    )
])
```

Notice how `3 * 4` is **nested inside** the right side of `2 + ...`. That nesting is what makes `*` evaluate first — the interpreter goes to the deepest node first and works its way up.

### How the Interpreter Evaluates It

It walks the tree from bottom to top:
```
Step 1: Visit LiteralExpr(2) → returns 2
Step 2: Visit LiteralExpr(3) → returns 3
Step 3: Visit LiteralExpr(4) → returns 4
Step 4: Visit BinaryExpr(3 * 4) → returns 12
Step 5: Visit BinaryExpr(2 + 12) → returns 14
Step 6: Visit PrintStmt → prints 14