"""
core/notification_store.py
"""

from dataclasses import dataclass, field
from datetime import datetime
from threading import Lock
from typing import List


@dataclass
class Notification:
    title: str
    message: str
    level: str = "info"
    timestamp: datetime = field(default_factory=datetime.now)
    read: bool = False


class NotificationStore:

    def __init__(self):
        self._notifications: List[Notification] = []
        self._lock = Lock()

    # -------------------------------------
    # Add
    # -------------------------------------

    def add(self, title, message, level="info"):

        notification = Notification(title=title, message=message, level=level)

        with self._lock:
            self._notifications.insert(0, notification)

        return notification

    # -------------------------------------
    # Get All
    # -------------------------------------

    def get_all(self):

        with self._lock:
            return list(self._notifications)

    # -------------------------------------
    # Get Unread
    # -------------------------------------

    def get_unread(self):

        with self._lock:
            return [
                notification
                for notification in self._notifications
                if not notification.read
            ]

    # -------------------------------------
    # Unread Count
    # -------------------------------------

    def unread_count(self):

        with self._lock:
            return sum(
                1 for notification in self._notifications if not notification.read
            )

    # -------------------------------------
    # Mark Read
    # -------------------------------------

    def mark_read(self, notification):

        with self._lock:
            notification.read = True

    # -------------------------------------
    # Mark All Read
    # -------------------------------------

    def mark_all_read(self):

        with self._lock:
            for notification in self._notifications:
                notification.read = True

    # -------------------------------------
    # Remove
    # -------------------------------------

    def remove(self, notification):

        with self._lock:
            if notification in self._notifications:
                self._notifications.remove(notification)

    # -------------------------------------
    # Clear
    # -------------------------------------

    def clear(self):

        with self._lock:
            self._notifications.clear()


# -------------------------------------
# Global Singleton
# -------------------------------------

notification_store = NotificationStore()
