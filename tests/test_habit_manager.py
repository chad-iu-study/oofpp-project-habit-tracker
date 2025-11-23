import unittest
from unittest.mock import patch
from datetime import datetime

from src.habit_tracker.habit_manager import HabitManager
from src.habit_tracker.habit import Habit


class TestHabitManager(unittest.TestCase):
    @patch("src.habit_tracker.habit_manager.load_habits", return_value=[])
    def test_init_uses_load_habits(self, mock_load_habits):
        mgr = HabitManager()
        mock_load_habits.assert_called_once()
        self.assertEqual(mgr.habits, [])

    @patch("src.habit_tracker.habit_manager.save_habits")
    @patch("src.habit_tracker.habit_manager.load_habits", return_value=[])
    def test_add_habit(self, mock_load_habits, mock_save_habits):
        mgr = HabitManager()
        habit = mgr.add_habit("Meditate", "daily", "mind")
        self.assertIn(habit, mgr.habits)
        mock_save_habits.assert_called_once()

    @patch("src.habit_tracker.habit_manager.save_habits")
    @patch("src.habit_tracker.habit_manager.load_habits")
    def test_delete_habit(self, mock_load_habits, mock_save_habits):
        h1 = Habit.create("H1", "daily", "mind")
        h2 = Habit.create("H2", "weekly", "body")
        mock_load_habits.return_value = [h1, h2]

        mgr = HabitManager()
        mgr.delete_habit(0)

        self.assertEqual(mgr.habits, [h2])
        mock_save_habits.assert_called_once()

    @patch("src.habit_tracker.habit_manager.save_habits")
    @patch("src.habit_tracker.habit_manager.load_habits")
    def test_mark_habit_completed(self, mock_load_habits, mock_save_habits):
        h = Habit.create("Run", "daily", "body")
        mock_load_habits.return_value = [h]

        mgr = HabitManager()
        ts = datetime.now()
        mgr.mark_habit_completed(0, ts)

        self.assertEqual(len(h.completions), 1)
        self.assertEqual(h.completions[0], ts)
        mock_save_habits.assert_called_once()

    @patch("src.habit_tracker.habit_manager.save_habits")
    @patch("src.habit_tracker.habit_manager.load_habits", return_value=[])
    def test_mark_habit_completed_invalid_index(self, mock_load_habits, mock_save_habits):
        mgr = HabitManager()
        with self.assertRaises(IndexError):
            mgr.mark_habit_completed(0, datetime.now())
        mock_save_habits.assert_not_called()

    @patch("src.habit_tracker.habit_manager.load_habits")
    def test_get_all_habits_returns_copy(self, mock_load_habits):
        h = Habit.create("X", "daily", "mind")
        mock_load_habits.return_value = [h]

        mgr = HabitManager()
        result = mgr.get_all_habits()

        self.assertEqual(result, [h])
        self.assertIsNot(result, mgr.habits)


if __name__ == "__main__":
    unittest.main()