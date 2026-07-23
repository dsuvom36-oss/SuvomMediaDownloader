"""
Shared pytest fixtures.
"""

from pathlib import Path

import pytest


@pytest.fixture
def temp_directory(tmp_path: Path):
    """Temporary directory for tests."""
    return tmp_path
