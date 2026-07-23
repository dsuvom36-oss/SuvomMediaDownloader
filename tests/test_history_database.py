"""
tests/test_history_database.py
"""

from types import SimpleNamespace

import pytest

from core.history import HistoryDatabase


@pytest.fixture
def db(tmp_path, monkeypatch):
    import sqlite3

    connection = sqlite3.connect(":memory:")
    connection.row_factory = sqlite3.Row

    monkeypatch.setattr(
        "core.history.sqlite3.connect",
        lambda *args, **kwargs: connection,
    )

    database = HistoryDatabase()

    monkeypatch.setattr(
        "core.history.event_bus.publish",
        lambda *args, **kwargs: None,
    )

    yield database

    database.close()


@pytest.fixture
def sample_task():
    return SimpleNamespace(
        name="Test Download",
        status="Completed",
        created_at="2026-07-23 10:00:00",
        finished_at="2026-07-23 10:05:00",
    )


def test_create_table(db):
    assert db.count() == 0


def test_add_task(db, sample_task):
    db.add_task(sample_task)

    assert db.count() == 1


def test_get_all(db, sample_task):
    db.add_task(sample_task)

    rows = db.get_all()

    assert len(rows) == 1
    assert rows[0].task_name == "Test Download"


def test_search(db, sample_task):
    db.add_task(sample_task)

    rows = db.search("Test")

    assert len(rows) == 1


def test_search_not_found(db):
    assert db.search("Nothing") == []


def test_delete(db, sample_task):
    db.add_task(sample_task)

    record = db.get_all()[0]

    db.delete(record.id)

    assert db.count() == 0


def test_clear(db, sample_task):
    db.add_task(sample_task)
    db.add_task(sample_task)

    assert db.count() == 2

    db.clear()

    assert db.count() == 0


def test_export_csv(db, sample_task, tmp_path):
    db.add_task(sample_task)

    filename = tmp_path / "history.csv"

    result = db.export_csv(filename)

    assert filename.exists()
    assert str(result) == str(filename)


def test_count(db):
    assert db.count() == 0


def test_close(db):
    db.close()
