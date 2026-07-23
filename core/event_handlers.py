from core.event_bus import event_bus
from core.event_types import Event

from core.activity_log import activity_log
from core.notification_store import notification_store
from core.history_service import history_database


class EventHandlers:

    def __init__(self):
        self.register()

    # ==================================================
    # Register Events
    # ==================================================

    def register(self):

        # Application
        event_bus.subscribe(Event.APPLICATION_STARTED, self.application_started)
        event_bus.subscribe(Event.APPLICATION_CLOSED, self.application_closed)

        # Tasks
        event_bus.subscribe(Event.TASK_ADDED, self.task_added)
        event_bus.subscribe(Event.TASK_STARTED, self.task_started)
        event_bus.subscribe(Event.TASK_PROGRESS, self.task_progress)
        event_bus.subscribe(Event.TASK_COMPLETED, self.task_completed)
        event_bus.subscribe(Event.TASK_FAILED, self.task_failed)
        event_bus.subscribe(Event.TASK_CANCELLED, self.task_cancelled)
        event_bus.subscribe(Event.TASK_REMOVED, self.task_removed)

        # History
        event_bus.subscribe(Event.HISTORY_ADDED, self.history_added)
        event_bus.subscribe(Event.HISTORY_DELETED, self.history_deleted)
        event_bus.subscribe(Event.HISTORY_CLEARED, self.history_cleared)
        event_bus.subscribe(Event.HISTORY_EXPORTED, self.history_exported)

        # Settings
        event_bus.subscribe(Event.SETTINGS_LOADED, self.settings_loaded)
        event_bus.subscribe(Event.SETTINGS_SAVED, self.settings_saved)

        # Errors
        event_bus.subscribe(Event.ERROR_OCCURRED, self.error_occurred)

    # ==================================================
    # Application
    # ==================================================

    def application_started(self):

        activity_log.add(
            "Application Started", "Application started successfully.", "System"
        )

        notification_store.add("Application", "Application started.", "success")

    def application_closed(self):

        activity_log.add("Application Closed", "Application closed.", "System")

    # ==================================================
    # Task Events
    # ==================================================

    def task_added(self, task):

        activity_log.add("Task Added", task.name, "Task")

    def task_started(self, task):

        activity_log.add("Task Started", task.name, "Task")

        notification_store.add("Task Started", task.name, "info")

    def task_progress(self, task, progress, message=""):
        # Ignore progress updates to avoid flooding logs
        pass

    def task_completed(self, task):

        # Automatically save to history
        history_database.add_task(task)

        activity_log.add("Task Completed", task.name, "Task")

        notification_store.add("Task Completed", task.name, "success")

    def task_failed(self, task):

        history_database.add_task(task)

        activity_log.add("Task Failed", task.name, "Error")

        notification_store.add("Task Failed", task.name, "error")

    def task_cancelled(self, task):

        history_database.add_task(task)

        activity_log.add("Task Cancelled", task.name, "Task")

        notification_store.add("Task Cancelled", task.name, "warning")

    def task_removed(self, task):

        activity_log.add("Task Removed", task.name, "Task")

    # ==================================================
    # History Events
    # ==================================================

    def history_added(self, task):

        activity_log.add("History Added", f"{task.name} saved to history.", "History")

    def history_deleted(self, record_id):

        activity_log.add("History Deleted", f"Record {record_id} deleted.", "History")

    def history_cleared(self):

        activity_log.add("History Cleared", "All history records removed.", "History")

        notification_store.add("History", "History cleared successfully.", "warning")

    def history_exported(self, file, count):

        activity_log.add("History Exported", f"{count} records exported.", "History")

        notification_store.add(
            "History Export", f"Exported {count} records successfully.", "success"
        )

    # ==================================================
    # Settings
    # ==================================================

    def settings_loaded(self, settings):

        activity_log.add("Settings Loaded", "Application settings loaded.", "Settings")

    def settings_saved(self, settings):

        activity_log.add("Settings Saved", "Application settings updated.", "Settings")

        notification_store.add("Settings", "Settings saved successfully.", "success")

    # ==================================================
    # Error Events
    # ==================================================

    def error_occurred(self, error, source="Application"):

        activity_log.add("Error", f"{source}: {error}", "Error")

        notification_store.add("Error", str(error), "error")


# ==================================================
# Global Instance
# ==================================================

event_handlers = EventHandlers()
