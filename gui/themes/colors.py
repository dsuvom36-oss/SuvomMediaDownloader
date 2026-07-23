"""
gui/themes/colors.py

Color definitions for Suvom Media Downloader.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Colors:

    # ======================================================
    # Brand
    # ======================================================

    PRIMARY = "#3B82F6"
    PRIMARY_HOVER = "#2563EB"

    SUCCESS = "#22C55E"
    WARNING = "#F59E0B"
    ERROR = "#EF4444"

    INFO = "#0EA5E9"

    # ======================================================
    # Dark Theme
    # ======================================================

    DARK_BG = "#181818"
    DARK_CARD = "#242424"
    DARK_NAV = "#1E1E1E"

    DARK_BORDER = "#303030"

    DARK_TEXT = "#FFFFFF"
    DARK_TEXT_SECONDARY = "#CFCFCF"

    # ======================================================
    # Light Theme
    # ======================================================

    LIGHT_BG = "#F5F5F5"
    LIGHT_CARD = "#FFFFFF"
    LIGHT_NAV = "#FFFFFF"

    LIGHT_BORDER = "#D1D5DB"

    LIGHT_TEXT = "#111827"
    LIGHT_TEXT_SECONDARY = "#6B7280"

    # ======================================================
    # Blue Theme
    # ======================================================

    BLUE_BG = "#0F172A"
    BLUE_CARD = "#1E293B"
    BLUE_NAV = "#16213E"

    BLUE_BORDER = "#334155"

    BLUE_TEXT = "#F8FAFC"
    BLUE_TEXT_SECONDARY = "#CBD5E1"

    # ======================================================
    # Downloads
    # ======================================================

    DOWNLOAD_RUNNING = "#3B82F6"
    DOWNLOAD_COMPLETED = "#22C55E"
    DOWNLOAD_FAILED = "#EF4444"
    DOWNLOAD_PAUSED = "#F59E0B"
    DOWNLOAD_QUEUED = "#9CA3AF"

    # ======================================================
    # Notifications
    # ======================================================

    NOTIFICATION_INFO = "#3B82F6"
    NOTIFICATION_SUCCESS = "#22C55E"
    NOTIFICATION_WARNING = "#F59E0B"
    NOTIFICATION_ERROR = "#EF4444"

    # ======================================================
    # Activity
    # ======================================================

    ACTIVITY_DOWNLOAD = "#3B82F6"
    ACTIVITY_HISTORY = "#22C55E"
    ACTIVITY_SYSTEM = "#8B5CF6"

    # ======================================================
    # Status
    # ======================================================

    READY = "#22C55E"
    BUSY = "#3B82F6"
    IDLE = "#9CA3AF"

    # ======================================================
    # Misc
    # ======================================================

    WHITE = "#FFFFFF"
    BLACK = "#000000"

    TRANSPARENT = "transparent"


colors = Colors()
