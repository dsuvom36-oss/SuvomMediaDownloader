"""
tests/test_container.py
"""

import pytest

from services.container import ServiceContainer


class DummyTaskManager:
    pass


class DummyTaskQueue:
    def __init__(self, manager):
        self.manager = manager


class DummyDownloadService:
    def __init__(self, manager, queue):
        self.manager = manager
        self.queue = queue


class DummyHistoryService:
    pass


class DummyNotificationService:
    pass


class DummySettingsService:
    pass


@pytest.fixture
def container(monkeypatch):

    monkeypatch.setattr(
        "services.container.TaskManager",
        DummyTaskManager,
    )

    monkeypatch.setattr(
        "services.container.TaskQueue",
        DummyTaskQueue,
    )

    monkeypatch.setattr(
        "services.container.DownloadService",
        DummyDownloadService,
    )

    monkeypatch.setattr(
        "services.container.get_history_service",
        lambda: DummyHistoryService(),
    )

    monkeypatch.setattr(
        "services.container.get_notification_service",
        lambda: DummyNotificationService(),
    )

    monkeypatch.setattr(
        "services.container.get_settings_service",
        lambda: DummySettingsService(),
    )

    return ServiceContainer()


def test_task_manager(container):
    assert isinstance(container.task_manager, DummyTaskManager)


def test_task_queue(container):
    assert isinstance(container.task_queue, DummyTaskQueue)


def test_download_service(container):
    assert isinstance(container.download_service, DummyDownloadService)


def test_history_service(container):
    assert isinstance(container.history_service, DummyHistoryService)


def test_notification_service(container):
    assert isinstance(container.notification_service, DummyNotificationService)


def test_settings_service(container):
    assert isinstance(container.settings_service, DummySettingsService)


def test_get_download_service(container):
    assert container.get("download_service") is container.download_service


def test_get_history_service(container):
    assert container.get("history_service") is container.history_service


def test_services_dictionary(container):

    services = container.services()

    assert "task_manager" in services
    assert "task_queue" in services
    assert "download_service" in services
    assert "history_service" in services
    assert "notification_service" in services
    assert "settings_service" in services


def test_services_count(container):
    assert len(container.services()) == 6
