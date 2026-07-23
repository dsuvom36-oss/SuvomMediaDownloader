"""
gui/__init__.py

GUI Package

Exports all pages and reusable widgets.
"""

# ==========================================
# Pages
# ==========================================

from .pages import (
    HomePage,
    SearchPage,
    DownloadsPage,
    HistoryPage,
    NotificationsPage,
    ActivityPage,
    SettingsPage,
    AboutPage,
)

# ==========================================
# Widgets
# ==========================================

from .widgets.sidebar import Sidebar
from .widgets.status_bar import StatusBar

# ==========================================
# Public Exports
# ==========================================

__all__ = [
    # Pages
    "HomePage",
    "SearchPage",
    "DownloadsPage",
    "HistoryPage",
    "NotificationsPage",
    "ActivityPage",
    "SettingsPage",
    "AboutPage",
    # Widgets
    "Sidebar",
    "StatusBar",
]
