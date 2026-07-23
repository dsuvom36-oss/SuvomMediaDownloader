from dataclasses import dataclass, field
from datetime import datetime
from threading import Lock
from typing import List


@dataclass
class Activity:
    event: str
    details: str
    category: str = "General"
    timestamp: datetime = field(default_factory=datetime.now)


class ActivityLog:

    def __init__(self):
        self._activities: List[Activity] = []
        self._lock = Lock()

    # =====================================

    def add(self, event, details="", category="General"):

        activity = Activity(event=event, details=details, category=category)

        with self._lock:
            self._activities.insert(0, activity)

        return activity

    # =====================================

    def get_all(self):

        with self._lock:
            return list(self._activities)

    # =====================================

    def filter_by_category(self, category):

        with self._lock:

            if category == "All":
                return list(self._activities)

            return [
                activity
                for activity in self._activities
                if activity.category == category
            ]

    # =====================================

    def search(self, keyword):

        keyword = keyword.lower()

        with self._lock:

            return [
                activity
                for activity in self._activities
                if (
                    keyword in activity.event.lower()
                    or keyword in activity.details.lower()
                    or keyword in activity.category.lower()
                )
            ]

    # =====================================

    def remove(self, activity):

        with self._lock:

            if activity in self._activities:
                self._activities.remove(activity)

    # =====================================

    def clear(self):

        with self._lock:
            self._activities.clear()

    # =====================================

    def count(self):

        with self._lock:
            return len(self._activities)

    # =====================================

    def count_by_category(self):

        with self._lock:

            counts = {}

            for activity in self._activities:

                counts[activity.category] = counts.get(activity.category, 0) + 1

            return counts


# ==========================================
# Shared Global Instance
# ==========================================

activity_log = ActivityLog()
