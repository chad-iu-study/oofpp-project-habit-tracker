from src.habit_tracker.habit import Habit
from src.habit_tracker.storage import load_habits, save_habits


class HabitManager:
    def __init__(self):
        self.habits = load_habits()

    def add_habit(self, name, period, domain):
        """
        - Create and add a new habit.
        - Appends new habit to internal list.
        - Saves to storage.
        - Returns: The created Habit instance.
        """
        habit = Habit.create(name, period, domain)
        self.habits.append(habit)
        save_habits(self.habits)
        return habit

    def delete_habit(self, index):
        """
        - Delete habit at given index.
        - Saves current internal storage to JSON storage.
        """
        del self.habits[index]
        save_habits(self.habits)
   
    def mark_habit_completed(self, index, timestamp):
        """
        - Mark habit at given index as completed.
        - timestamp: datetime of completion.
        - Saves current internal storage to JSON storage.
        """
        self.habits[index].mark_completed(timestamp)
        save_habits(self.habits)

    def get_all_habits(self):
        """
        - Return list of all habits.
        - Returns: list of Habit instances."""
        return list(self.habits)