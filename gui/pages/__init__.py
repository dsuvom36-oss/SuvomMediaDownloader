"""
gui/pages/__init__.py

Exports all GUI pages.
"""

from .home import HomePage
from .search import SearchPage
from .downloads import DownloadsPage
from .history import HistoryPage
from .notifications import NotificationsPage
from .activity import ActivityPage
from .settings import SettingsPage
from .about import AboutPage

__all__ = [
    "HomePage",
    "SearchPage",
    "DownloadsPage",
    "HistoryPage",
    "NotificationsPage",
    "ActivityPage",
    "SettingsPage",
    "AboutPage",
]
