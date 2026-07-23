"""
tests/test_downloader.py
"""


import pytest

from updater.downloader import UpdateDownloader


@pytest.fixture
def downloader(tmp_path):
    return UpdateDownloader(download_directory=tmp_path)


def test_create_downloader(downloader):
    assert downloader is not None


def test_directory_exists(downloader):
    assert downloader.directory.exists()


def test_files_empty(downloader):
    assert downloader.files() == []


def test_exists_false(downloader):
    assert downloader.exists("update.zip") is False


def test_delete_missing_file(downloader):
    assert downloader.delete("missing.zip") is False


def test_clear_directory(downloader):
    (downloader.directory / "a.txt").write_text("hello")
    (downloader.directory / "b.txt").write_text("world")

    assert len(downloader.files()) == 2

    downloader.clear()

    assert downloader.files() == []


def test_repr(downloader):
    assert "UpdateDownloader" in repr(downloader)
