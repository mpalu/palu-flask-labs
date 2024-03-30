"""
This module contains the Items class.
"""


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
        Retrieves all items.

        Returns:
            list: A list of all items.
        """
        pass
