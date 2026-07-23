"""
core/event_types.py

Defines all application events used by the EventBus.
"""

from enum import Enum


class Event(str, Enum):

    # ==========================================
    # Application
    # ==========================================

    APPLICATION_STARTED = "application_started"
    APPLICATION_CLOSED = "application_closed"

    # ==========================================
    # Navigation / UI
    # ==========================================

    PAGE_CHANGED = "page_changed"
    THEME_CHANGED = "theme_changed"

    # ==========================================
    # Download Tasks
    # ==========================================

    TASK_ADDED = "task_added"
    TASK_STARTED = "task_started"
    TASK_PAUSED = "task_paused"
    TASK_RESUMED = "task_resumed"
    TASK_PROGRESS = "task_progress"
    TASK_COMPLETED = "task_completed"
    TASK_FAILED = "task_failed"
    TASK_CANCELLED = "task_cancelled"
    TASK_REMOVED = "task_removed"

    # ==========================================
    # Queue
    # ==========================================

    QUEUE_UPDATED = "queue_updated"

    # ==========================================
    # History
    # ==========================================

    HISTORY_ADDED = "history_added"
    HISTORY_DELETED = "history_deleted"
    HISTORY_CLEARED = "history_cleared"
    HISTORY_EXPORTED = "history_exported"

    # ==========================================
    # Notifications
    # ==========================================

    NOTIFICATION_ADDED = "notification_added"
    NOTIFICATION_READ = "notification_read"
    NOTIFICATION_CLEARED = "notification_cleared"

    # ==========================================
    # Activity Log
    # ==========================================

    ACTIVITY_ADDED = "activity_added"
    ACTIVITY_CLEARED = "activity_cleared"

    # ==========================================
    # Settings
    # ==========================================

    SETTINGS_LOADED = "settings_loaded"
    SETTINGS_SAVED = "settings_saved"

    # ==========================================
    # Errors
    # ==========================================

    ERROR_OCCURRED = "error_occurred"

    # ==========================================
    # Downloader
    # ==========================================

    DOWNLOAD_STARTED = "download_started"
    DOWNLOAD_FINISHED = "download_finished"

    # ==========================================
    # Search
    # ==========================================

    SEARCH_STARTED = "search_started"
    SEARCH_COMPLETED = "search_completed"

    # ==========================================
    # Thumbnail
    # ==========================================

    THUMBNAIL_LOADED = "thumbnail_loaded"
