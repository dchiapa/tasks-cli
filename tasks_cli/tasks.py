def _next_id(tasks: list[dict]) -> int:
    ids: list[int] = []
    for task in tasks:
        raw = task.get("id")
        try:
            ids.append(int(raw))
        except (TypeError, ValueError):
            continue
    return max(ids) + 1 if ids else 1


def add_task(tasks: list[dict], title: str) -> None:
    tasks.append(
        {
            "id": _next_id(tasks),
            "title": title,
            "completed": False,
        }
    )


def complete_task(tasks: list[dict], task_id: int) -> str:
    for task in tasks:
        if int(task.get("id", -1)) == task_id:
            if bool(task.get("completed", False)):
                return "already_completed"
            task["completed"] = True
            return "completed"
    return "not_found"


def edit_task(tasks: list[dict], task_id: int, new_title: str) -> str:
    for task in tasks:
        if int(task.get("id", -1)) == task_id:
            if task.get("title", "").strip() == new_title.strip():
                return "unchanged"
            task["title"] = new_title.strip()
            return "edited"
    return "not_found"


def search_tasks(tasks: list[dict], query: str) -> list[dict]:
    needle = query.casefold()
    return [
        task
        for task in tasks
        if needle in str(task.get("title", "")).casefold()
    ]


def delete_task(tasks: list[dict], task_id: int) -> bool:
    before = len(tasks)
    remaining = [t for t in tasks if int(t.get("id", -1)) != task_id]
    if len(remaining) == before:
        return False
    tasks.clear()
    tasks.extend(remaining)
    return True
