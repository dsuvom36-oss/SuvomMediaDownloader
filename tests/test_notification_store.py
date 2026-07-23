"""
tests/test_notification_store.py
"""

from core.notification_store import NotificationStore


def test_add_notification():
    store = NotificationStore()

    notification = store.add("Title", "Message", "info")

    assert notification.title == "Title"
    assert notification.message == "Message"
    assert notification.level == "info"


def test_get_all():
    store = NotificationStore()

    store.add("A", "B")

    assert len(store.get_all()) == 1


def test_get_unread():
    store = NotificationStore()

    store.add("A", "B")

    assert len(store.get_unread()) == 1


def test_unread_count():
    store = NotificationStore()

    store.add("A", "B")
    store.add("C", "D")

    assert store.unread_count() == 2


def test_mark_read():
    store = NotificationStore()

    notification = store.add("A", "B")

    store.mark_read(notification)

    assert notification.read is True


def test_mark_all_read():
    store = NotificationStore()

    store.add("A", "B")
    store.add("C", "D")

    store.mark_all_read()

    assert store.unread_count() == 0


def test_remove():
    store = NotificationStore()

    notification = store.add("A", "B")

    store.remove(notification)

    assert len(store.get_all()) == 0


def test_clear():
    store = NotificationStore()

    store.add("A", "B")
    store.add("C", "D")

    store.clear()

    assert len(store.get_all()) == 0


def test_order():
    store = NotificationStore()

    first = store.add("First", "1")
    second = store.add("Second", "2")

    notifications = store.get_all()

    assert notifications[0] == second
    assert notifications[1] == first


def test_read_after_mark_all():
    store = NotificationStore()

    store.add("A", "B")
    store.add("C", "D")

    store.mark_all_read()

    assert len(store.get_unread()) == 0
