import customtkinter as ctk


class AboutPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        title = ctk.CTkLabel(self, text="ℹ About", font=("Segoe UI", 30, "bold"))
        title.pack(pady=30)

        info = ctk.CTkLabel(
            self,
            text="Suvom Media Downloader\nVersion 1.0\n\nDeveloped by Suvom",
            font=("Segoe UI", 18),
        )
        info.pack(pady=20)
