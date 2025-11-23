import unittest
from datetime import datetime, timedelta, timezone

from src.habit_tracker.habit import Habit
from src.habit_tracker.analytics import (
    get_habits_by_period,
    get_weekly_domain_counts,
    get_weekly_persona,
    get_monthly_habit_summary,
    get_weekly_habit_summary,
)


class TestAnalytics(unittest.TestCase):
    def setUp(self):
        now = datetime.now(timezone.utc)
        self.now = now
        self.h1 = Habit.create("Read", "daily", "mind")
        self.h2 = Habit.create("Run", "daily", "body")
        self.h3 = Habit.create("Paint", "weekly", "craft")

        self.h1.completions.append(now - timedelta(days=1))
        self.h1.completions.append(now - timedelta(days=3))
        self.h2.completions.append(now - timedelta(days=2))
        self.h2.completions.append(now - timedelta(days=15))
        self.h3.completions.append(now - timedelta(days=10))

        self.habits = [self.h1, self.h2, self.h3]

    def test_get_habits_by_period(self):
        daily = get_habits_by_period(self.habits, "daily")
        weekly = get_habits_by_period(self.habits, "weekly")
        self.assertEqual(len(daily), 2)
        self.assertEqual(len(weekly), 1)

    def test_get_weekly_domain_counts(self):
        counts = get_weekly_domain_counts(self.habits, self.now)
        self.assertEqual(counts.get("mind"), 2)
        self.assertEqual(counts.get("body"), 1)
        self.assertNotIn("craft", counts)

    def test_get_weekly_persona(self):
        persona = get_weekly_persona(self.habits, self.now)
        self.assertIsInstance(persona, str)

    def test_get_monthly_habit_summary(self):
        summary = get_monthly_habit_summary(self.habits, self.now)
        self.assertEqual(summary.get("Read"), 2)
        self.assertEqual(summary.get("Run"), 2)
        self.assertEqual(summary.get("Paint"), 1)

    def test_get_weekly_habit_summary(self):
        summary = get_weekly_habit_summary(self.habits, self.now)
        self.assertEqual(summary.get("Read"), 2)
        self.assertEqual(summary.get("Run"), 1)
        self.assertIsNone(summary.get("Paint"))


if __name__ == "__main__":
    unittest.main()