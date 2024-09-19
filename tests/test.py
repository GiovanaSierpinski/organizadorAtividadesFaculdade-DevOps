from src.main import *
import unittest
from unittest.mock import patch, mock_open

class TestOrganizadorAtividades(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[{"name": "Somativa 1", "subject": "DevOps", "completed": false}]')
    def test_load_tasks(self, mock_file):
        tasks = load_tasks("tasks.json")
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["name"], "Somativa 1")

    @patch("builtins.open", new_callable=mock_open)
    def test_save_tasks(self, mock_file):
        tasks = [{"name": "Somativa 1", "subject": "DevOps", "completed": False}]
        save_tasks(tasks, "tasks.json")
        mock_file.assert_called_once_with("tasks.json", "w")
        mock_file().write.assert_called_once_with(json.dumps(tasks, indent=4))

    @patch("builtins.open", new_callable=mock_open)
    def test_add_task(self, mock_file):
        tasks = []
        add_task(tasks, "Estudar física", "Física")
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["name"], "Estudar física")
        self.assertEqual(tasks[0]["subject"], "Física")
        self.assertFalse(tasks[0]["completed"])

    def test_complete_task(self):
        tasks = [{"name": "Estudar física", "subject": "Física", "completed": False}]
        complete_task(tasks, 0)
        self.assertTrue(tasks[0]["completed"])

    def test_remove_task(self):
        tasks = [{"name": "Estudar física", "subject": "Física", "completed": False}]
        remove_task(tasks, 0)
        self.assertEqual(len(tasks), 0)

if __name__ == "__main__":
    unittest.main()

