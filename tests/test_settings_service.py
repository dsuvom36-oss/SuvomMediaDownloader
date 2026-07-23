"""
tests/test_settings_service.py
"""

import pytest

from services.settings_service import SettingsService


@pytest.fixture
def service(monkeypatch):
    data = {"theme": "Dark"}

    monkeypatch.setattr(
        "services.settings_service.load_settings",
        lambda: data.copy(),
    )

    monkeypatch.setattr(
        "services.settings_service.save_settings",
        lambda settings: None,
    )

    monkeypatch.setattr(
        "services.settings_service.event_bus.publish",
        lambda *args, **kwargs: None,
    )

    return SettingsService()


def test_load(service):
    settings = service.load()
    assert settings["theme"] == "Dark"


def test_get_existing(service):
    assert service.get("theme") == "Dark"


def test_get_default(service):
    assert service.get("missing", "default") == "default"


def test_set(service):
    service.set("language", "English")
    assert service.get("language") == "English"


def test_update(service):
    service.update(
        {
            "theme": "Light",
            "language": "Bengali",
        }
    )

    assert service.get("theme") == "Light"
    assert service.get("language") == "Bengali"


def test_remove(service):
    service.set("temp", 123)
    service.remove("temp")
    assert service.get("temp") is None


def test_remove_missing(service):
    service.remove("missing")
    assert service.get("missing") is None


def test_reset_defaults(service):
    service.reset_defaults()

    assert service.get("theme") == "Dark"
    assert service.get("language") == "English"
    assert service.get("max_workers") == 3


def test_as_dict(service):
    data = service.as_dict()

    assert isinstance(data, dict)
    assert data["theme"] == "Dark"


def test_as_dict_returns_copy(service):
    data = service.as_dict()
    data["theme"] = "Changed"

    assert service.get("theme") == "Dark"
