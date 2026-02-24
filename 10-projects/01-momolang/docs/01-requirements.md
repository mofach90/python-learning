# MomoLang — Requirements (v0.1)

## Goal
Build a minimal toy programming language (“Momolang”) in Python to solidify understanding of the language pipeline (lexing → parsing → AST → interpretation) by producing a runnable CLI tool that can execute simple programs (starting with `print` and basic literals/expressions).

## Stakeholders / Users
- Primary user: me (learning Python + CS fundamentals)
- Secondary user: future me / other learners reading the repo (needs clear docs, examples, and tests)

## Top Use Cases
1. As a learner, I want to write a Momolang source file in my editor and run it from the terminal, so that I can observe the full execution pipeline end-to-end.
2. As a learner, I want to see clear syntax errors with line/column information, so that I can understand how lexers/parsers report problems.
3. As a learner, I want to inspect intermediate representations (tokens and/or AST), so that I can debug and verify each compiler stage.

## Functional Requirements (v0.1 / MVP)

### Language features
- The language must support a `print` statement that outputs the evaluated value of an expression to stdout.
- The language must support:
  - integer literals (e.g., `1`, `42`)
  - string literals (e.g., `"hello"`)
- The language must support arithmetic expressions:
  - addition using `+` for integers (e.g., `1 + 2`)
  - multiplication using `*` for integers (e.g., `3 * 4`)
- The language must support expression evaluation inside `print`, e.g.:
  - `print 1 + 2;`
  - `print 2 * 3;`

### Errors
- Syntax errors must be reported with at least:
  - error type (LexError or ParseError)
  - line and column number
  - a short message describing what was expected vs what was found
- Runtime errors must be reported with at least:
  - error type (RuntimeError)
  - a short message describing the failure (e.g., invalid operand types)

## Out of Scope (v0.1 / Non-goals)
- Variables / assignment (e.g., `let x = 3`)
- Control flow: `if`, `else`, `while`, `for`
- Functions (user-defined or built-in beyond `print`)
- Data structures (arrays/lists/maps)
- Modules/imports
- Floating point numbers
- Bytecode compilation / VM (tree-walk interpreter only in v0.1)
- Optimizations (performance is not a goal)