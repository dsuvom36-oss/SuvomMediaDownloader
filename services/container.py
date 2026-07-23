"""
services/container.py

Dependency Injection (DI) Container
"""

from core.task_manager import TaskManager
from core.task_queue import TaskQueue

from services.download_service import DownloadService
from services.history_service import get_history_service
from services.notification_service import get_notification_service
from services.settings_service import get_settings_service


class ServiceContainer:

    def __init__(self):

        # =====================================
        # Core
        # =====================================

        self.task_manager = TaskManager()

        self.task_queue = TaskQueue(self.task_manager)

        # =====================================
        # Services
        # =====================================

        self.download_service = DownloadService(self.task_manager, self.task_queue)

        self.history_service = get_history_service()

        self.notification_service = get_notification_service()

        self.settings_service = get_settings_service()

    # =====================================
    # Get Service
    # =====================================

    def get(self, name):

        return getattr(self, name)

    # =====================================
    # Dictionary
    # =====================================

    def services(self):

        return {
            "task_manager": self.task_manager,
            "task_queue": self.task_queue,
            "download_service": self.download_service,
            "history_service": self.history_service,
            "notification_service": self.notification_service,
            "settings_service": self.settings_service,
        }


# ==========================================
# Lazy Global Container
# ==========================================

_container = None


def get_container():
    """
    Returns the shared ServiceContainer instance.
    Creates it only when first requested.
    """
    global _container

    if _container is None:
        _container = ServiceContainer()

    return _container
