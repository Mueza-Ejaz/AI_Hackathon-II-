import unittest
from src.todo import TodoApp, Task

class TestTodoApp(unittest.TestCase):

    def setUp(self):
        self.app = TodoApp()

    def test_add_task(self):
        task = self.app.add_task("Buy groceries")
        self.assertIsInstance(task, Task)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Buy groceries")
        self.assertIsNone(task.description)
        self.assertFalse(task.completed)
        self.assertEqual(len(self.app.tasks), 1)
        self.assertEqual(self.app._next_id, 2)

        task2 = self.app.add_task("Walk the dog", "Morning walk")
        self.assertIsInstance(task2, Task)
        self.assertEqual(task2.id, 2)
        self.assertEqual(task2.title, "Walk the dog")
        self.assertEqual(task2.description, "Morning walk")
        self.assertFalse(task2.completed)
        self.assertEqual(len(self.app.tasks), 2)
        self.assertEqual(self.app._next_id, 3)

    def test_get_all_tasks(self):
        self.assertEqual(self.app.get_all_tasks(), [])
        self.app.add_task("Task 1")
        self.app.add_task("Task 2")
        tasks = self.app.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].title, "Task 1")
        self.assertEqual(tasks[1].title, "Task 2")

    def test_mark_task_complete(self):
        self.app.add_task("Task 1")
        self.app.add_task("Task 2")
        self.assertTrue(self.app.mark_task_complete(1))
        self.assertTrue(self.app.tasks[0].completed)
        self.assertFalse(self.app.tasks[1].completed)

    def test_mark_task_complete_invalid_id(self):
        self.app.add_task("Task 1")
        self.assertFalse(self.app.mark_task_complete(999))
        self.assertFalse(self.app.tasks[0].completed)

    def test_update_task_title(self):
        task = self.app.add_task("Old Title", "Old Description")
        self.assertTrue(self.app.update_task(task.id, new_title="New Title"))
        self.assertEqual(task.title, "New Title")
        self.assertEqual(task.description, "Old Description")

    def test_update_task_description(self):
        task = self.app.add_task("Old Title", "Old Description")
        self.assertTrue(self.app.update_task(task.id, new_description="New Description"))
        self.assertEqual(task.title, "Old Title")
        self.assertEqual(task.description, "New Description")

    def test_update_task_both(self):
        task = self.app.add_task("Old Title", "Old Description")
        self.assertTrue(self.app.update_task(task.id, new_title="New Title", new_description="New Description"))
        self.assertEqual(task.title, "New Title")
        self.assertEqual(task.description, "New Description")

    def test_update_task_invalid_id(self):
        self.app.add_task("Some Task")
        self.assertFalse(self.app.update_task(999, new_title="Non Existent"))

    def test_update_task_no_changes(self):
        task = self.app.add_task("Title", "Description")
        self.assertTrue(self.app.update_task(task.id)) # Should return True as ID found, but no changes made
        self.assertEqual(task.title, "Title")
        self.assertEqual(task.description, "Description")

    def test_delete_task(self):
        self.app.add_task("Task 1")
        self.app.add_task("Task 2")
        self.assertTrue(self.app.delete_task(1))
        self.assertEqual(len(self.app.tasks), 1)
        self.assertEqual(self.app.tasks[0].id, 2)

    def test_delete_task_invalid_id(self):
        self.app.add_task("Task 1")
        self.assertFalse(self.app.delete_task(999))
        self.assertEqual(len(self.app.tasks), 1)

    def test_delete_only_task(self):
        self.app.add_task("Only Task")
        self.assertTrue(self.app.delete_task(1))
        self.assertEqual(len(self.app.tasks), 0)

if __name__ == '__main__':
    unittest.main()
