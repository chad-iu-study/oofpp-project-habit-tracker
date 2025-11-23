import json
import os
from src.habit_tracker.habit import Habit
from datetime import datetime


BASE_DIR = os.path.dirname(__file__)
DEFAULT_PATH = os.path.join(BASE_DIR, "..", "..", "habits.json")


def load_habits():
    """
    - Load habits from the default JSON file.
    - Returns list[Habit]: list of Habit instances.
    """
    if not os.path.exists(DEFAULT_PATH):
        return []
    
    try:
        with open(DEFAULT_PATH, "r") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print("Error decoding JSON from habits file.")
        return []
    except FileNotFoundError:
        print("Habits file not found.")
        return []
    except Exception as e:
        print(f"An error occurred while loading habits: {e}")
        return []
    
    return [habit_from_dict(item) for item in data]


def save_habits(habits):
    """
    - Save list of Habits to JSON file.
    - habits: list of Habit instances to save.
    """
    data = [habit_to_dict(habit) for habit in habits]
    with open(DEFAULT_PATH, "w") as f:
        json.dump(data, f, indent=2)


def habit_to_dict(habit):
    """
    - Convert Habit instance to dictionary for JSON serialization.
    - habit: Habit instance to convert.
    - Returns: dict representation of the Habit.
    """
    return {
        "id": habit.id,
        "name": habit.name,
        "period": habit.period,
        "domain": habit.domain,
        "created_at": habit.created_at.isoformat(),
        "completions": [completion.isoformat() for completion in habit.completions],
    }


def habit_from_dict(data):
    """
    - Create Habit instance from JSON object.
    - data: dict representation of the Habit.
    - Returns: Habit instance.
    """
    created_at = datetime.fromisoformat(data["created_at"])
    completions = [datetime.fromisoformat(completion) for completion in data.get("completions", [])]
    return Habit(
        id=data["id"],
        name=data["name"],
        period=data["period"],
        domain=data["domain"],
        created_at=created_at,
        completions=completions,
    )