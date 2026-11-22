# Learning log

- **Project:** In-memory command-line task tracker.
- **Completed milestone:** Fixed index bounds and duplicate-title checking. Five CLI checks passed: invalid indices retry, both valid positions work, duplicates are rejected, both completion actions work through all tasks, and empty entry exits.
- **Concepts demonstrated:** Dictionaries containing lists, moving tasks between lists, short-circuit validation with range membership, duplicate prevention, and stopping when active tasks run out.
- **Support level:** Index bounds and duplicate checking were fixed by the learner after targeted feedback and a comparison example. Independent design and transfer have not yet been assessed.
- **Program adjustment:** Use substantial milestones with learner-owned design, documentation use, debugging, and validation. Minor wording cleanup is optional review feedback, not a separate milestone. After persistence, move to a directory audit tool rather than expanding the tracker.
- **Practice next:** File handling, JSON serialization, missing-file handling, and designing and checking a feature from requirements.
- **Current blocker:** No blocker in the previously checked flows. Persistence has been assigned but not reviewed; wording cleanup does not block it.
- **Next milestone:** Save active and completed tasks to tasks.json on normal exit; restore them on startup and skip initial entry when a save exists; use the existing entry flow when the file is missing. The learner chooses the implementation and demonstrates a first run, exit/restart with one completed task, and restart with all tasks completed. Review damaged-file handling afterward.
