"""
tests/test_download_service.py
"""

from types import SimpleNamespace

import pytest

from services.download_service import DownloadService


class DummyTaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task.id] = task

    def remove_task(self, task_id):
        self.tasks.pop(task_id, None)

    def get_task(self, task_id):
        return self.tasks.get(task_id)

    def get_all_tasks(self):
        return list(self.tasks.values())


class DummyTaskQueue:
    def __init__(self):
        self.started = []
        self.paused = []
        self.resumed = []
        self.cancelled = []
        self.added = []

    def add(self, task):
        self.added.append(task)

    def start(self, task):
        self.started.append(task)

    def pause(self, task):
        self.paused.append(task)

    def resume(self, task):
        self.resumed.append(task)

    def cancel(self, task):
        self.cancelled.append(task)


@pytest.fixture
def service():
    manager = DummyTaskManager()
    queue = DummyTaskQueue()

    return DownloadService(manager, queue)


@pytest.fixture
def task():
    return SimpleNamespace(id=1, status="Pending")


def test_add_task(service, task):
    service.add_task(task)

    assert service.total_tasks() == 1
    assert task in service.task_queue.added


def test_remove_existing_task(service, task):
    service.add_task(task)

    assert service.remove_task(task.id) is True
    assert service.total_tasks() == 0


def test_remove_missing_task(service):
    assert service.remove_task(999) is False


def test_get_task(service, task):
    service.add_task(task)

    assert service.get_task(task.id) is task


def test_get_all_tasks(service, task):
    service.add_task(task)

    assert len(service.get_all_tasks()) == 1


def test_start(service, task):
    service.add_task(task)

    service.start(task.id)

    assert task in service.task_queue.started


def test_pause(service, task):
    service.add_task(task)

    service.pause(task.id)

    assert task in service.task_queue.paused


def test_resume(service, task):
    service.add_task(task)

    service.resume(task.id)

    assert task in service.task_queue.resumed


def test_cancel(service, task):
    service.add_task(task)

    service.cancel(task.id)

    assert task in service.task_queue.cancelled


def test_total_tasks(service):
    assert service.total_tasks() == 0


def test_running_tasks(service):
    service.add_task(SimpleNamespace(id=1, status="Running"))
    service.add_task(SimpleNamespace(id=2, status="Completed"))

    assert service.running_tasks() == 1


def test_completed_tasks(service):
    service.add_task(SimpleNamespace(id=1, status="Completed"))
    service.add_task(SimpleNamespace(id=2, status="Running"))

    assert service.completed_tasks() == 1


def test_failed_tasks(service):
    service.add_task(SimpleNamespace(id=1, status="Failed"))
    service.add_task(SimpleNamespace(id=2, status="Completed"))

    assert service.failed_tasks() == 1


def test_pause_all(service):
    t1 = SimpleNamespace(id=1, status="Pending")
    t2 = SimpleNamespace(id=2, status="Pending")

    service.add_task(t1)
    service.add_task(t2)

    service.pause_all()

    assert len(service.task_queue.paused) == 2


def test_resume_all(service):
    t1 = SimpleNamespace(id=1, status="Pending")
    t2 = SimpleNamespace(id=2, status="Pending")

    service.add_task(t1)
    service.add_task(t2)

    service.resume_all()

    assert len(service.task_queue.resumed) == 2


def test_cancel_all(service):
    t1 = SimpleNamespace(id=1, status="Pending")
    t2 = SimpleNamespace(id=2, status="Pending")

    service.add_task(t1)
    service.add_task(t2)

    service.cancel_all()

    assert len(service.task_queue.cancelled) == 2
