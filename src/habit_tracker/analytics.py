from datetime import timedelta
from collections import Counter

# Define weekly persona mapping
WEEKLY_PERSONA = {
    "mind": "The Mindsmith",
    "body": "The Iron Vessel",
    "heart": "The Gentle Flame",
    "craft": "The Artisan",
    "soul": "The Seer",
}

def get_habits_by_period(habits, period):
    """
    - Filter habits by the given period (daily, weekly, monthly).
    - Return a list of habits matching the period using list comprehension.
    """
    return [habit for habit in habits if habit.period == period]

def get_weekly_domain_counts(habits, reference_time):
    week_start = reference_time - timedelta(days=7)
    counts = Counter()
    for habit in habits:
        for completion in habit.completions:
            if completion >= week_start and completion <= reference_time:
                counts[habit.domain] += 1
    return dict(counts)

def get_weekly_persona(habits, reference_time):
    counts = get_weekly_domain_counts(habits, reference_time)
    if not counts:
        return "No dominant Domain this week."
    top_domain = None
    top_count = -1
    for domain, count in counts.items():
        if count > top_count:
            top_count = count
            top_domain = domain

    if top_domain is None:
        top_domain = ""
    persona = WEEKLY_PERSONA.get(top_domain, f"The {top_domain.capitalize()}")
    return f"Your dominant Domain this week is:\n {top_domain.capitalize()}\n – Weekly Persona: '{persona}'\n Count: {top_count}."