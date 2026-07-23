import customtkinter as ctk


class SearchPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)

        # Header
        header = ctk.CTkFrame(self, corner_radius=12)
        header.pack(fill="x", padx=20, pady=20)

        ctk.CTkLabel(
            header, text="🔍 Search Media", font=("Segoe UI", 28, "bold")
        ).pack(pady=15)

        # Search Card
        card = ctk.CTkFrame(self, corner_radius=15)
        card.pack(fill="x", padx=20)

        ctk.CTkLabel(
            card, text="Paste a supported media URL", font=("Segoe UI", 18, "bold")
        ).pack(pady=(20, 10))

        self.url_entry = ctk.CTkEntry(card, height=40, placeholder_text="https://...")
        self.url_entry.pack(fill="x", padx=30)

        ctk.CTkButton(card, text="Preview", height=40, width=180).pack(pady=20)

        # Preview Card
        preview = ctk.CTkFrame(self, corner_radius=15)
        preview.pack(fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(preview, text="Preview", font=("Segoe UI", 22, "bold")).pack(
            pady=15
        )

        thumbnail = ctk.CTkFrame(preview, width=300, height=170, corner_radius=12)
        thumbnail.pack(pady=10)
        thumbnail.pack_propagate(False)

        ctk.CTkLabel(thumbnail, text="Thumbnail", font=("Segoe UI", 20)).place(
            relx=0.5, rely=0.5, anchor="center"
        )

        info = ctk.CTkFrame(preview, fg_color="transparent")
        info.pack(fill="x", padx=40, pady=20)

        ctk.CTkLabel(info, text="Title: -").pack(anchor="w")
        ctk.CTkLabel(info, text="Duration: -").pack(anchor="w")
        ctk.CTkLabel(info, text="Format: -").pack(anchor="w")

        options = ctk.CTkFrame(preview, fg_color="transparent")
        options.pack(pady=10)

        quality = ctk.CTkOptionMenu(options, values=["1080p", "720p", "480p", "360p"])
        quality.grid(row=0, column=0, padx=10)

        format_menu = ctk.CTkOptionMenu(options, values=["MP4", "WEBM", "MP3"])
        format_menu.grid(row=0, column=1, padx=10)

        ctk.CTkButton(preview, text="Download", width=220, height=45).pack(pady=25)
