"""
services/settings_service.py

Settings Service
"""

from core.settings import load_settings, save_settings
from core.event_bus import event_bus
from core.event_types import Event


class SettingsService:

    def __init__(self):
        self.settings = load_settings()

    # ==================================================
    # Load
    # ==================================================

    def load(self):

        self.settings = load_settings()

        event_bus.publish(Event.SETTINGS_LOADED, settings=self.settings)

        return self.settings

    # ==================================================
    # Save
    # ==================================================

    def save(self):

        save_settings(self.settings)

        event_bus.publish(Event.SETTINGS_SAVED, settings=self.settings)

    # ==================================================
    # Get
    # ==================================================

    def get(self, key, default=None):
        return self.settings.get(key, default)

    # ==================================================
    # Set
    # ==================================================

    def set(self, key, value):

        self.settings[key] = value

        self.save()

    # ==================================================
    # Update Multiple Settings
    # ==================================================

    def update(self, values: dict):

        self.settings.update(values)

        self.save()

    # ==================================================
    # Remove
    # ==================================================

    def remove(self, key):

        if key in self.settings:
            del self.settings[key]
            self.save()

    # ==================================================
    # Reset Defaults
    # ==================================================

    def reset_defaults(self):

        self.settings = {
            "theme": "Dark",
            "download_folder": "downloads",
            "max_workers": 3,
            "refresh_interval": 500,
            "show_notifications": True,
            "auto_save_history": True,
            "auto_start_queue": True,
            "language": "English",
            "check_updates": True,
            "minimize_to_tray": False,
            "start_maximized": False,
        }

        self.save()

    # ==================================================
    # Utility
    # ==================================================

    def as_dict(self):
        return self.settings.copy()


# ==================================================
# Lazy Singleton
# ==================================================

_settings_service = None


def get_settings_service():
    """
    Returns the shared SettingsService instance.
    Creates it only when first requested.
    """
    global _settings_service

    if _settings_service is None:
        _settings_service = SettingsService()

    return _settings_service
