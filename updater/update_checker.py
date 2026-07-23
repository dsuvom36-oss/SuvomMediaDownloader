"""
updater/update_checker.py

Checks whether a new application version is available.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

from .version import Version


class UpdateChecker:
    """
    Performs update checks using a local manifest file.

    The manifest should contain:

    {
        "version": "2.1.0",
        "release_notes": "...",
        "download_url": "..."
    }
    """

    def __init__(
        self,
        current_version: str = "2.0.0",
        manifest_path: Optional[Path] = None,
    ):
        self._current = Version(current_version)

        self.manifest_path = manifest_path or Path(__file__).parent / "manifest.json"

        self._latest = self._current
        self._manifest = {}

        self.load_manifest()

    # -------------------------------------------------
    # Manifest
    # -------------------------------------------------

    def load_manifest(self) -> None:
        """
        Load update manifest.
        """

        if not self.manifest_path.exists():
            self._latest = self._current
            self._manifest = {}
            return

        try:
            with open(self.manifest_path, "r", encoding="utf-8") as file:
                self._manifest = json.load(file)

            version = self._manifest.get(
                "version",
                str(self._current),
            )

            self._latest = Version(version)

        except Exception:
            self._manifest = {}
            self._latest = self._current

    # -------------------------------------------------
    # Versions
    # -------------------------------------------------

    def current_version(self) -> Version:
        return self._current

    def latest_version(self) -> Version:
        return self._latest

    # -------------------------------------------------
    # Update
    # -------------------------------------------------

    def is_update_available(self) -> bool:
        return self._latest > self._current

    # -------------------------------------------------
    # Manifest Data
    # -------------------------------------------------

    def release_notes(self) -> str:
        return self._manifest.get("release_notes", "")

    def download_url(self) -> str:
        return self._manifest.get("download_url", "")

    def manifest(self) -> dict:
        return dict(self._manifest)

    # -------------------------------------------------
    # Refresh
    # -------------------------------------------------

    def refresh(self) -> None:
        """
        Reload the manifest.
        """
        self.load_manifest()

    # -------------------------------------------------
    # Representation
    # -------------------------------------------------

    def __repr__(self) -> str:
        return f"<UpdateChecker " f"current={self._current} " f"latest={self._latest}>"
