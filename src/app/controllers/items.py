"""
This module contains the items controller blueprint.

It defines routes for rendering the items.html template.
"""

from flask import Blueprint
from src.app.models.items import Items

items_bp = Blueprint("items_bp", __name__)


@items_bp.route("/items", methods=["GET"])
def get_all_items():
    """
    Retrieves all items from the database.
    """
    all_items = Items.all()
    return all_items
