"""
services/notification_service.py

Notification Service
"""

from core.notification_store import notification_store
from core.event_bus import event_bus
from core.event_types import Event


class NotificationService:

    def __init__(self):
        self.store = notification_store

    # ==================================================
    # Add Notification
    # ==================================================

    def add(self, title, message, level="info"):

        notification = self.store.add(
            title=title,
            message=message,
            level=level,
        )

        event_bus.publish(
            Event.NOTIFICATION_ADDED,
            notification=notification,
        )

        return notification

    # ==================================================
    # Remove Notification
    # ==================================================

    def remove(self, notification):

        self.store.remove(notification)

        event_bus.publish(
            Event.NOTIFICATION_CLEARED,
            notification=notification,
        )

        return notification

    # ==================================================
    # Mark Read
    # ==================================================

    def mark_read(self, notification):

        self.store.mark_read(notification)

        event_bus.publish(
            Event.NOTIFICATION_READ,
            notification=notification,
        )

        return notification

    # ==================================================
    # Mark All Read
    # ==================================================

    def mark_all_read(self):

        unread = self.store.get_unread()

        for notification in unread:
            self.store.mark_read(notification)

        if unread:
            event_bus.publish(Event.NOTIFICATION_READ)

        return len(unread)

    # ==================================================
    # Clear All
    # ==================================================

    def clear(self):

        self.store.clear()

        event_bus.publish(Event.NOTIFICATION_CLEARED)

    # ==================================================
    # Get Notifications
    # ==================================================

    def get_all(self):
        return self.store.get_all()

    def unread(self):
        return self.store.get_unread()

    def read(self):
        return [notification for notification in self.get_all() if notification.read]

    # ==================================================
    # Statistics
    # ==================================================

    def total_count(self):
        return len(self.get_all())

    def unread_count(self):
        return self.store.unread_count()

    def read_count(self):
        return len(self.read())

    # ==================================================
    # Helpers
    # ==================================================

    def has_unread(self):
        return self.unread_count() > 0


# ==================================================
# Lazy Singleton
# ==================================================

_notification_service = None


def get_notification_service():
    """
    Returns the shared NotificationService instance.
    Creates it only when first requested.
    """
    global _notification_service

    if _notification_service is None:
        _notification_service = NotificationService()

    return _notification_service
