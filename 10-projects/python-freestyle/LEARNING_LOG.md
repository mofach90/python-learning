# Learning log

- **Project:** In-memory command-line task tracker.
- **Completed milestone:** The tracker stores task status in one dictionary, builds active and completed display groups, skips index prompting when no active tasks remain, and prints a message for that empty-index case. Code inspected; not run.
- **Concepts demonstrated:** Input validation, short-circuit evaluation with `and`, loops, dictionaries, booleans, and deriving display groups from stored data.
- **Practice next:** Keep menu actions valid as task state changes and make their effects clear to the user.
- **Current blocker:** The menu still says “search and check,” task options only say “Task Title/Index,” and the title action prints “Removing.” The empty-index message does not tell the user that no active tasks are available.
- **Next task:** Update the menu and messages so they clearly say the actions mark active tasks complete, including a clear message when none remain.
