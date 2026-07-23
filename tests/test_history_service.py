"""
tests/test_history_service.py
"""

import pytest

from services.history_service import HistoryService


class DummyTask:
    def __init__(self, status="Completed"):
        self.status = status


class DummyDatabase:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        return True

    def delete(self, history_id):
        return True

    def clear(self):
        self.tasks.clear()
        return True

    def get_all(self):
        return self.tasks

    def search(self, keyword):
        return [
            task
            for task in self.tasks
            if keyword.lower() in getattr(task, "status", "").lower()
        ]

    def export_csv(self, filename):
        return True


@pytest.fixture
def service(monkeypatch):
    db = DummyDatabase()

    monkeypatch.setattr(
        "services.history_service.get_history_database",
        lambda: db,
    )

    monkeypatch.setattr(
        "services.history_service.event_bus.publish",
        lambda *args, **kwargs: None,
    )

    return HistoryService()


def test_add(service):
    task = DummyTask()

    assert service.add(task) is True
    assert service.count() == 1


def test_delete(service):
    assert service.delete(1) is True


def test_clear(service):
    service.add(DummyTask())

    assert service.count() == 1

    service.clear()

    assert service.count() == 0


def test_get_all(service):
    service.add(DummyTask())

    assert len(service.get_all()) == 1


def test_search(service):
    service.add(DummyTask(status="Completed"))

    result = service.search("Completed")

    assert len(result) == 1


def test_export_csv(service):
    assert service.export_csv("history.csv") is True


def test_completed(service):
    service.add(DummyTask("Completed"))
    service.add(DummyTask("Failed"))

    assert service.completed() == 1


def test_failed(service):
    service.add(DummyTask("Completed"))
    service.add(DummyTask("Failed"))

    assert service.failed() == 1


def test_cancelled(service):
    service.add(DummyTask("Cancelled"))
    service.add(DummyTask("Completed"))

    assert service.cancelled() == 1


def test_count(service):
    service.add(DummyTask())
    service.add(DummyTask())

    assert service.count() == 2
