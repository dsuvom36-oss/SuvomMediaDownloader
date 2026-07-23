"""
gui/widgets/status_bar.py

Status Bar Widget
"""

import customtkinter as ctk

from core.event_bus import event_bus
from core.event_types import Event


class StatusBar(ctk.CTkFrame):

    def __init__(self, parent, services):

        super().__init__(parent, height=32, corner_radius=0)

        self.services = services

        self.task_manager = services.task_manager
        self.download_service = services.download_service
        self.notification_service = services.notification_service

        self.grid_columnconfigure(1, weight=1)

        self.create_widgets()
        self.register_events()

    # ======================================
    # Widgets
    # ======================================

    def create_widgets(self):

        self.status_label = ctk.CTkLabel(self, text="Ready", anchor="w")

        self.status_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.info_label = ctk.CTkLabel(self, text="0 Active | 0 Completed", anchor="e")

        self.info_label.grid(row=0, column=1, padx=10, pady=5, sticky="e")

    # ======================================
    # Event Registration
    # ======================================

    def register_events(self):

        event_bus.subscribe(Event.APPLICATION_STARTED, self.on_application_started)

        event_bus.subscribe(Event.TASK_ADDED, self.refresh)

        event_bus.subscribe(Event.TASK_STARTED, self.refresh)

        event_bus.subscribe(Event.TASK_PROGRESS, self.refresh)

        event_bus.subscribe(Event.TASK_COMPLETED, self.refresh)

        event_bus.subscribe(Event.TASK_FAILED, self.refresh)

        event_bus.subscribe(Event.TASK_CANCELLED, self.refresh)
