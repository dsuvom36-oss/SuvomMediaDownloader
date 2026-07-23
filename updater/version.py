"""
updater/version.py

Version class for comparing semantic versions.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import total_ordering


@total_ordering
@dataclass(frozen=True)
class Version:
    """
    Represents a semantic version.

    Examples:
        Version("1.0.0")
        Version("2.5")
        Version("3")
    """

    major: int
    minor: int = 0
    patch: int = 0

    def __init__(self, version: str | tuple[int, int, int]):
        if isinstance(version, str):
            parts = version.strip().split(".")

            numbers = []

            for part in parts[:3]:
                try:
                    numbers.append(int(part))
                except ValueError:
                    numbers.append(0)

            while len(numbers) < 3:
                numbers.append(0)

            object.__setattr__(self, "major", numbers[0])
            object.__setattr__(self, "minor", numbers[1])
            object.__setattr__(self, "patch", numbers[2])

        elif isinstance(version, tuple):
            major, minor, patch = version
            object.__setattr__(self, "major", major)
            object.__setattr__(self, "minor", minor)
            object.__setattr__(self, "patch", patch)

        else:
            raise TypeError("Version must be initialized with a string or tuple.")

    # -------------------------------------------------
    # Comparison
    # -------------------------------------------------

    def _tuple(self):
        return (
            self.major,
            self.minor,
            self.patch,
        )

    def __eq__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self._tuple() == other._tuple()

    def __lt__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self._tuple() < other._tuple()

    # -------------------------------------------------
    # String Representation
    # -------------------------------------------------

    def __str__(self):
        return f"{self.major}." f"{self.minor}." f"{self.patch}"

    def __repr__(self):
        return f"Version('{self}')"

    # -------------------------------------------------
    # Utilities
    # -------------------------------------------------

    def to_tuple(self):
        return self._tuple()

    def to_dict(self):
        return {
            "major": self.major,
            "minor": self.minor,
            "patch": self.patch,
        }

    @classmethod
    def parse(cls, version: str):
        """
        Create a Version instance from a string.
        """
        return cls(version)
