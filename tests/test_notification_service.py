"""
tests/test_notification_service.py
"""

import pytest

from services.notification_service import NotificationService
from core.notification_store import Notification


class DummyStore:
    def __init__(self):
        self.notifications = []

    def add(self, title, message, level="info"):
        notification = Notification(
            title=title,
            message=message,
            level=level,
        )
        self.notifications.insert(0, notification)
        return notification

    def get_all(self):
        return list(self.notifications)

    def get_unread(self):
        return [n for n in self.notifications if not n.read]

    def unread_count(self):
        return len(self.get_unread())

    def mark_read(self, notification):
        notification.read = True

    def mark_all_read(self):
        for notification in self.notifications:
            notification.read = True

    def remove(self, notification):
        if notification in self.notifications:
            self.notifications.remove(notification)

    def clear(self):
        self.notifications.clear()


@pytest.fixture
def service(monkeypatch):
    store = DummyStore()

    monkeypatch.setattr(
        "services.notification_service.notification_store",
        store,
    )

    monkeypatch.setattr(
        "services.notification_service.event_bus.publish",
        lambda *args, **kwargs: None,
    )

    return NotificationService()


def test_add(service):
    n = service.add("Title", "Message")

    assert n.title == "Title"
    assert service.total_count() == 1


def test_remove(service):
    n = service.add("Title", "Message")

    service.remove(n)

    assert service.total_count() == 0


def test_mark_read(service):
    n = service.add("Title", "Message")

    service.mark_read(n)

    assert n.read is True


def test_mark_all_read(service):
    service.add("A", "A")
    service.add("B", "B")

    assert service.unread_count() == 2

    count = service.mark_all_read()

    assert count == 2
    assert service.unread_count() == 0


def test_clear(service):
    service.add("A", "A")
    service.add("B", "B")

    service.clear()

    assert service.total_count() == 0


def test_get_all(service):
    service.add("A", "A")

    assert len(service.get_all()) == 1


def test_unread(service):
    service.add("A", "A")

    assert len(service.unread()) == 1


def test_read(service):
    n = service.add("A", "A")

    service.mark_read(n)

    assert len(service.read()) == 1


def test_total_count(service):
    service.add("A", "A")
    service.add("B", "B")

    assert service.total_count() == 2


def test_unread_count(service):
    service.add("A", "A")

    assert service.unread_count() == 1


def test_read_count(service):
    n = service.add("A", "A")

    service.mark_read(n)

    assert service.read_count() == 1


def test_has_unread(service):
    assert service.has_unread() is False

    service.add("A", "A")

    assert service.has_unread() is True
