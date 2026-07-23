from tkinter import messagebox

from core.notification_store import notification_store


class NotificationManager:

    def __init__(self, enabled=True):

        self.enabled = enabled

    # -------------------------------------

    def enable(self):

        self.enabled = True

    # -------------------------------------

    def disable(self):

        self.enabled = False

    # -------------------------------------

    def notify(self, title, message, level="info"):

        # Save notification
        notification_store.add(title=title, message=message, level=level)

        # Skip popup if disabled
        if not self.enabled:
            return

        if level == "success":
            messagebox.showinfo(f"✅ {title}", message)

        elif level == "warning":
            messagebox.showwarning(title, message)

        elif level == "error":
            messagebox.showerror(title, message)

        else:
            messagebox.showinfo(title, message)

    # -------------------------------------

    def info(self, title, message):

        self.notify(title, message, "info")

    # -------------------------------------

    def success(self, title, message):

        self.notify(title, message, "success")

    # -------------------------------------

    def warning(self, title, message):

        self.notify(title, message, "warning")

    # -------------------------------------

    def error(self, title, message):

        self.notify(title, message, "error")

    # -------------------------------------
    # Task Events
    # -------------------------------------

    def task_started(self, task_name):

        self.info("Task Started", f"{task_name} has started.")

    def task_completed(self, task_name):

        self.success("Task Completed", f"{task_name} completed successfully.")

    def task_failed(self, task_name):

        self.error("Task Failed", f"{task_name} failed.")

    def task_paused(self, task_name):

        self.warning("Task Paused", f"{task_name} has been paused.")

    def task_cancelled(self, task_name):

        self.warning("Task Cancelled", f"{task_name} has been cancelled.")

    # -------------------------------------
    # App Events
    # -------------------------------------

    def settings_saved(self):

        self.success("Settings", "Settings saved successfully.")

    def history_exported(self):

        self.success("History", "History exported successfully.")

    def application_started(self):

        self.info("Application", "Application started.")

    def application_closed(self):

        self.info("Application", "Application closed.")
