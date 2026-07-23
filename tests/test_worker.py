"""
tests/test_worker.py
"""

import pytest

from core.worker import Worker
from core.task_manager import TaskStatus


class DummyTask:
    def __init__(self):
        self.id = "task-1"


class DummyTaskManager:

    def __init__(self):
        self.status_calls = []
        self.progress_calls = []

    def set_status(self, task_id, status, message=""):
        self.status_calls.append((task_id, status, message))

    def update_progress(self, task_id, progress, message=""):
        self.progress_calls.append((task_id, progress, message))


@pytest.fixture
def task():
    return DummyTask()


@pytest.fixture
def manager():
    return DummyTaskManager()


def test_successful_run(task, manager):

    called = {"value": False}

    def work_function(worker, task):
        called["value"] = True

    worker = Worker(task, manager, work_function)

    worker.run()

    assert called["value"] is True
    assert manager.status_calls[0][1] == TaskStatus.RUNNING
    assert manager.status_calls[-1][1] == TaskStatus.COMPLETED


def test_failed_run(task, manager):

    def work_function(worker, task):
        raise RuntimeError("failure")

    worker = Worker(task, manager, work_function)

    worker.run()

    assert manager.status_calls[-1][1] == TaskStatus.FAILED
    assert "failure" in manager.status_calls[-1][2]


def test_update_progress(task, manager):

    worker = Worker(task, manager, lambda **kwargs: None)

    worker.update_progress(55, "Downloading")

    assert manager.progress_calls == [("task-1", 55, "Downloading")]


def test_pause(task, manager):

    worker = Worker(task, manager, lambda **kwargs: None)

    worker.pause()

    assert manager.status_calls[-1][1] == TaskStatus.PAUSED


def test_resume(task, manager):

    worker = Worker(task, manager, lambda **kwargs: None)

    worker.resume()

    assert manager.status_calls[-1][1] == TaskStatus.RUNNING


def test_stop(task, manager):

    worker = Worker(task, manager, lambda **kwargs: None)

    worker.stop()

    assert worker.is_cancelled() is True
    assert manager.status_calls[-1][1] == TaskStatus.CANCELLED


def test_is_cancelled_initial(task, manager):

    worker = Worker(task, manager, lambda **kwargs: None)

    assert worker.is_cancelled() is False


def test_cancelled_run_not_completed(task, manager):

    def work_function(worker, task):
        worker.stop()

    worker = Worker(task, manager, work_function)

    worker.run()

    statuses = [status for _, status, _ in manager.status_calls]

    assert TaskStatus.CANCELLED in statuses
    assert TaskStatus.COMPLETED not in statuses


def test_multiple_pause_resume(task, manager):

    worker = Worker(task, manager, lambda **kwargs: None)

    worker.pause()
    worker.resume()
    worker.pause()
    worker.resume()

    statuses = [status for _, status, _ in manager.status_calls]

    assert statuses.count(TaskStatus.PAUSED) == 2
    assert statuses.count(TaskStatus.RUNNING) == 2
