from collections import defaultdict
from threading import Lock
from typing import Callable


class EventBus:
    """
    A simple thread-safe publish/subscribe event bus.
    """

    def __init__(self):
        self._listeners = defaultdict(list)
        self._lock = Lock()

    # ==========================================
    # Subscribe
    # ==========================================

    def subscribe(self, event_name: str, callback: Callable):

        with self._lock:

            if callback not in self._listeners[event_name]:
                self._listeners[event_name].append(callback)

    # ==========================================
    # Unsubscribe
    # ==========================================

    def unsubscribe(self, event_name: str, callback: Callable):

        with self._lock:

            if callback in self._listeners[event_name]:
                self._listeners[event_name].remove(callback)

    # ==========================================
    # Publish Event
    # ==========================================

    def publish(self, event_name: str, **kwargs):

        with self._lock:
            listeners = list(self._listeners.get(event_name, []))

        for callback in listeners:

            try:
                callback(**kwargs)

            except Exception as error:
                print(f"[EventBus] Error handling '{event_name}': {error}")

    # ==========================================
    # Remove All Listeners
    # ==========================================

    def clear(self):

        with self._lock:
            self._listeners.clear()

    # ==========================================
    # Get Listener Count
    # ==========================================

    def listener_count(self, event_name: str):

        with self._lock:
            return len(self._listeners.get(event_name, []))

    # ==========================================
    # List Registered Events
    # ==========================================

    def registered_events(self):

        with self._lock:
            return list(self._listeners.keys())


# ==========================================
# Global Shared Event Bus
# ==========================================

event_bus = EventBus()
