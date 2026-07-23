"""
updater/installer.py

Update Installer

Generic installer responsible for preparing and
installing application update packages.
"""

from __future__ import annotations

import shutil
import zipfile
from pathlib import Path


class UpdateInstaller:
    """
    Handles update package installation.
    """

    def __init__(self, install_directory: Path | None = None):
        self.install_directory = install_directory or Path.cwd()

    # -------------------------------------------------
    # Validation
    # -------------------------------------------------

    def validate(self, package: Path) -> bool:
        """
        Validate that the update package exists.
        """

        return package.exists() and package.is_file()

    # -------------------------------------------------
    # Extract ZIP Package
    # -------------------------------------------------

    def extract(
        self,
        package: Path,
        destination: Path | None = None,
    ) -> Path:
        """
        Extract a ZIP update package.
        """

        if not self.validate(package):
            raise FileNotFoundError(package)

        destination = destination or self.install_directory / "update_temp"

        destination.mkdir(
            parents=True,
            exist_ok=True,
        )

        with zipfile.ZipFile(package, "r") as archive:
            archive.extractall(destination)

        return destination

    # -------------------------------------------------
    # Install
    # -------------------------------------------------

    def install(
        self,
        extracted_directory: Path,
    ) -> None:
        """
        Copy extracted update files into the
        application directory.
        """

        if not extracted_directory.exists():
            raise FileNotFoundError(extracted_directory)

        for item in extracted_directory.iterdir():

            destination = self.install_directory / item.name

            if item.is_dir():

                shutil.copytree(
                    item,
                    destination,
                    dirs_exist_ok=True,
                )

            else:

                shutil.copy2(
                    item,
                    destination,
                )

    # -------------------------------------------------
    # Cleanup
    # -------------------------------------------------

    def cleanup(self, directory: Path) -> None:
        """
        Remove temporary update files.
        """

        if directory.exists():
            shutil.rmtree(
                directory,
                ignore_errors=True,
            )

    # -------------------------------------------------
    # Full Installation
    # -------------------------------------------------

    def install_package(
        self,
        package: Path,
    ) -> bool:
        """
        Extract and install a package.
        """

        extracted = self.extract(package)

        self.install(extracted)

        self.cleanup(extracted)

        return True

    # -------------------------------------------------
    # Representation
    # -------------------------------------------------

    def __repr__(self) -> str:
        return f"<UpdateInstaller " f"directory='{self.install_directory}'>"
