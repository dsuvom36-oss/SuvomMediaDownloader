"""
services/history_service.py

History Service
"""

from core.history_service import get_history_database
from core.event_bus import event_bus
from core.event_types import Event


class HistoryService:

    def __init__(self):
        self.database = get_history_database()

    # -------------------------------------------------
    # Add
    # -------------------------------------------------

    def add(self, task):
        result = self.database.add_task(task)

        event_bus.publish(Event.HISTORY_ADDED, task=task)

        return result

    # -------------------------------------------------
    # Delete
    # -------------------------------------------------

    def delete(self, history_id):
        result = self.database.delete(history_id)

        event_bus.publish(Event.HISTORY_DELETED, history_id=history_id)

        return result

    # -------------------------------------------------
    # Clear
    # -------------------------------------------------

    def clear(self):
        result = self.database.clear()

        event_bus.publish(Event.HISTORY_CLEARED)

        return result

    # -------------------------------------------------
    # Get All
    # -------------------------------------------------

    def get_all(self):
        return self.database.get_all()

    # -------------------------------------------------
    # Search
    # -------------------------------------------------

    def search(self, keyword):
        return self.database.search(keyword)

    # -------------------------------------------------
    # Export CSV
    # -------------------------------------------------

    def export_csv(self, filename):
        result = self.database.export_csv(filename)

        event_bus.publish(Event.HISTORY_EXPORTED, filename=filename)

        return result

    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    def count(self):
        return len(self.get_all())

    def completed(self):
        return len(
            [
                item
                for item in self.get_all()
                if getattr(item, "status", "") == "Completed"
            ]
        )

    def failed(self):
        return len(
            [item for item in self.get_all() if getattr(item, "status", "") == "Failed"]
        )

    def cancelled(self):
        return len(
            [
                item
                for item in self.get_all()
                if getattr(item, "status", "") == "Cancelled"
            ]
        )


# -------------------------------------------------
# Lazy Singleton
# -------------------------------------------------

_history_service = None


def get_history_service():
    """
    Returns the shared HistoryService instance.
    Creates it only when first requested.
    """
    global _history_service

    if _history_service is None:
        _history_service = HistoryService()

    return _history_service
