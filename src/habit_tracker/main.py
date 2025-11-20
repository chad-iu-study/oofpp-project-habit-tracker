import sys
import os
from datetime import datetime, timezone
from habit_manager import HabitManager
from analytics import (
    get_habits_by_period,
    get_weekly_persona,
)


# Constants for valid periods and domains
VALID_PERIODS = ("daily", "weekly", "monthly")
VALID_DOMAINS = ("body", "mind", "heart", "craft", "soul")


def list_habits(mgr):
    """
    - List all habits. 
    - Pull from habit manager. 
    - If none, print no habits yet.
    """
    habits = mgr.get_all_habits()
    if habits == [None]:
        print("No habits yet.")
    for i, habit in enumerate(habits):
        print_habit(habit, i + 1)


def create_habit(mgr):
    """
    - Create a new habit by prompting user for name, period, domain.
    - Uses choose() to validate period and domain.
    - Adds habit to manager and returns the created habit.
    """
    name = input("Habit name: ").strip()
    period = choose("Period (daily/weekly/monthly): ", VALID_PERIODS)
    domain = choose("Domain (body/mind/heart/craft/soul): ", VALID_DOMAINS)
    habit = mgr.add_habit(name, period, domain)
    print("Created:", habit.name)


def delete_habit(mgr):
    """
    - Delete a habit by prompting user for index.
    - Handles invalid input and exceptions.
    """
    selection = input("Enter index to delete: ").strip()
    try:
        index = check_index(int(selection), mgr)
        mgr.delete_habit(index)
        print("Deleted.")
    except Exception as e:
        print("Error:", e)


def mark_habit_completed(mgr):
    """
    - Mark a habit as completed by prompting user for index.
    - Handles invalid input and exceptions.
    """
    selection = input("Enter index to mark as completed: ").strip()
    try:
        index = check_index(int(selection), mgr)
        mgr.mark_habit_completed(index, now_utc())
        print("Marked as completed.")
    except Exception as e:
        print("Error:", e)


def view_analytics(mgr):
    """
    - View analytics including weekly persona.
    """
    habits = mgr.get_all_habits()
    print("Habits by period:")
    for period in VALID_PERIODS:
        grouped = get_habits_by_period(habits, period)
        print(f"  {period}: {len(grouped)}")
    persona = get_weekly_persona(habits, now_utc())
    print(persona)


# Helper functions
def print_habit(habit, index=None):
    """
    - Print habit details in formatted way.
    - Includes name, period, domain, created_at, and number of completions.
    """
    print(f"[{index}] {habit.name}")
    print(f"     period: {habit.period}, domain: {habit.domain}, created: {habit.created_at.strftime('%d %B %Y, %H:%M')} ")
    print(f"     completions: {len(habit.completions)}")


def choose(prompt, validOptions):
    """
    - Loops until user inputs a valid choice from valid list. 
    - Removes leading/trailing white space and makes input lowercase.
    - Returns the valid choice.
    """
    while True:
        option = input(prompt).strip().lower()
        if option in validOptions:
            return option
        print("Invalid choice. Options:", ", ".join(validOptions))


def show_menu():
    print("\nMenu:")
    print("1) List habits")
    print("2) Create habit")
    print("3) Delete habit")
    print("4) Mark habit as completed")
    print("5) View analytics & weekly persona")
    print("6) Exit")


def check_index(input_str, mgr):
    """
    - Validate user input as index.
    - Returns index if valid, else None."""
    # get max index
    max_index = len(mgr.get_all_habits())
    index = input_str
    if 1 <= index <= max_index:
        return index
    else:
        print(f"Index out of range. Please enter a number between 1 and {max_index}.")
        return None
    

def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def main():
    mgr = HabitManager()
    print(" --- Habit Tracker CLI --- ")
    while True:
        os.system("clear")
        show_menu()
        choice = input("Choose: ").strip()
        if choice == "1":
            os.system("clear")
            list_habits(mgr)
            input("Press Enter to continue...")
        elif choice == "2":
            os.system("clear")
            create_habit(mgr)
        elif choice == "3":
            os.system("clear")
            show_menu()
            delete_habit(mgr)
        elif choice == "4":
            os.system("clear")
            list_habits(mgr)
            mark_habit_completed(mgr)
        elif choice == "5":
            os.system("clear")
            view_analytics(mgr)
            input("Press Enter to continue...")
        elif choice == "6":
            print("Bye.")
            sys.exit(0)
        else:
            print("Invalid menu choice.")


if __name__ == "__main__":
    main()