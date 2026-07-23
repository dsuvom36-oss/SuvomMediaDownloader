import customtkinter as ctk


class DownloadsPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)

        # Header
        header = ctk.CTkFrame(self, corner_radius=12)
        header.pack(fill="x", padx=20, pady=20)

        ctk.CTkLabel(
            header, text="📥 Download Manager", font=("Segoe UI", 28, "bold")
        ).pack(pady=15)

        # Download Card
        card = ctk.CTkFrame(self, corner_radius=15)
        card.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(
            card, text="Example Video.mp4", font=("Segoe UI", 20, "bold")
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.progress = ctk.CTkProgressBar(card, width=700)
        self.progress.pack(padx=20, pady=10, fill="x")
        self.progress.set(0.35)  # 35%

        info = ctk.CTkFrame(card, fg_color="transparent")
        info.pack(fill="x", padx=20)

        ctk.CTkLabel(info, text="Status : Downloading").grid(
            row=0, column=0, sticky="w"
        )

        ctk.CTkLabel(info, text="Speed : 5.2 MB/s").grid(row=0, column=1, padx=20)

        ctk.CTkLabel(info, text="ETA : 00:45").grid(row=0, column=2, padx=20)

        buttons = ctk.CTkFrame(card, fg_color="transparent")
        buttons.pack(pady=15)

        ctk.CTkButton(buttons, text="▶ Pause", width=140).grid(row=0, column=0, padx=10)

        ctk.CTkButton(buttons, text="❌ Cancel", width=140).grid(
            row=0, column=1, padx=10
        )

        ctk.CTkButton(buttons, text="📁 Open Folder", width=160).grid(
            row=0, column=2, padx=10
        )

        # Queue Section
        queue = ctk.CTkFrame(self, corner_radius=15)
        queue.pack(fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(queue, text="Download Queue", font=("Segoe UI", 22, "bold")).pack(
            pady=15
        )

        queue_box = ctk.CTkTextbox(queue, height=250)
        queue_box.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        queue_box.insert("end", "• Example Video.mp4\n")
        queue_box.insert("end", "• Another Video.mp4\n")
        queue_box.insert("end", "• Sample Audio.mp3\n")

        queue_box.configure(state="disabled")
