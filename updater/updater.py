"""
updater/updater.py

Application Updater
"""

from __future__ import annotations

from typing import Optional

from .update_checker import UpdateChecker
from .version import Version


class Updater:
    """
    Coordinates application update operations.
    """

    def __init__(self, checker: Optional[UpdateChecker] = None):
        self.checker = checker or UpdateChecker()

    # -----------------------------------------------------
    # Check
    # -----------------------------------------------------

    def check_for_updates(self) -> bool:
        """
        Returns True if an update is available.
        """
        return self.checker.is_update_available()

    def latest_version(self) -> Version:
        """
        Return the latest available version.
        """
        return self.checker.latest_version()

    def current_version(self) -> Version:
        """
        Return the installed version.
        """
        return self.checker.current_version()

    # -----------------------------------------------------
    # Information
    # -----------------------------------------------------

    def update_info(self) -> dict:
        """
        Return update information.
        """
        return {
            "current_version": str(self.current_version()),
            "latest_version": str(self.latest_version()),
            "update_available": self.check_for_updates(),
        }

    # -----------------------------------------------------
    # Download
    # -----------------------------------------------------

    def download_update(self) -> None:
        """
        Placeholder for downloading updates.
        """
        raise NotImplementedError("Download functionality is not implemented.")

    # -----------------------------------------------------
    # Install
    # -----------------------------------------------------

    def install_update(self) -> None:
        """
        Placeholder for installing updates.
        """
        raise NotImplementedError("Install functionality is not implemented.")

    # -----------------------------------------------------
    # Combined
    # -----------------------------------------------------

    def update(self) -> bool:
        """
        Check whether an update is available.

        Returns:
            True if an update is available.
            False otherwise.
        """
        return self.check_for_updates()

    # -----------------------------------------------------
    # Representation
    # -----------------------------------------------------

    def __repr__(self) -> str:
        return (
            f"<Updater "
            f"current={self.current_version()} "
            f"latest={self.latest_version()}>"
        )
