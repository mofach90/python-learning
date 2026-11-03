# Learning log

- **Project:** In-memory command-line task tracker.
- **Completed milestone:** Collect task titles, display them, keep the remove menu available for multiple actions, and leave it with `break` on choice `0`. Code inspected; not run.
- **Concepts demonstrated:** Input validation, loops, lists, functions, type hints, dictionaries, and dispatching a selected action.
- **Practice next:** Handle an empty task list clearly; distinguish returning from `main()` from terminating the process.
- **Current blocker:** The tracker uses `exit()` when the starting list is empty; removal functions also cannot accept a selection if called with an empty list.
- **Next task:** Make the tracker end gracefully when the task list is empty, without calling `exit()`.
