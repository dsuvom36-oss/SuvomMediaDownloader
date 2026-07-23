import customtkinter as ctk


class DownloadCard(ctk.CTkFrame):
    def __init__(
        self, master, title, progress=0, status="Waiting", speed="0 MB/s", eta="--:--"
    ):
        super().__init__(master, corner_radius=15)

        self.pack(fill="x", padx=15, pady=10)

        title_label = ctk.CTkLabel(self, text=title, font=("Segoe UI", 18, "bold"))
        title_label.pack(anchor="w", padx=15, pady=(12, 5))

        self.progress = ctk.CTkProgressBar(self)
        self.progress.pack(fill="x", padx=15)
        self.progress.set(progress / 100)

        info = ctk.CTkFrame(self, fg_color="transparent")
        info.pack(fill="x", padx=15, pady=10)

        ctk.CTkLabel(info, text=f"Status: {status}").grid(row=0, column=0, sticky="w")
        ctk.CTkLabel(info, text=f"Speed: {speed}").grid(row=0, column=1, padx=20)
        ctk.CTkLabel(info, text=f"ETA: {eta}").grid(row=0, column=2, padx=20)

        buttons = ctk.CTkFrame(self, fg_color="transparent")
        buttons.pack(pady=(0, 12))

        ctk.CTkButton(buttons, text="⏸ Pause", width=110).grid(row=0, column=0, padx=5)
        ctk.CTkButton(buttons, text="❌ Cancel", width=110).grid(
            row=0, column=1, padx=5
        )
        ctk.CTkButton(buttons, text="📁 Open", width=110).grid(row=0, column=2, padx=5)
