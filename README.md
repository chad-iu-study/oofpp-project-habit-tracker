# Habit Tracker (OOP Python)

A minimal, object-oriented habit tracking application written in Python. The program runs from the command line and stores data in a local JSON file. It follows a clean separation of concerns between model, storage, manager, analytics, and a simple CLI interface.

## Features

- Create daily, weekly, or monthly habits  
- Delete habits  
- Mark habits as completed (UTC timestamp)  
- JSON-based storage (`habits.json`)  
- Analytics:
  - Habits grouped by period  
  - Weekly domain counts  
  - Weekly persona summary  
  - Longest streak calculations  

## Project Structure
habit-tracker/
├─ src/
│  └─ habit_tracker/
│     ├─ habit.py
│     ├─ storage.py
│     ├─ habit_manager.py
│     ├─ analytics.py
│     └─ main.py
│
├─ tests/
│  ├─ test_habit.py
│  ├─ test_storage.py
│  ├─ test_manager.py
│  └─ test_analytics.py
│
├─ habits.json
├─ requirements.txt
├─ README.md
└─ Makefile

## Installation
```bash
git clone <repo-url>
cd src/habit-tracker
python -m venv .venv

# macOS / Linux
source .venv/bin/activate

# Windows (PowerShell)
# .venv\Scripts\activate

pip install -r requirements.txt

## RUN Project
python main.py

## RUN Tests
python -m unittest discover -s tests