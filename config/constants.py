"""
config/constants.py

Application Constants
Suvom Media Downloader
"""

from pathlib import Path

# ==========================================================
# Application
# ==========================================================

APP_NAME = "Suvom Media Downloader"
APP_VERSION = "2.0.0"
APP_AUTHOR = "Suvom Project Limited"
APP_COMPANY = "Suvom Project Limited"

WEBSITE = "https://suvomprojectlimited.com"
EMAIL = "suvomproject@gmail.com"

# ==========================================================
# Root Directories
# ==========================================================

ROOT_DIR = Path(__file__).resolve().parent.parent

ASSETS_DIR = ROOT_DIR / "assets"
CONFIG_DIR = ROOT_DIR / "config"
CORE_DIR = ROOT_DIR / "core"
GUI_DIR = ROOT_DIR / "gui"
SERVICES_DIR = ROOT_DIR / "services"

DOWNLOAD_DIR = ROOT_DIR / "downloads"
LOG_DIR = ROOT_DIR / "logs"
TEMP_DIR = ROOT_DIR / "temp"

# ==========================================================
# Assets
# ==========================================================

ICON_DIR = ASSETS_DIR / "icons"
IMAGE_DIR = ASSETS_DIR / "images"
FONT_DIR = ASSETS_DIR / "fonts"
THEME_DIR = ASSETS_DIR / "themes"

DARK_THEME = THEME_DIR / "dark.json"
LIGHT_THEME = THEME_DIR / "light.json"
BLUE_THEME = THEME_DIR / "blue.json"

# ==========================================================
# Config Files
# ==========================================================

CONFIG_FILE = CONFIG_DIR / "config.json"
SETTINGS_FILE = CONFIG_DIR / "settings.json"

# ==========================================================
# Downloads
# ==========================================================

DEFAULT_DOWNLOAD_FOLDER = DOWNLOAD_DIR

MAX_CONCURRENT_DOWNLOADS = 3

DEFAULT_TIMEOUT = 30

RETRY_COUNT = 3

RETRY_DELAY = 5

# ==========================================================
# Window
# ==========================================================

WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 850

MIN_WINDOW_WIDTH = 1200
MIN_WINDOW_HEIGHT = 700

# ==========================================================
# Theme
# ==========================================================

DEFAULT_THEME = "dark"

DEFAULT_APPEARANCE_MODE = "system"

DEFAULT_FONT = "Segoe UI"

FONT_SMALL = 11
FONT_NORMAL = 13
FONT_LARGE = 16
FONT_TITLE = 22

# ==========================================================
# Progress
# ==========================================================

REFRESH_INTERVAL = 500

THUMBNAIL_SIZE = (320, 180)

# ==========================================================
# Logging
# ==========================================================

LOG_LEVEL = "INFO"

LOG_FILE = LOG_DIR / "application.log"

# ==========================================================
# Database
# ==========================================================

HISTORY_DATABASE = CONFIG_DIR / "history.db"

# ==========================================================
# Cache
# ==========================================================

CACHE_DIRECTORY = TEMP_DIR / "cache"

THUMBNAIL_CACHE = TEMP_DIR / "thumbnails"

# ==========================================================
# Notifications
# ==========================================================

NOTIFICATION_DURATION = 4000

# ==========================================================
# Supported File Extensions
# ==========================================================

VIDEO_EXTENSIONS = [
    ".mp4",
    ".mkv",
    ".webm",
    ".avi",
    ".mov",
]

AUDIO_EXTENSIONS = [
    ".mp3",
    ".wav",
    ".aac",
    ".ogg",
    ".m4a",
]

IMAGE_EXTENSIONS = [
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
]

# ==========================================================
# Colors
# ==========================================================

SUCCESS_COLOR = "#22C55E"
WARNING_COLOR = "#F59E0B"
ERROR_COLOR = "#EF4444"
PRIMARY_COLOR = "#3B82F6"

# ==========================================================
# Status
# ==========================================================

STATUS_READY = "Ready"
STATUS_RUNNING = "Running"
STATUS_PAUSED = "Paused"
STATUS_COMPLETED = "Completed"
STATUS_FAILED = "Failed"
STATUS_CANCELLED = "Cancelled"

# ==========================================================
# Event Names
# ==========================================================

APP_STARTED = "application_started"
APP_CLOSED = "application_closed"

TASK_STARTED = "task_started"
TASK_PROGRESS = "task_progress"
TASK_COMPLETED = "task_completed"
TASK_FAILED = "task_failed"
TASK_CANCELLED = "task_cancelled"

# ==========================================================
# Create Required Directories
# ==========================================================

for directory in (
    DOWNLOAD_DIR,
    LOG_DIR,
    TEMP_DIR,
    CACHE_DIRECTORY,
    THUMBNAIL_CACHE,
):
    directory.mkdir(parents=True, exist_ok=True)
