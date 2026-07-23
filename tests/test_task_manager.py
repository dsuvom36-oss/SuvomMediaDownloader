"""
tests/test_task_manager.py
"""

import pytest

from core.task_manager import (
    Task,
    TaskManager,
    TaskStatus,
)


@pytest.fixture
def manager(monkeypatch):

    monkeypatch.setattr(
        "core.task_manager.event_bus.publish",
        lambda *args, **kwargs: None,
    )

    return TaskManager()


@pytest.fixture
def task():
    return Task(name="Test Task")


def test_add_task(manager, task):
    manager.add_task(task)

    assert manager.get_task(task.id) is task


def test_get_task(manager, task):
    manager.add_task(task)

    assert manager.get_task(task.id) == task


def test_get_missing_task(manager):
    assert manager.get_task("missing") is None


def test_get_all_tasks(manager):
    manager.add_task(Task("A"))
    manager.add_task(Task("B"))

    assert len(manager.get_all_tasks()) == 2


def test_update_progress(manager, task):
    manager.add_task(task)

    manager.update_progress(task.id, 50, "Halfway")

    assert task.progress == 50
    assert task.message == "Halfway"


def test_set_running(manager, task):
    manager.add_task(task)

    manager.set_status(task.id, TaskStatus.RUNNING)

    assert task.status == TaskStatus.RUNNING
    assert task.started_at is not None


def test_set_paused(manager, task):
    manager.add_task(task)

    manager.set_status(task.id, TaskStatus.PAUSED)

    assert task.status == TaskStatus.PAUSED


def test_set_completed(manager, task):
    manager.add_task(task)

    manager.set_status(task.id, TaskStatus.COMPLETED)

    assert task.status == TaskStatus.COMPLETED
    assert task.progress == 100
    assert task.finished_at is not None


def test_set_failed(manager, task):
    manager.add_task(task)

    manager.set_status(task.id, TaskStatus.FAILED)

    assert task.status == TaskStatus.FAILED
    assert task.finished_at is not None


def test_set_cancelled(manager, task):
    manager.add_task(task)

    manager.set_status(task.id, TaskStatus.CANCELLED)

    assert task.status == TaskStatus.CANCELLED
    assert task.finished_at is not None


def test_remove_task(manager, task):
    manager.add_task(task)

    manager.remove_task(task.id)

    assert manager.get_task(task.id) is None


def test_remove_missing_task(manager):
    manager.remove_task("missing")

    assert manager.get_all_tasks() == []


def test_statistics_empty(manager):
    stats = manager.get_statistics()

    assert stats["total"] == 0
    assert stats["queued"] == 0


def test_statistics(manager):
    tasks = [
        Task("Queued"),
        Task("Running"),
        Task("Paused"),
        Task("Completed"),
        Task("Failed"),
        Task("Cancelled"),
    ]

    statuses = [
        TaskStatus.QUEUED,
        TaskStatus.RUNNING,
        TaskStatus.PAUSED,
        TaskStatus.COMPLETED,
        TaskStatus.FAILED,
        TaskStatus.CANCELLED,
    ]

    for task, status in zip(tasks, statuses):
        task.status = status
        manager.add_task(task)

    stats = manager.get_statistics()

    assert stats["total"] == 6
    assert stats["queued"] == 1
    assert stats["running"] == 1
    assert stats["paused"] == 1
    assert stats["completed"] == 1
    assert stats["failed"] == 1
    assert stats["cancelled"] == 1
