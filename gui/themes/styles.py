"""
gui/themes/styles.py

Style definitions for Suvom Media Downloader
"""

from dataclasses import dataclass

from .colors import colors


@dataclass(frozen=True)
class Fonts:

    FAMILY = "Segoe UI"

    SMALL = (FAMILY, 11)

    NORMAL = (FAMILY, 13)

    MEDIUM = (FAMILY, 15)

    LARGE = (FAMILY, 18)

    TITLE = (FAMILY, 24, "bold")

    HEADING = (FAMILY, 20, "bold")

    SUBTITLE = (FAMILY, 16, "bold")

    BUTTON = (FAMILY, 13, "bold")

    STATUS = (FAMILY, 12)


@dataclass(frozen=True)
class Radius:

    SMALL = 6

    NORMAL = 10

    LARGE = 16

    ROUND = 30


@dataclass(frozen=True)
class Padding:

    XS = 4

    SMALL = 8

    NORMAL = 12

    LARGE = 16

    XL = 24

    XXL = 32


@dataclass(frozen=True)
class Size:

    SIDEBAR_WIDTH = 240

    TOPBAR_HEIGHT = 60

    STATUSBAR_HEIGHT = 32

    DOWNLOAD_CARD_HEIGHT = 120

    HISTORY_CARD_HEIGHT = 80

    NOTIFICATION_CARD_HEIGHT = 70

    ACTIVITY_CARD_HEIGHT = 70

    BUTTON_HEIGHT = 38

    ENTRY_HEIGHT = 38

    PROGRESS_HEIGHT = 12


@dataclass(frozen=True)
class Border:

    WIDTH = 1

    COLOR = colors.DARK_BORDER


@dataclass(frozen=True)
class Animation:

    ENABLED = True

    DURATION = 200

    REFRESH = 500


class Style:

    colors = colors

    fonts = Fonts()

    radius = Radius()

    padding = Padding()

    size = Size()

    border = Border()

    animation = Animation()


style = Style()
