"""
tests/test_version.py

Unit tests for updater.version.Version
"""

import pytest

from updater.version import Version


def test_equal_versions():
    assert Version("1.0.0") == Version("1.0.0")


def test_less_than():
    assert Version("1.0.0") < Version("1.1.0")


def test_greater_than():
    assert Version("2.0.0") > Version("1.9.9")


def test_parse_two_parts():
    assert Version("2.5").to_tuple() == (2, 5, 0)


def test_parse_one_part():
    assert Version("3").to_tuple() == (3, 0, 0)


def test_tuple_constructor():
    assert Version((1, 2, 3)).to_tuple() == (1, 2, 3)


def test_string_output():
    assert str(Version("2.1.4")) == "2.1.4"


def test_repr():
    assert repr(Version("1.0.0")) == "Version('1.0.0')"


def test_to_dict():
    assert Version("2.4.6").to_dict() == {
        "major": 2,
        "minor": 4,
        "patch": 6,
    }


def test_invalid_type():
    with pytest.raises(TypeError):
        Version(123)
