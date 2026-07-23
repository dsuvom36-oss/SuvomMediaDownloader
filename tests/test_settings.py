"""
tests/test_settings.py

Tests for application constants and settings.
"""

from pathlib import Path

from config import constants


def test_app_name():
    assert constants.APP_NAME == "Suvom Media Downloader"


def test_version():
    assert isinstance(constants.APP_VERSION, str)


def test_root_directory():
    assert constants.ROOT_DIR.exists()


def test_assets_directory():
    assert isinstance(constants.ASSETS_DIR, Path)


def test_download_directory():
    assert constants.DOWNLOAD_DIR.exists()


def test_log_directory():
    assert constants.LOG_DIR.exists()


def test_temp_directory():
    assert constants.TEMP_DIR.exists()


def test_window_size():
    assert constants.WINDOW_WIDTH > 0
    assert constants.WINDOW_HEIGHT > 0


def test_default_theme():
    assert constants.DEFAULT_THEME in (
        "dark",
        "light",
        "blue",
    )


def test_font():
    assert isinstance(constants.DEFAULT_FONT, str)


def test_video_extensions():
    assert ".mp4" in constants.VIDEO_EXTENSIONS


def test_audio_extensions():
    assert ".mp3" in constants.AUDIO_EXTENSIONS


def test_image_extensions():
    assert ".png" in constants.IMAGE_EXTENSIONS


def test_log_file():
    assert constants.LOG_FILE.parent.exists()


def test_database_path():
    assert constants.HISTORY_DATABASE.parent.exists()
