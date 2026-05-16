import unittest

from tasks_cli import tasks as task_ops


def _task(task_id: int, title: str, completed: bool = False) -> dict:
    return {"id": task_id, "title": title, "completed": completed}


class AddTaskTests(unittest.TestCase):
    def test_first_task_gets_id_one(self) -> None:
        task_list: list[dict] = []
        task_ops.add_task(task_list, "Primera")
        self.assertEqual(task_list[0]["id"], 1)
        self.assertEqual(task_list[0]["title"], "Primera")
        self.assertFalse(task_list[0]["completed"])

    def test_next_id_is_max_plus_one(self) -> None:
        task_list = [_task(1, "a"), _task(3, "b")]
        task_ops.add_task(task_list, "c")
        self.assertEqual(task_list[-1]["id"], 4)

    def test_next_id_when_no_valid_ids_returns_one(self) -> None:
        task_list = [{"title": "sin id"}, {"id": "x", "title": "id inválido"}]
        task_ops.add_task(task_list, "nueva")
        self.assertEqual(task_list[-1]["id"], 1)


class CompleteTaskTests(unittest.TestCase):
    def test_complete_pending_task(self) -> None:
        task_list = [_task(1, "a", completed=False)]
        self.assertEqual(task_ops.complete_task(task_list, 1), "completed")
        self.assertTrue(task_list[0]["completed"])

    def test_complete_already_completed(self) -> None:
        task_list = [_task(1, "a", completed=True)]
        self.assertEqual(task_ops.complete_task(task_list, 1), "already_completed")

    def test_complete_missing_id(self) -> None:
        task_list = [_task(1, "a")]
        self.assertEqual(task_ops.complete_task(task_list, 99), "not_found")


class EditTaskTests(unittest.TestCase):
    def test_edit_updates_title(self) -> None:
        task_list = [_task(1, "viejo")]
        self.assertEqual(task_ops.edit_task(task_list, 1, "nuevo"), "edited")
        self.assertEqual(task_list[0]["title"], "nuevo")

    def test_edit_strips_title(self) -> None:
        task_list = [_task(1, "viejo")]
        task_ops.edit_task(task_list, 1, "  nuevo  ")
        self.assertEqual(task_list[0]["title"], "nuevo")

    def test_edit_same_title_is_unchanged(self) -> None:
        task_list = [_task(1, "igual")]
        self.assertEqual(task_ops.edit_task(task_list, 1, "  igual  "), "unchanged")

    def test_edit_missing_id(self) -> None:
        task_list = [_task(1, "a")]
        self.assertEqual(task_ops.edit_task(task_list, 99, "b"), "not_found")


class SearchTasksTests(unittest.TestCase):
    def setUp(self) -> None:
        self.task_list = [
            _task(1, "Estudiar Python"),
            _task(2, "Comprar leche"),
            _task(3, "python avanzado"),
        ]

    def test_search_is_case_insensitive(self) -> None:
        matches = task_ops.search_tasks(self.task_list, "PYTHON")
        self.assertEqual(len(matches), 2)
        self.assertEqual({t["id"] for t in matches}, {1, 3})

    def test_search_partial_match(self) -> None:
        matches = task_ops.search_tasks(self.task_list, "leche")
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]["id"], 2)

    def test_search_no_matches(self) -> None:
        self.assertEqual(task_ops.search_tasks(self.task_list, "docker"), [])


class DeleteTaskTests(unittest.TestCase):
    def test_delete_existing_task(self) -> None:
        task_list = [_task(1, "a"), _task(2, "b")]
        self.assertTrue(task_ops.delete_task(task_list, 1))
        self.assertEqual(len(task_list), 1)
        self.assertEqual(task_list[0]["id"], 2)

    def test_delete_missing_id(self) -> None:
        task_list = [_task(1, "a")]
        self.assertFalse(task_ops.delete_task(task_list, 99))
        self.assertEqual(len(task_list), 1)


if __name__ == "__main__":
    unittest.main()
