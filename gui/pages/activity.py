import customtkinter as ctk

from gui.widgets.header import Header


class ActivityPage(ctk.CTkFrame):

    REFRESH_INTERVAL = 1000

    def __init__(self, master):
        super().__init__(master)

        self.rows = {}

        # =====================================
        # Header
        # =====================================

        header = Header(self, "📋 Activity Log")
        header.pack(fill="x")

        # =====================================
        # Toolbar
        # =====================================

        toolbar = ctk.CTkFrame(self)
        toolbar.pack(fill="x", padx=15, pady=10)

        self.search = ctk.CTkEntry(toolbar, placeholder_text="Search...")
        self.search.pack(side="left", fill="x", expand=True, padx=(0, 10))

        self.filter = ctk.CTkOptionMenu(
            toolbar,
            values=[
                "All",
                "System",
                "Task",
                "History",
                "Settings",
                "Notification",
                "Queue",
                "User",
                "Error",
            ],
            command=lambda _: self.refresh(),
        )

        self.filter.pack(side="left")

        ctk.CTkButton(toolbar, text="Refresh", command=self.refresh).pack(
            side="left", padx=5
        )

        ctk.CTkButton(toolbar, text="Clear All", command=self.clear_all).pack(
            side="right"
        )

        # =====================================
        # Statistics
        # =====================================

        self.stats = ctk.CTkLabel(
            self, text="Activities: 0", font=("Segoe UI", 14, "bold")
        )

        self.stats.pack(anchor="w", padx=20, pady=(0, 10))

        # =====================================
        # Scroll Area
        # =====================================

        self.scroll = ctk.CTkScrollableFrame(self)

        self.scroll.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        self.refresh()
