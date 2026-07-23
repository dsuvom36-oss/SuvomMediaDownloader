"""
updater/downloader.py

Update Downloader

Generic downloader used by the updater system.
"""

from __future__ import annotations

from pathlib import Path
from urllib.request import urlretrieve
from typing import Callable, Optional

ProgressCallback = Callable[[int, int], None]


class UpdateDownloader:
    """
    Downloads update packages.
    """

    def __init__(self, download_directory: Path | None = None):
        self.download_directory = (
            download_directory or Path(__file__).parent / "downloads"
        )

        self.download_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    # -------------------------------------------------
    # Download
    # -------------------------------------------------

    def download(
        self,
        url: str,
        filename: str | None = None,
        progress_callback: Optional[ProgressCallback] = None,
    ) -> Path:
        """
        Download a file.

        Args:
            url:
                Download URL.

            filename:
                Optional output filename.

            progress_callback:
                Function(bytes_downloaded, total_bytes)

        Returns:
            Path to downloaded file.
        """

        if filename is None:
            filename = url.split("/")[-1] or "update.bin"

        destination = self.download_directory / filename

        def reporthook(block_num, block_size, total_size):
            if progress_callback:
                downloaded = block_num * block_size
                progress_callback(downloaded, total_size)

        urlretrieve(
            url,
            destination,
            reporthook=reporthook,
        )

        return destination

    # -------------------------------------------------
    # Exists
    # -------------------------------------------------

    def exists(self, filename: str) -> bool:
        return (self.download_directory / filename).exists()

    # -------------------------------------------------
    # Delete
    # -------------------------------------------------

    def delete(self, filename: str) -> bool:
        file = self.download_directory / filename

        if file.exists():
            file.unlink()
            return True

        return False

    # -------------------------------------------------
    # Clear
    # -------------------------------------------------

    def clear(self) -> None:
        for file in self.download_directory.iterdir():
            if file.is_file():
                file.unlink()

    # -------------------------------------------------
    # List Files
    # -------------------------------------------------

    def files(self) -> list[Path]:
        return sorted(self.download_directory.glob("*"))

    # -------------------------------------------------
    # Information
    # -------------------------------------------------

    @property
    def directory(self) -> Path:
        return self.download_directory

    def __repr__(self) -> str:
        return f"<UpdateDownloader " f"directory='{self.download_directory}'>"
