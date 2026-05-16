import json
from pathlib import Path


def _project_root() -> Path:
    return Path(__file__).resolve().parent.parent


def tasks_file_path() -> Path:
    return _project_root() / "tasks.json"


def load_tasks() -> list[dict]:
    path = tasks_file_path()
    if not path.is_file():
        return []
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return []
    data = json.loads(text)
    if not isinstance(data, list):
        return []
    return data


def save_tasks(tasks: list[dict]) -> None:
    path = tasks_file_path()
    path.write_text(
        json.dumps(tasks, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
