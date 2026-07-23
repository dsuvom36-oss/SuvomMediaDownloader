"""
History Database Singleton

Provides a lazily initialized shared HistoryDatabase instance.
"""

from core.history import HistoryDatabase

_history_database = None


def get_history_database():
    """
    Returns the shared HistoryDatabase instance.
    Creates it only on first use.
    """
    global _history_database

    if _history_database is None:
        _history_database = HistoryDatabase()

    return _history_database
