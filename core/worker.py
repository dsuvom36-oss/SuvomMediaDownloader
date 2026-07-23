from threading import Thread, Event
import time

from core.task_manager import TaskStatus


class Worker(Thread):

    def __init__(self, task, task_manager, work_function):
        super().__init__(daemon=True)

        self.task = task
        self.task_manager = task_manager
        self.work_function = work_function

        self._pause = Event()
        self._pause.set()

        self._stop = Event()

    # ==========================================

    def run(self):

        try:

            self.task_manager.set_status(self.task.id, TaskStatus.RUNNING)

            self.work_function(worker=self, task=self.task)

            if not self._stop.is_set():

                self.task_manager.set_status(self.task.id, TaskStatus.COMPLETED)

        except Exception as e:

            self.task_manager.set_status(self.task.id, TaskStatus.FAILED, str(e))

    # ==========================================

    def update_progress(self, progress, message=""):

        self.task_manager.update_progress(self.task.id, progress, message)

    # ==========================================

    def wait_if_paused(self):

        while not self._pause.is_set():

            if self._stop.is_set():
                return

            time.sleep(0.1)

    # ==========================================

    def pause(self):

        self._pause.clear()

        self.task_manager.set_status(self.task.id, TaskStatus.PAUSED)

    # ==========================================

    def resume(self):

        self._pause.set()

        self.task_manager.set_status(self.task.id, TaskStatus.RUNNING)

    # ==========================================

    def stop(self):

        self._stop.set()

        self._pause.set()

        self.task_manager.set_status(self.task.id, TaskStatus.CANCELLED)

    # ==========================================

    def is_cancelled(self):

        return self._stop.is_set()
