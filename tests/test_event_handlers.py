"""
tests/test_event_handlers.py
"""

import pytest

from core.event_bus import EventBus


@pytest.fixture
def bus():
    return EventBus()


def test_subscribe_publish():
    """Subscriber receives published keyword data."""

    bus = EventBus()

    received = []

    def listener(message):
        received.append(message)

    bus.subscribe("test_event", listener)

    bus.publish("test_event", message="Hello")

    assert received == ["Hello"]


def test_multiple_subscribers():
    """Multiple subscribers receive the same event."""

    bus = EventBus()

    first = []
    second = []

    bus.subscribe("event", lambda value: first.append(value))
    bus.subscribe("event", lambda value: second.append(value))

    bus.publish("event", value=123)

    assert first == [123]
    assert second == [123]


def test_unsubscribe():
    """Unsubscribed listener should not receive events."""

    bus = EventBus()

    received = []

    def listener(message):
        received.append(message)

    bus.subscribe("event", listener)
    bus.unsubscribe("event", listener)

    bus.publish("event", message="hello")

    assert received == []


def test_publish_without_subscribers():
    """Publishing an event with no subscribers should not raise."""

    bus = EventBus()

    bus.publish("unknown_event", test=True)


def test_multiple_events():
    """Subscribers receive only the events they subscribed to."""

    bus = EventBus()

    event_a = []
    event_b = []

    bus.subscribe("A", lambda value: event_a.append(value))
    bus.subscribe("B", lambda value: event_b.append(value))

    bus.publish("A", value=1)
    bus.publish("B", value=2)

    assert event_a == [1]
    assert event_b == [2]


def test_same_callback_multiple_events():
    """One callback can subscribe to multiple events."""

    bus = EventBus()

    received = []

    def listener(value):
        received.append(value)

    bus.subscribe("A", listener)
    bus.subscribe("B", listener)

    bus.publish("A", value="one")
    bus.publish("B", value="two")

    assert received == ["one", "two"]


def test_publish_none():
    """Publishing None should work."""

    bus = EventBus()

    received = []

    bus.subscribe("event", lambda value: received.append(value))

    bus.publish("event", value=None)

    assert received == [None]
