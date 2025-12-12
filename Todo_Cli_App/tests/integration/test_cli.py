import unittest
import subprocess
import os
import sys

class TestTodoCLI(unittest.TestCase):

    def setUp(self):
        # Ensure the todo.py script is executable for testing
        self.todo_script = os.path.join(os.path.dirname(__file__), '../../src/todo.py')
        self.interpreter = sys.executable # Use the current Python interpreter

    def run_cli_command(self, input_data):
        """Helper to run the CLI with given input and capture output."""
        process = subprocess.run(
            [self.interpreter, self.todo_script],
            input=input_data,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        return process.stdout, process.stderr

    def test_add_and_view_task(self):
        # Test adding a task and then viewing it
        input_sequence = "1\nTest Task 1\n\n2\n6\n"
        stdout, stderr = self.run_cli_command(input_sequence)

        self.assertIn("Task added successfully!", stdout)
        self.assertIn("[ ] 1: Test Task 1", stdout)
        self.assertIn("Exiting application. Goodbye!", stdout)
        self.assertEqual(stderr, "")

    def test_add_and_view_multiple_tasks(self):
        # Test adding multiple tasks and viewing them
        input_sequence = "1\nTask Alpha\n\n1\nTask Beta\nDescription Beta\n2\n6\n"
        stdout, stderr = self.run_cli_command(input_sequence)

        self.assertIn("Task added successfully!", stdout)
        self.assertIn("[ ] 1: Task Alpha", stdout)
        self.assertIn("[ ] 2: Task Beta (Description Beta)", stdout)
        self.assertIn("Exiting application. Goodbye!", stdout)
        self.assertEqual(stderr, "")

    def test_view_empty_tasks(self):
        # Test viewing tasks when none are present
        input_sequence = "2\n6\n"
        stdout, stderr = self.run_cli_command(input_sequence)

        self.assertIn("No tasks to display.", stdout)
        self.assertIn("Exiting application. Goodbye!", stdout)
        self.assertEqual(stderr, "")

    def test_mark_task_complete(self):
        # Add a task, mark it complete, and view it
        input_sequence = "1\nTask to complete\n\n3\n1\n2\n6\n"
        stdout, stderr = self.run_cli_command(input_sequence)

        self.assertIn("Task added successfully!", stdout)
        self.assertIn("Task 1 marked as complete.", stdout)
        self.assertIn("[✓] 1: Task to complete", stdout)
        self.assertIn("Exiting application. Goodbye!", stdout)
        self.assertEqual(stderr, "")

    def test_mark_task_complete_invalid_id(self):
        # Try to mark a non-existent task as complete
        input_sequence = "1\nTask to complete\n\n3\n999\n6\n"
        stdout, stderr = self.run_cli_command(input_sequence)

        self.assertIn("Task added successfully!", stdout)
        self.assertIn("Task 999 not found.", stdout)
        self.assertIn("Exiting application. Goodbye!", stdout)
        self.assertEqual(stderr, "")

if __name__ == '__main__':
    unittest.main()
