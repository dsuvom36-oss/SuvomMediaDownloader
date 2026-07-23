"""
services/download_service.py

High-level service for managing download tasks.
"""

from core.task_manager import TaskManager
from core.task_queue import TaskQueue
from core.event_bus import event_bus
from core.event_types import Event


class DownloadService:

    def __init__(self, task_manager: TaskManager, task_queue: TaskQueue):

        self.task_manager = task_manager
        self.task_queue = task_queue

    # --------------------------------------------------
    # Task Management
    # --------------------------------------------------

    def add_task(self, task):
        """
        Add a task and enqueue it.
        """

        self.task_manager.add_task(task)
        self.task_queue.add(task)

        return task

    def remove_task(self, task_id):

        task = self.task_manager.get_task(task_id)

        if task is None:
            return False

        self.task_manager.remove_task(task_id)

        return True

    def get_task(self, task_id):

        return self.task_manager.get_task(task_id)

    def get_all_tasks(self):

        return self.task_manager.get_all_tasks()

    # --------------------------------------------------
    # Queue Controls
    # --------------------------------------------------

    def start(self, task_id):

        task = self.task_manager.get_task(task_id)

        if task:
            self.task_queue.start(task)

    def pause(self, task_id):

        task = self.task_manager.get_task(task_id)

        if task:
            self.task_queue.pause(task)

    def resume(self, task_id):

        task = self.task_manager.get_task(task_id)

        if task:
            self.task_queue.resume(task)

    def cancel(self, task_id):

        task = self.task_manager.get_task(task_id)

        if task:
            self.task_queue.cancel(task)

    # --------------------------------------------------
    # Bulk Operations
    # --------------------------------------------------

    def pause_all(self):

        for task in self.get_all_tasks():
            self.pause(task.id)

    def resume_all(self):

        for task in self.get_all_tasks():
            self.resume(task.id)

    def cancel_all(self):

        for task in self.get_all_tasks():
            self.cancel(task.id)

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def total_tasks(self):

        return len(self.get_all_tasks())

    def running_tasks(self):

        return len(
            [
                task
                for task in self.get_all_tasks()
                if getattr(task, "status", None) == "Running"
            ]
        )

    def completed_tasks(self):

        return len(
            [
                task
                for task in self.get_all_tasks()
                if getattr(task, "status", None) == "Completed"
            ]
        )

    def failed_tasks(self):

        return len(
            [
                task
                for task in self.get_all_tasks()
                if getattr(task, "status", None) == "Failed"
            ]
        )


download_service = None


def initialize_download_service(task_manager, task_queue):
    """
    Initialize the global DownloadService instance.
    """

    global download_service

    download_service = DownloadService(task_manager, task_queue)

    event_bus.publish(Event.QUEUE_UPDATED)

    return download_service
