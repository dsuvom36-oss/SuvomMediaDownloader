import customtkinter as ctk

from core.event_bus import event_bus
from core.event_types import Event


class HomePage(ctk.CTkFrame):

    def __init__(self, parent, task_manager):

        super().__init__(parent)

        self.task_manager = task_manager

        # ==========================================
        # UI
        # ==========================================

        self.build_ui()

        # Load initial statistics
        self.update_statistics(self.task_manager.get_statistics())

        # Register EventBus listeners
        self.register_events()

    # ==========================================
    # Build UI
    # ==========================================

    def build_ui(self):

        title = ctk.CTkLabel(self, text="Dashboard", font=("Segoe UI", 28, "bold"))

        title.pack(pady=(20, 10))

        self.total_label = ctk.CTkLabel(
            self, text="Total Tasks : 0", font=("Segoe UI", 18)
        )

        self.total_label.pack(pady=5)

        self.running_label = ctk.CTkLabel(
            self, text="Running : 0", font=("Segoe UI", 18)
        )

        self.running_label.pack(pady=5)

        self.completed_label = ctk.CTkLabel(
            self, text="Completed : 0", font=("Segoe UI", 18)
        )

        self.completed_label.pack(pady=5)

        self.failed_label = ctk.CTkLabel(self, text="Failed : 0", font=("Segoe UI", 18))

        self.failed_label.pack(pady=5)

        self.queued_label = ctk.CTkLabel(self, text="Queued : 0", font=("Segoe UI", 18))

        self.queued_label.pack(pady=5)

    # ==========================================
    # Event Registration
    # ==========================================

    def register_events(self):

        events = [
            Event.TASK_ADDED,
            Event.TASK_STARTED,
            Event.TASK_COMPLETED,
            Event.TASK_FAILED,
            Event.TASK_CANCELLED,
            Event.TASK_REMOVED,
        ]

        for event in events:

            event_bus.subscribe(event, self.on_task_changed)

    # ==========================================
    # Event Callback
    # ==========================================

    def on_task_changed(self, **kwargs):

        self.refresh_dashboard()

    # ==========================================
    # Refresh Dashboard
    # ==========================================

    def refresh_dashboard(self):

        stats = self.task_manager.get_statistics()

        self.update_statistics(stats)

    # ==========================================
    # Update Statistics
    # ==========================================

    def update_statistics(self, stats):

        self.total_label.configure(text=f"Total Tasks : {stats['total']}")

        self.running_label.configure(text=f"Running : {stats['running']}")

        self.completed_label.configure(text=f"Completed : {stats['completed']}")

        self.failed_label.configure(text=f"Failed : {stats['failed']}")

        self.queued_label.configure(text=f"Queued : {stats['queued']}")

    # ==========================================
    # Cleanup
    # ==========================================

    def destroy(self):

        events = [
            Event.TASK_ADDED,
            Event.TASK_STARTED,
            Event.TASK_COMPLETED,
            Event.TASK_FAILED,
            Event.TASK_CANCELLED,
            Event.TASK_REMOVED,
        ]

        for event in events:

            event_bus.unsubscribe(event, self.on_task_changed)

        super().destroy()
