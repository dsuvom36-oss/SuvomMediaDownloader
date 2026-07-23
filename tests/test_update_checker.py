"""
tests/test_update_checker.py
"""


from updater.update_checker import UpdateChecker


def test_current_version():
    checker = UpdateChecker()

    assert checker.current_version() is not None


def test_latest_version():
    checker = UpdateChecker()

    assert checker.latest_version() is not None


def test_update_available_returns_bool():
    checker = UpdateChecker()

    assert isinstance(checker.is_update_available(), bool)


def test_manifest_returns_dict():
    checker = UpdateChecker()

    assert isinstance(checker.manifest(), dict)


def test_release_notes():
    checker = UpdateChecker()

    assert isinstance(checker.release_notes(), str)


def test_download_url():
    checker = UpdateChecker()

    assert isinstance(checker.download_url(), str)


def test_refresh():
    checker = UpdateChecker()

    checker.refresh()

    assert checker.latest_version() is not None


def test_repr():
    checker = UpdateChecker()

    assert "UpdateChecker" in repr(checker)
