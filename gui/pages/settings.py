import customtkinter as ctk
from tkinter import filedialog, messagebox

from gui.widgets.header import Header
from core.settings import load_settings, save_settings


class SettingsPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.settings = load_settings()

        # ==================================
        # Header
        # ==================================

        header = Header(self, "⚙ Settings")
        header.pack(fill="x")

        # ==================================
        # Main Container
        # ==================================

        container = ctk.CTkScrollableFrame(self)

        container.pack(fill="both", expand=True, padx=20, pady=20)

        # ==================================
        # Theme
        # ==================================

        ctk.CTkLabel(
            container, text="Appearance Theme", font=("Segoe UI", 16, "bold")
        ).pack(anchor="w", pady=(10, 5))

        self.theme = ctk.CTkOptionMenu(container, values=["Light", "Dark", "System"])

        self.theme.set(self.settings["theme"])

        self.theme.pack(fill="x")

        # ==================================
        # Download Folder
        # ==================================

        ctk.CTkLabel(
            container, text="Default Output Folder", font=("Segoe UI", 16, "bold")
        ).pack(anchor="w", pady=(20, 5))

        folder_frame = ctk.CTkFrame(container)

        folder_frame.pack(fill="x")

        self.folder = ctk.CTkEntry(folder_frame)

        self.folder.insert(0, self.settings["download_folder"])

        self.folder.pack(side="left", fill="x", expand=True, padx=(0, 10))

        ctk.CTkButton(folder_frame, text="Browse", command=self.choose_folder).pack(
            side="right"
        )

        # ==================================
        # Maximum Workers
        # ==================================

        ctk.CTkLabel(
            container, text="Maximum Concurrent Tasks", font=("Segoe UI", 16, "bold")
        ).pack(anchor="w", pady=(20, 5))

        self.workers = ctk.CTkSlider(container, from_=1, to=10, number_of_steps=9)

        self.workers.set(self.settings["max_workers"])

        self.workers.pack(fill="x")

        self.worker_label = ctk.CTkLabel(
            container, text=str(self.settings["max_workers"])
        )

        self.worker_label.pack()

        self.workers.configure(command=self.update_workers)

        # ==================================
        # Refresh Interval
        # ==================================

        ctk.CTkLabel(
            container, text="Refresh Interval (ms)", font=("Segoe UI", 16, "bold")
        ).pack(anchor="w", pady=(20, 5))

        self.refresh = ctk.CTkEntry(container)

        self.refresh.insert(0, str(self.settings["refresh_interval"]))

        self.refresh.pack(fill="x")

        # ==================================
        # Notifications
        # ==================================

        self.notifications = ctk.CTkCheckBox(container, text="Enable Notifications")

        if self.settings["show_notifications"]:
            self.notifications.select()

        self.notifications.pack(anchor="w", pady=20)

        # ==================================
        # Auto Save History
        # ==================================

        self.history = ctk.CTkCheckBox(container, text="Automatically Save History")

        if self.settings["auto_save_history"]:
            self.history.select()

        self.history.pack(anchor="w")

        # ==================================
        # Save Button
        # ==================================

        ctk.CTkButton(
            container, text="💾 Save Settings", height=45, command=self.save
        ).pack(fill="x", pady=30)

    # ==================================

    def choose_folder(self):

        folder = filedialog.askdirectory()

        if folder:
            self.folder.delete(0, "end")
            self.folder.insert(0, folder)

    # ==================================

    def update_workers(self, value):

        self.worker_label.configure(text=str(int(value)))

    # ==================================

    def save(self):

        settings = {
            "theme": self.theme.get(),
            "download_folder": self.folder.get(),
            "max_workers": int(self.workers.get()),
            "refresh_interval": int(self.refresh.get()),
            "show_notifications": self.notifications.get() == 1,
            "auto_save_history": self.history.get() == 1,
        }

        save_settings(settings)

        ctk.set_appearance_mode(settings["theme"])

        messagebox.showinfo("Success", "Settings saved successfully.")
