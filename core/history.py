import csv
import os
import sqlite3
from dataclasses import dataclass
from core.event_bus import event_bus
from core.event_types import Event

DATABASE = "database/history.db"

# Create database folder automatically
os.makedirs(os.path.dirname(DATABASE), exist_ok=True)


@dataclass
class HistoryRecord:
    id: int | None = None
    task_name: str = ""
    status: str = ""
    created_at: str = ""
    completed_at: str = ""


class HistoryDatabase:

    def __init__(self):

        self.connection = sqlite3.connect(DATABASE, check_same_thread=False)

        self.connection.row_factory = sqlite3.Row

        self.create_table()

    # ==========================================
    # Create Table
    # ==========================================

    def create_table(self):

        cursor = self.connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS history(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                task_name TEXT,

                status TEXT,

                created_at TEXT,

                completed_at TEXT
            )
        """)

        self.connection.commit()

    # ==========================================
    # Add Task
    # ==========================================

    def add_task(self, task):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO history
            (
                task_name,
                status,
                created_at,
                completed_at
            )
            VALUES (?, ?, ?, ?)
            """,
            (task.name, str(task.status), str(task.created_at), str(task.finished_at)),
        )

        self.connection.commit()

        event_bus.publish(Event.HISTORY_ADDED, task=task)

    # ==========================================
    # Get All
    # ==========================================

    def get_all(self):

        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT *
            FROM history
            ORDER BY id DESC
        """)

        rows = cursor.fetchall()

        return [
            HistoryRecord(
                id=row["id"],
                task_name=row["task_name"],
                status=row["status"],
                created_at=row["created_at"],
                completed_at=row["completed_at"],
            )
            for row in rows
        ]

    # ==========================================
    # Search
    # ==========================================

    def search(self, keyword):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM history
            WHERE task_name LIKE ?
               OR status LIKE ?
            ORDER BY id DESC
            """,
            (f"%{keyword}%", f"%{keyword}%"),
        )

        rows = cursor.fetchall()

        return [
            HistoryRecord(
                id=row["id"],
                task_name=row["task_name"],
                status=row["status"],
                created_at=row["created_at"],
                completed_at=row["completed_at"],
            )
            for row in rows
        ]

    # ==========================================
    # Delete
    # ==========================================

    def delete(self, record_id):

        cursor = self.connection.cursor()

        cursor.execute("DELETE FROM history WHERE id=?", (record_id,))

        self.connection.commit()

        event_bus.publish(Event.HISTORY_DELETED, record_id=record_id)

    # ==========================================
    # Clear
    # ==========================================

    def clear(self):

        cursor = self.connection.cursor()

        cursor.execute("DELETE FROM history")

        self.connection.commit()

        event_bus.publish(Event.HISTORY_CLEARED)

    # ==========================================
    # Export CSV
    # ==========================================

    def export_csv(self, file_path):

        rows = self.get_all()

        with open(file_path, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow(["Task Name", "Status", "Created At", "Completed At"])

            for row in rows:

                writer.writerow(
                    [row.task_name, row.status, row.created_at, row.completed_at]
                )

        event_bus.publish(Event.HISTORY_EXPORTED, file=file_path, count=len(rows))

        return file_path

    # ==========================================
    # Count
    # ==========================================

    def count(self):

        cursor = self.connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM history")

        return cursor.fetchone()[0]

    # ==========================================
    # Close
    # ==========================================

    def close(self):

        self.connection.close()

    # ==========================================
    # Context Manager
    # ==========================================

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
