import customtkinter as ctk

from core.event_bus import event_bus
from core.event_types import Event

from gui.widgets.header import Header
from gui.widgets.progress_card import ProgressCard


class DownloadsPage(ctk.CTkFrame):

    def __init__(self, master, task_manager=None, task_queue=None):
        super().__init__(master)

        self.task_manager = task_manager
        self.task_queue = task_queue

        self.cards = {}

        # ---------------------------------
        # Header
        # ---------------------------------

        header = Header(self, "📥 Downloads")
        header.pack(fill="x")

        # ---------------------------------
        # Scrollable Area
        # ---------------------------------

        self.container = ctk.CTkScrollableFrame(self)

        self.container.pack(fill="both", expand=True, padx=20, pady=20)

        self.register_events()

        self.load_existing_tasks()

    # ---------------------------------
    # Register EventBus
    # ---------------------------------

    def register_events(self):

        event_bus.subscribe(Event.TASK_ADDED, self.task_added)

        event_bus.subscribe(Event.TASK_PROGRESS, self.task_updated)

        event_bus.subscribe(Event.TASK_STARTED, self.task_updated)

        event_bus.subscribe(Event.TASK_PAUSED, self.task_updated)

        event_bus.subscribe(Event.TASK_RESUMED, self.task_updated)

        event_bus.subscribe(Event.TASK_COMPLETED, self.task_updated)

        event_bus.subscribe(Event.TASK_FAILED, self.task_updated)

        event_bus.subscribe(Event.TASK_CANCELLED, self.task_updated)

        event_bus.subscribe(Event.TASK_REMOVED, self.task_removed)

    # ---------------------------------
    # Load Existing Tasks
    # ---------------------------------

    def load_existing_tasks(self):

        if self.task_manager is None:
            return

        for task in self.task_manager.get_all_tasks():
            self.create_card(task)

    # ---------------------------------
    # Create Card
    # ---------------------------------

    def create_card(self, task):

        if task.id in self.cards:
            return

        card = ProgressCard(
            self.container,
            task,
            on_pause=self.task_queue.pause if self.task_queue else None,
            on_resume=self.task_queue.resume if self.task_queue else None,
            on_cancel=self.task_queue.cancel if self.task_queue else None,
        )

        card.pack(fill="x", padx=10, pady=8)

        self.cards[task.id] = card

    # ---------------------------------
    # Event: Task Added
    # ---------------------------------

    def task_added(self, task=None, **kwargs):

        if task is None:
            task = kwargs.get("task")

        if task:
            self.create_card(task)

    # ---------------------------------
    # Event: Task Updated
    # ---------------------------------

    def task_updated(self, task=None, **kwargs):

        if task is None:
            task = kwargs.get("task")

        if task is None:
            return

        card = self.cards.get(task.id)

        if card:
            card.refresh()

    # ---------------------------------
    # Event: Task Removed
    # ---------------------------------

    def task_removed(self, task=None, **kwargs):

        if task is None:
            task = kwargs.get("task")

        if task is None:
            return

        card = self.cards.pop(task.id, None)

        if card:
            card.destroy()

    # ---------------------------------
    # Cleanup
    # ---------------------------------

    def destroy(self):

        event_bus.unsubscribe(Event.TASK_ADDED, self.task_added)
        event_bus.unsubscribe(Event.TASK_PROGRESS, self.task_updated)
        event_bus.unsubscribe(Event.TASK_STARTED, self.task_updated)
        event_bus.unsubscribe(Event.TASK_PAUSED, self.task_updated)
        event_bus.unsubscribe(Event.TASK_RESUMED, self.task_updated)
        event_bus.unsubscribe(Event.TASK_COMPLETED, self.task_updated)
        event_bus.unsubscribe(Event.TASK_FAILED, self.task_updated)
        event_bus.unsubscribe(Event.TASK_CANCELLED, self.task_updated)
        event_bus.unsubscribe(Event.TASK_REMOVED, self.task_removed)

        super().destroy()
