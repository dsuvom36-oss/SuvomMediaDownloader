import json
import os

from core.event_bus import event_bus
from core.event_types import Event

SETTINGS_FILE = "config/settings.json"


DEFAULT_SETTINGS = {
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


def load_settings():

    if not os.path.exists(SETTINGS_FILE):

        save_settings(DEFAULT_SETTINGS)

        settings = DEFAULT_SETTINGS.copy()

    else:

        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:

            settings = json.load(f)

        updated = False

        for key, value in DEFAULT_SETTINGS.items():

            if key not in settings:

                settings[key] = value

                updated = True

        if updated:

            save_settings(settings)

    event_bus.publish(Event.SETTINGS_LOADED, settings=settings)

    return settings


def save_settings(settings):

    os.makedirs(os.path.dirname(SETTINGS_FILE), exist_ok=True)

    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:

        json.dump(settings, f, indent=4)

    event_bus.publish(Event.SETTINGS_SAVED, settings=settings)


def get_setting(settings, key):

    return settings.get(key, DEFAULT_SETTINGS.get(key))


def set_setting(settings, key, value):

    settings[key] = value

    save_settings(settings)
