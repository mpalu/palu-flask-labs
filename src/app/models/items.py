"""
This module contains the Items class.
"""

import logging
from typing import Optional

from src.app.models.database import DatabaseException, open_connection


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
    def get_all() -> list:
        """
        Retrieves all items from the database.

        Returns:
            list: A list of all items.
        """

        conn = open_connection()
        c = conn.cursor()
        c.execute("SELECT id, name, description FROM items")
        items = c.fetchall()
        conn.close()
        return [Items(*item) for item in items]

    @staticmethod
    def get(item_id: int) -> Optional["Items"]:
        """
        Retrieves an item from the database by its ID.

        Args:
            item_id (int): The ID of the item to retrieve.

        Returns:
            Optional["Items"]: The item with the specified ID,
            or None if the item does not exist.
        """
        conn = open_connection()
        c = conn.cursor()
        c.execute(
            "SELECT id, name, description FROM items WHERE id = ?", (item_id,)
        )  # pylint: disable=line-too-long
        item = c.fetchone()
        conn.close()
        if item:
            return Items(*item)
        else:
            return None

    def add(self):
        """
        Saves the item to the database.
        """
        conn = open_connection()
        c = conn.cursor()
        c.execute(
            "INSERT INTO items (id, name, description) VALUES (?, ?, ?)",
            (self.id, self.name, self.description),
        )
        conn.commit()
        conn.close()

    @staticmethod
    def create_table_items():
        """
        Creates a table 'items' in the database if it doesn't already exist.

        The table has the following columns:
        - id: INTEGER (Primary Key)
        - name: TEXT (Not Null)
        - description: TEXT

        This function connects to the database, creates the table, and commits
        the changes.

        Args:
            None

        Returns:
            None
        """
        conn = None

        try:
            conn = open_connection()
            c = conn.cursor()

            logging.debug("Checking if table 'items' exists...")
            c.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='items'"  # pylint: disable=line-too-long
            )
            table_exists = c.fetchone()
            if table_exists:
                logging.debug(
                    "Table 'items' already exists. Skipping creation."
                )  # pylint: disable=line-too-long
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


if __name__ == "__main__":
    Items.create_table_items()
