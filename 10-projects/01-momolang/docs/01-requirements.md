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