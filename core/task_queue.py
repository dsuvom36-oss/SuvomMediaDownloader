from queue import Queue
from threading import Lock

from core.worker import Worker
from core.task_manager import TaskManager


class TaskQueue:

    def __init__(self, manager: TaskManager, max_workers=3):

        self.manager = manager

        self.max_workers = max_workers

        self.queue = Queue()

        self.workers = {}

        self.lock = Lock()

    # ----------------------------

    def add(self, task_id, target, *args, **kwargs):

        self.queue.put((task_id, target, args, kwargs))

        self._start_next()

    # ----------------------------

    def _start_next(self):

        with self.lock:

            self._cleanup_finished()

            while len(self.workers) < self.max_workers and not self.queue.empty():

                task_id, target, args, kwargs = self.queue.get()

                worker = Worker(self.manager, task_id, target, *args, **kwargs)

                self.workers[task_id] = worker

                worker.start()

    # ----------------------------

    def _cleanup_finished(self):

        finished = []

        for task_id, worker in self.workers.items():

            if not worker.is_alive():

                finished.append(task_id)

        for task_id in finished:

            del self.workers[task_id]

    # ----------------------------

    def update(self):

        self._start_next()

    # ----------------------------

    def cancel(self, task_id):

        worker = self.workers.get(task_id)

        if worker:

            worker.stop()

    # ----------------------------

    def pause(self, task_id):

        worker = self.workers.get(task_id)

        if worker:

            worker.pause()

    # ----------------------------

    def resume(self, task_id):

        worker = self.workers.get(task_id)

        if worker:

            worker.resume()

    # ----------------------------

    def running_count(self):

        self._cleanup_finished()

        return len(self.workers)

    # ----------------------------

    def queued_count(self):

        return self.queue.qsize()
