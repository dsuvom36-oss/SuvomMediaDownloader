"""
gui/widgets/__init__.py

Reusable GUI widgets for Suvom Media Downloader.
"""

# ==========================================
# Navigation
# ==========================================

from .sidebar import Sidebar
from .status_bar import StatusBar

# ==========================================
# Cards
# ==========================================

from .download_card import DownloadCard
from .notification_card import NotificationCard
from .history_card import HistoryCard
from .activity_card import ActivityCard

# ==========================================
# Common Widgets
# ==========================================

from .progress_bar import ProgressBar
from .search_box import SearchBox
from .topbar import TopBar

# ==========================================
# Dialogs
# ==========================================

from .dialogs import (
    ConfirmDialog,
    ErrorDialog,
    InfoDialog,
)

# ==========================================
# Public Exports
# ==========================================

__all__ = [
    # Navigation
    "Sidebar",
    "StatusBar",
    # Cards
    "DownloadCard",
    "NotificationCard",
    "HistoryCard",
    "ActivityCard",
    # Common
    "ProgressBar",
    "SearchBox",
    "TopBar",
    # Dialogs
    "ConfirmDialog",
    "ErrorDialog",
    "InfoDialog",
]
