import customtkinter as ctk
from tkinter import filedialog, messagebox

from gui.widgets.header import Header
from gui.widgets.history_row import HistoryRow
from gui.widgets.stat_card import StatCard


class HistoryPage(ctk.CTkFrame):

    def __init__(self, master, history_db=None):
        super().__init__(master)

        self.history_db = history_db

        # ==========================================
        # Header
        # ==========================================

        header = Header(self, "🕒 History")
        header.pack(fill="x")

        # ==========================================
        # Statistics
        # ==========================================

        stats_frame = ctk.CTkFrame(self)
        stats_frame.pack(fill="x", padx=20, pady=(15, 10))

        self.total_card = StatCard(stats_frame, "Total", "0", "📄")

        self.completed_card = StatCard(stats_frame, "Completed", "0", "✅")

        self.failed_card = StatCard(stats_frame, "Failed", "0", "❌")

        self.total_card.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.completed_card.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.failed_card.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

        for i in range(3):
            stats_frame.grid_columnconfigure(i, weight=1)

        # ==========================================
        # Toolbar
        # ==========================================

        toolbar = ctk.CTkFrame(self)
        toolbar.pack(fill="x", padx=20, pady=(0, 10))

        self.search_entry = ctk.CTkEntry(toolbar, placeholder_text="Search task...")

        self.search_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        self.search_entry.bind("<KeyRelease>", lambda e: self.load_history())

        self.status_filter = ctk.CTkOptionMenu(
            toolbar,
            values=["All", "Completed", "Failed", "Cancelled"],
            command=lambda x: self.load_history(),
        )

        self.status_filter.pack(side="left", padx=5)

        self.refresh_btn = ctk.CTkButton(
            toolbar, text="Refresh", width=100, command=self.load_history
        )

        self.refresh_btn.pack(side="left", padx=5)

        self.export_btn = ctk.CTkButton(
            toolbar, text="Export CSV", width=120, command=self.export_csv
        )

        self.export_btn.pack(side="left", padx=5)

        self.clear_btn = ctk.CTkButton(
            toolbar,
            text="Clear",
            width=100,
            fg_color="red",
            hover_color="#990000",
            command=self.clear_history,
        )

        self.clear_btn.pack(side="left", padx=5)

        # ==========================================
        # Scrollable History
        # ==========================================

        self.scroll = ctk.CTkScrollableFrame(self)

        self.scroll.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        self.load_history()

    # ==================================================

    def update_statistics(self):

        if self.history_db is None:
            return

        self.total_card.update_value(self.history_db.count())

        self.completed_card.update_value(self.history_db.count_by_status("Completed"))

        self.failed_card.update_value(self.history_db.count_by_status("Failed"))

    # ==================================================

    def load_history(self):

        for widget in self.scroll.winfo_children():
            widget.destroy()

        if self.history_db is None:
            return

        self.update_statistics()

        search = self.search_entry.get().strip()

        status = self.status_filter.get()

        if search:

            rows = self.history_db.search(search)

        elif status != "All":

            rows = self.history_db.filter_by_status(status)

        else:

            rows = self.history_db.get_all()

        for row in rows:

            task = {
                "id": row[0],
                "task_id": row[1],
                "name": row[2],
                "status": row[3],
                "progress": row[4],
                "message": row[5],
                "created_at": row[6],
                "started_at": row[7],
                "finished_at": row[8],
            }

            history_row = HistoryRow(
                self.scroll, task, on_view=self.view_task, on_delete=self.delete_task
            )

            history_row.pack(fill="x", padx=5, pady=5)

    # ==================================================

    def view_task(self, task):

        messagebox.showinfo(
            "Task Details",
            f"Task : {task['name']}\n\n"
            f"Status : {task['status']}\n"
            f"Progress : {task['progress']}%\n"
            f"Message : {task['message']}\n\n"
            f"Created : {task['created_at']}\n"
            f"Started : {task['started_at']}\n"
            f"Finished : {task['finished_at']}",
        )

    # ==================================================

    def delete_task(self, task):

        if not messagebox.askyesno("Delete", f"Delete '{task['name']}'?"):

            return

        self.history_db.delete(task["task_id"])

        self.load_history()

    # ==================================================

    def clear_history(self):

        if not messagebox.askyesno("Clear History", "Delete all history?"):

            return

        self.history_db.clear()

        self.load_history()

    # ==================================================

    def export_csv(self):

        filename = filedialog.asksaveasfilename(
            defaultextension=".csv", filetypes=[("CSV Files", "*.csv")]
        )

        if not filename:
            return

        self.history_db.export_csv(filename)

        messagebox.showinfo("Export", "History exported successfully.")
