"""
This module contains the database model for the application.
"""

import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_PATH = os.getenv("DATABASE_PATH", "data/palu_labs.db")


def create_table():
    """
    Creates a table named 'items' in the database if it doesn't already exist.

    The table has the following columns:
    - id: INTEGER (Primary Key)
    - name: TEXT (Not Null)
    - description: TEXT

    This function connects to the database, creates the table, and commits the
    changes.

    Args:
        None

    Returns:
        None
    """
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute(
        """
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT
            )
        """
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_table()
