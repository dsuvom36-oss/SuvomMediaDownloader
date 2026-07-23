"""
tests/test_updater.py

Unit tests for updater.updater
"""

import pytest

from updater.updater import Updater


@pytest.fixture
def updater():
    return Updater()


def test_create_updater(updater):
    assert updater is not None


def test_current_version(updater):
    assert updater.current_version() is not None


def test_latest_version(updater):
    assert updater.latest_version() is not None


def test_check_for_updates_returns_bool(updater):
    assert isinstance(
        updater.check_for_updates(),
        bool,
    )


def test_update_info(updater):
    info = updater.update_info()

    assert isinstance(info, dict)

    assert "current_version" in info
    assert "latest_version" in info
    assert "update_available" in info


def test_update_returns_bool(updater):
    assert isinstance(
        updater.update(),
        bool,
    )


def test_download_update_not_implemented(updater):
    with pytest.raises(NotImplementedError):
        updater.download_update()


def test_install_update_not_implemented(updater):
    with pytest.raises(NotImplementedError):
        updater.install_update()


def test_repr(updater):
    assert "Updater" in repr(updater)
