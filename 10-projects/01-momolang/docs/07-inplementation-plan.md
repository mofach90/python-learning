# Momolang — Final Build Order (v0.1 Implementation Plan)

## Step 0 — Repo Scaffolding

Create package and placeholders:

- `momolang/` (package)
- `tests/`
- `examples/hello.momo`

---

## Step 1 — Tokens + Lexer (minimal)

Implement:

- `TokenType` enum: `PRINT`, `NUMBER`, `STRING`, `PLUS`, `STAR`, `LPAREN`, `RPAREN`, `SEMICOLON`, `EOF`
- `Token` dataclass: `type`, `lexeme`/`literal`, `line`, `col`
- `tokenize(source)` supporting:
  - Whitespace + newline tracking
  - Identifiers (only `print` keyword for now)
  - Numbers
  - Strings `"..."` (no escapes)
  - Single-char tokens: `+ * ( ) ;`
  - `LexError` on unknown chars

**First test:** tokenizing `print("Hello world");`

---

## Step 2 — Parser (print-only, string-only first)

Implement minimal parsing to support only:

- `print_stmt → print ( STRING ) ;`

Return AST:

- `Program([PrintStmt(LiteralExpr("Hello world"))])`

**First test:** parsing the hello program builds correct AST.

---

## Step 3 — Interpreter (print-only)

Interpret:

- Execute `Program`
- Execute `PrintStmt`
- Evaluate `LiteralExpr`
- Output to stdout

**First end-to-end run:** `python -m momolang examples/hello.momo` prints `Hello world`.

---

## Step 4 — Grow Expressions Gradually

Add in this order:

1. `NUMBER` literals
2. `+` for ints
3. `*` for ints
4. Precedence (`mul` before `add`)
5. Runtime type errors for invalid operands

Each addition should come with:

- Lexer test (if needed)
- Parser test
- Interpreter test