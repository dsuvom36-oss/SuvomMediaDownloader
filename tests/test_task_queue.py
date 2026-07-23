"""
tests/test_task_queue.py
"""

import pytest

from core.task_queue import TaskQueue


class DummyManager:
    pass


class DummyWorker:

    def __init__(self, manager, task_id, target, *args, **kwargs):
        self.manager = manager
        self.task_id = task_id
        self.target = target
        self.started = False
        self.stopped = False
        self.paused = False
        self.resumed = False
        self.alive = True

    def start(self):
        self.started = True

    def stop(self):
        self.stopped = True

    def pause(self):
        self.paused = True

    def resume(self):
        self.resumed = True

    def is_alive(self):
        return self.alive


@pytest.fixture
def queue(monkeypatch):
    monkeypatch.setattr("core.task_queue.Worker", DummyWorker)

    return TaskQueue(DummyManager(), max_workers=2)


def dummy():
    pass


def test_add(queue):
    queue.add("1", dummy)

    assert queue.running_count() == 1
    assert "1" in queue.workers


def test_running_count(queue):
    queue.add("1", dummy)

    assert queue.running_count() == 1


def test_queued_count(queue):
    queue.add("1", dummy)
    queue.add("2", dummy)
    queue.add("3", dummy)

    assert queue.running_count() == 2
    assert queue.queued_count() == 1


def test_cancel(queue):
    queue.add("1", dummy)

    queue.cancel("1")

    assert queue.workers["1"].stopped is True


def test_pause(queue):
    queue.add("1", dummy)

    queue.pause("1")

    assert queue.workers["1"].paused is True


def test_resume(queue):
    queue.add("1", dummy)

    queue.resume("1")

    assert queue.workers["1"].resumed is True


def test_cleanup_finished(queue):
    queue.add("1", dummy)

    queue.workers["1"].alive = False

    queue.update()

    assert queue.running_count() == 0


def test_start_next_after_cleanup(queue):
    queue.add("1", dummy)
    queue.add("2", dummy)
    queue.add("3", dummy)

    queue.workers["1"].alive = False

    queue.update()

    assert queue.running_count() == 2
    assert "3" in queue.workers


def test_cancel_missing(queue):
    queue.cancel("missing")


def test_pause_missing(queue):
    queue.pause("missing")


def test_resume_missing(queue):
    queue.resume("missing")
