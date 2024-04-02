"""
This module contains the database model for the application.
"""

import logging
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()

DATABASE_PATH = os.getenv("DATABASE_PATH")


class DatabaseException(Exception):
    """
    Represents a database error.
    """

    pass


def open_connection() -> sqlite3.Connection:
    """
    Opens a connection to the database.

    Returns:
        sqlite3.Connection: The database connection.
    """
    try:
        logging.info("Connecting to the database '%s'...", DATABASE_PATH)
        conn = sqlite3.connect(DATABASE_PATH)
        return conn
    except sqlite3.Error as e:
        raise DatabaseException(f"Error connecting to the database: {e}") from e
