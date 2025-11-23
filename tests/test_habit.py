import unittest
import uuid
from datetime import datetime, timedelta, timezone

from src.habit_tracker.habit import Habit


class TestHabit(unittest.TestCase):

    def test_create_initializes_properly(self):
        h = Habit.create("Read", "daily", "mind")

        self.assertEqual(h.name, "Read")
        self.assertEqual(h.period, "daily")
        self.assertEqual(h.domain, "mind")

        self.assertEqual(len(h.completions), 0)

        self.assertTrue(uuid.UUID(h.id))

        self.assertEqual(h.created_at.tzinfo, timezone.utc)
        now = datetime.now(timezone.utc)
        self.assertLess((now - h.created_at).total_seconds(), 5)

    def test_mark_completed_stores_timestamp(self):
        h = Habit.create("Run", "daily", "body")
        t = datetime.now(timezone.utc)
        h.mark_completed(t)

        self.assertEqual(len(h.completions), 1)
        self.assertEqual(h.completions[0], t)

    def test_mark_completed_preserves_order(self):
        h = Habit.create("Walk", "daily", "body")
        t1 = datetime.now(timezone.utc) - timedelta(minutes=5)
        t2 = datetime.now(timezone.utc)

        h.mark_completed(t1)
        h.mark_completed(t2)

        self.assertEqual(h.completions, [t1, t2])

    def test_multiple_habits_have_unique_ids(self):
        h1 = Habit.create("A", "daily", "mind")
        h2 = Habit.create("B", "daily", "mind")
        self.assertNotEqual(h1.id, h2.id)

    def test_stores_many_completions(self):
        h = Habit.create("Bulk", "daily", "mind")
        base = datetime.now(timezone.utc)

        for i in range(200):
            h.mark_completed(base + timedelta(seconds=i))

        self.assertEqual(len(h.completions), 200)
        self.assertEqual(h.completions[0], base)
        self.assertEqual(h.completions[-1], base + timedelta(seconds=199))


if __name__ == "__main__":
    unittest.main()