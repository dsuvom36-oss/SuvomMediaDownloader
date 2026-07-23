"""
tests/test_installer.py
"""

from pathlib import Path

import pytest

from updater.installer import UpdateInstaller


@pytest.fixture
def installer(tmp_path):
    return UpdateInstaller(install_directory=tmp_path)


def test_create_installer(installer):
    assert installer is not None


def test_validate_missing_file(installer):
    assert installer.validate(Path("missing.zip")) is False


def test_cleanup(installer, tmp_path):
    folder = tmp_path / "temp"

    folder.mkdir()

    (folder / "a.txt").write_text("abc")

    assert folder.exists()

    installer.cleanup(folder)

    assert not folder.exists()


def test_repr(installer):
    assert "UpdateInstaller" in repr(installer)
