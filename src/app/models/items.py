"""
This module contains the Items class.
"""

import logging
import sqlite3
from src.app.models.database import DatabaseException, DATABASE_PATH


class Items:
    """
    Represents a collection of items.
    """

    def __init__(self, item_id: int, name: str, description: str) -> None:
        """
        Initializes a new instance of the Items class.

        Args:
            item_id (int): The ID of the item.
            name (str): The name of the item.
            description (str): The description of the item.
        """
        self.id = item_id
        self.name = name
        self.description = description

    @staticmethod
    def all() -> list:
        """
        Retrieves all items from the database.

        Returns:
            list: A list of all items.
        """

        Items.create_table_items()
        Items.insert_initial_data()

        conn = sqlite3.connect(DATABASE_PATH)
        c = conn.cursor()
        c.execute("SELECT id, name, description FROM items")
        items = c.fetchall()
        conn.close()
        return [Items(*item) for item in items]

    @staticmethod
    def insert_initial_data():
        """
        Inserts initial data into the database.

        Returns:
            None
        """
        initial_data = [
            (1, "Item 1", "Description for item 1"),
            (2, "Item 2", "Description for item 2"),
            (3, "Item 3", "Description for item 3"),
        ]
        conn = sqlite3.connect(DATABASE_PATH)
        c = conn.cursor()
        for item in initial_data:
            c.execute("SELECT id FROM items WHERE id = ?", (item[0],))
            existing_item = c.fetchone()
            if existing_item:
                print(f"Item {item[0]} already exists. Skipping insertion.")
            else:
                c.execute(
                    "INSERT INTO items (id, name, description) VALUES (?, ?, ?)",
                    (item[0], item[1], item[2]),
                )
        conn.commit()
        conn.close()

    @staticmethod
    def create_table_items():
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
        try:
            logging.debug("Connecting to databse '%s'...", DATABASE_PATH)
            conn = sqlite3.connect(DATABASE_PATH)
            c = conn.cursor()

            logging.debug("Checking if table 'items' exists...")
            c.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='items'"
            )
            table_exists = c.fetchone()
            if table_exists:
                logging.debug("Table 'items' already exists. Skipping creation.")
                return

            logging.debug("Creating table 'items'...")
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

        except DatabaseException as e:
            logging.error("Error creating table: %s", e)

        finally:
            if conn:
                conn.close()
