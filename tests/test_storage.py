import unittest
import os
import tempfile
from datetime import datetime

from src.habit_tracker.storage import load_habits, save_habits, habit_to_dict, habit_from_dict
from src.habit_tracker.habit import Habit


class TestStorage(unittest.TestCase):
    def test_habit_to_dict_and_from_dict_roundtrip(self):
        h = Habit.create("Read", "daily", "mind")
        h.completions.append(datetime.now())

        d = habit_to_dict(h)
        h2 = habit_from_dict(d)

        self.assertEqual(h.id, h2.id)
        self.assertEqual(h.name, h2.name)
        self.assertEqual(h.period, h2.period)
        self.assertEqual(h.domain, h2.domain)
        self.assertEqual(len(h2.completions), 1)

    def test_load_habits_missing_file_returns_empty_list(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "habits.json")
            habits = load_habits(path=path)
            self.assertEqual(habits, [])

    def test_save_and_load_roundtrip_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "habits.json")

            h1 = Habit.create("Read", "daily", "mind")
            h2 = Habit.create("Run", "weekly", "body")

            save_habits([h1, h2], path=path)
            loaded = load_habits(path=path)

            self.assertEqual(len(loaded), 2)
            names = {h.name for h in loaded}
            self.assertEqual(names, {"Read", "Run"})


if __name__ == "__main__":
    unittest.main()