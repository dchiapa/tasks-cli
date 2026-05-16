import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from task_cli import storage


class StorageTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmpdir = tempfile.TemporaryDirectory()
        self.tasks_path = Path(self._tmpdir.name) / "tasks.json"
        self._patch = patch.object(storage, "tasks_file_path", return_value=self.tasks_path)
        self._patch.start()

    def tearDown(self) -> None:
        self._patch.stop()
        self._tmpdir.cleanup()

    def test_load_returns_empty_when_file_missing(self) -> None:
        self.assertEqual(storage.load_tasks(), [])

    def test_load_returns_empty_when_file_is_empty(self) -> None:
        self.tasks_path.write_text("", encoding="utf-8")
        self.assertEqual(storage.load_tasks(), [])

    def test_save_and_load_round_trip(self) -> None:
        data = [{"id": 1, "title": "Probar", "completed": False}]
        storage.save_tasks(data)
        loaded = storage.load_tasks()
        self.assertEqual(loaded, data)

    def test_saved_file_is_valid_json_list(self) -> None:
        storage.save_tasks([{"id": 1, "title": "x", "completed": True}])
        parsed = json.loads(self.tasks_path.read_text(encoding="utf-8"))
        self.assertIsInstance(parsed, list)
        self.assertEqual(parsed[0]["title"], "x")

    def test_load_returns_empty_when_root_is_not_a_list(self) -> None:
        self.tasks_path.write_text('{"id": 1}', encoding="utf-8")
        self.assertEqual(storage.load_tasks(), [])


if __name__ == "__main__":
    unittest.main()
