"""
This module contains the database model for the application.
"""

import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_PATH = os.getenv("DATABASE_PATH")


class DatabaseException(Exception):
    """
    Represents a database error.
    """

    pass
