import customtkinter as ctk

from gui.widgets.header import Header


class NotificationsPage(ctk.CTkFrame):

    REFRESH_INTERVAL = 1000

    def __init__(self, master):
        super().__init__(master)

        self.cards = {}

        # ===========================
        # Header
        # ===========================

        header = Header(self, "🔔 Notifications")
        header.pack(fill="x")

        # ===========================
        # Toolbar
        # ===========================

        toolbar = ctk.CTkFrame(self)
        toolbar.pack(fill="x", padx=15, pady=10)

        self.filter = ctk.CTkOptionMenu(
            toolbar,
            values=["All", "Info", "Success", "Warning", "Error"],
            command=lambda _: self.refresh_notifications(),
        )

        self.filter.set("All")
        self.filter.pack(side="left")

        self.count_label = ctk.CTkLabel(toolbar, text="0 Notifications")
        self.count_label.pack(side="left", padx=15)

        ctk.CTkButton(toolbar, text="Mark All Read", command=self.mark_all_read).pack(
            side="right", padx=5
        )

        ctk.CTkButton(toolbar, text="Clear All", command=self.clear_all).pack(
            side="right"
        )

        # ===========================
        # Scroll Area
        # ===========================

        self.scroll = ctk.CTkScrollableFrame(self)

        self.scroll.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        self.refresh_notifications()
