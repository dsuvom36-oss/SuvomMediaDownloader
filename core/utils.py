"""
core/utils.py

Common utility functions.
"""

from pathlib import Path
from datetime import datetime
import os
import re

# ==================================================
# File Utilities
# ==================================================


def ensure_directory(path):
    """
    Create directory if it doesn't exist.
    """
    Path(path).mkdir(parents=True, exist_ok=True)


def file_exists(path):
    """
    Check whether a file exists.
    """
    return Path(path).exists()


def get_file_size(path):
    """
    Return file size in bytes.
    """
    if not file_exists(path):
        return 0

    return os.path.getsize(path)


# ==================================================
# Size Formatting
# ==================================================


def format_bytes(size):

    if size is None:
        return "0 B"

    size = float(size)

    units = ["B", "KB", "MB", "GB", "TB"]

    for unit in units:

        if size < 1024:
            return f"{size:.2f} {unit}"

        size /= 1024

    return f"{size:.2f} PB"


# ==================================================
# Speed Formatting
# ==================================================


def format_speed(speed):

    return f"{format_bytes(speed)}/s"


# ==================================================
# Time Formatting
# ==================================================


def format_seconds(seconds):

    if seconds is None:
        return "--:--"

    seconds = int(seconds)

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    if hours:
        return f"{hours:02}:{minutes:02}:{secs:02}"

    return f"{minutes:02}:{secs:02}"


# ==================================================
# Date & Time
# ==================================================


def current_time():

    return datetime.now().strftime("%H:%M:%S")


def current_date():

    return datetime.now().strftime("%d-%m-%Y")


def current_datetime():

    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# ==================================================
# Filename Utilities
# ==================================================

INVALID_CHARS = r'[<>:"/\\|?*]'


def sanitize_filename(name):

    name = re.sub(INVALID_CHARS, "", name)

    return name.strip()


# ==================================================
# Progress
# ==================================================


def progress_percentage(downloaded, total):

    if total == 0:
        return 0

    return round((downloaded / total) * 100, 2)


# ==================================================
# ETA
# ==================================================


def calculate_eta(downloaded, total, speed):

    if speed <= 0:
        return "--:--"

    remaining = total - downloaded

    if remaining <= 0:
        return "00:00"

    return format_seconds(remaining / speed)
