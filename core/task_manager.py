from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from threading import Lock
import uuid

from core.event_bus import event_bus
from core.event_types import Event

# ==========================================
# Task Status
# ==========================================


class TaskStatus(str, Enum):

    QUEUED = "Queued"
    RUNNING = "Running"
    PAUSED = "Paused"
    COMPLETED = "Completed"
    FAILED = "Failed"
    CANCELLED = "Cancelled"


# ==========================================
# Task
# ==========================================


@dataclass
class Task:

    name: str

    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    status: TaskStatus = TaskStatus.QUEUED

    progress: int = 0

    message: str = ""

    created_at: datetime = field(default_factory=datetime.now)

    started_at: datetime | None = None

    finished_at: datetime | None = None


# ==========================================
# Task Manager
# ==========================================


class TaskManager:

    def __init__(self):

        self.tasks = {}

        self._lock = Lock()

    # ======================================

    def add_task(self, task):

        with self._lock:

            self.tasks[task.id] = task

        event_bus.publish(Event.TASK_ADDED, task=task)

        return task

    # ======================================

    def get_task(self, task_id):

        with self._lock:

            return self.tasks.get(task_id)

    # ======================================

    def get_all_tasks(self):

        with self._lock:

            return list(self.tasks.values())

    # ======================================

    def update_progress(self, task_id, progress, message=""):

        task = self.get_task(task_id)

        if task is None:
            return

        task.progress = progress

        task.message = message

        event_bus.publish(
            Event.TASK_PROGRESS, task=task, progress=progress, message=message
        )

    # ======================================

    def set_status(self, task_id, status, message=""):

        task = self.get_task(task_id)

        if task is None:
            return

        task.status = status

        task.message = message

        now = datetime.now()

        if status == TaskStatus.RUNNING:

            if task.started_at is None:
                task.started_at = now

            event_bus.publish(Event.TASK_STARTED, task=task)

        elif status == TaskStatus.PAUSED:

            event_bus.publish(Event.TASK_PAUSED, task=task)

        elif status == TaskStatus.COMPLETED:

            task.progress = 100

            task.finished_at = now

            event_bus.publish(Event.TASK_COMPLETED, task=task)

        elif status == TaskStatus.FAILED:

            task.finished_at = now

            event_bus.publish(Event.TASK_FAILED, task=task)

        elif status == TaskStatus.CANCELLED:

            task.finished_at = now

            event_bus.publish(Event.TASK_CANCELLED, task=task)

    # ======================================

    def remove_task(self, task_id):

        task = self.get_task(task_id)

        if task is None:
            return

        event_bus.publish(Event.TASK_REMOVED, task=task)

        with self._lock:

            self.tasks.pop(task_id, None)

    # ======================================

    def get_statistics(self):

        stats = {
            "total": 0,
            "queued": 0,
            "running": 0,
            "paused": 0,
            "completed": 0,
            "failed": 0,
            "cancelled": 0,
        }

        with self._lock:

            stats["total"] = len(self.tasks)

            for task in self.tasks.values():

                if task.status == TaskStatus.QUEUED:
                    stats["queued"] += 1

                elif task.status == TaskStatus.RUNNING:
                    stats["running"] += 1

                elif task.status == TaskStatus.PAUSED:
                    stats["paused"] += 1

                elif task.status == TaskStatus.COMPLETED:
                    stats["completed"] += 1

                elif task.status == TaskStatus.FAILED:
                    stats["failed"] += 1

                elif task.status == TaskStatus.CANCELLED:
                    stats["cancelled"] += 1

        return stats
