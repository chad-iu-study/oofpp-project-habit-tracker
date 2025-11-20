from dataclasses import dataclass, field
from datetime import datetime, timezone
import uuid


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


@dataclass
class Habit:
    """
    Represents a single habit.

    Attributes:
        id - Unique identifier for the habit.
        name - Name of the habit.
        period - One type of 'daily', 'weekly', or 'monthly'.
        domain - Category the habit belongs to ('body', 'mind', etc.).
        created_at - Time habit was created.
        completions - Time when habit was completed.

    Methods:
        - Use Habit.create() to generate a new habit with an auto-uuid
            return: Habit instance.
        - Use mark_completed() to log completions.
    """
    id: str
    name: str
    period: str  # "daily" | "weekly" | "monthly"
    domain: str  # "body" | "mind" | "heart" | "craft" | "soul"
    created_at: datetime
    completions: list[datetime] = field(default_factory=list)

    @classmethod
    def create(cls, name, period, domain):
        return cls(
            id=str(uuid.uuid4()),
            name=name,
            period=period,
            domain=domain,
            created_at=now_utc(),
            completions=[],
        )

    def mark_completed(self, timestamp):
        self.completions.append(timestamp)