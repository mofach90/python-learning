# Learning log

- **Project:** In-memory command-line task tracker.
- **Completed milestone:** The tracker stores tasks with completion status and displays completed tasks with a strikethrough. Code inspected; not run.
- **Concepts demonstrated:** Input validation, loops, dictionaries, functions, type hints, and representing task state with booleans.
- **Practice next:** Call string methods during validation and make the completion action clear in the menu.
- **Current blocker:** `index.isdigit` is referenced without `()`, so it does not check the input; converting non-numeric input can raise `ValueError`. Completed tasks are stored in the same dictionary, not a separate list as the task requested.
- **Next task:** Fix index input validation so non-numeric and out-of-range entries are rejected cleanly.
