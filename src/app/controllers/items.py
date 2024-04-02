"""
This module contains the items controller blueprint.

It defines routes for rendering the items.html template.
"""

from flask import Blueprint, redirect, render_template, request, url_for

from src.app.models.items import Items

items_bp = Blueprint("items_bp", __name__)


@items_bp.route("/items", methods=["GET"])
def items():
    """
    Retrieves all items from the database.
    """
    all_items = Items.get_all()
    return render_template("items.html", items=all_items)


@items_bp.route("/items", methods=["POST"])
def add_item():
    """
    Add a new item to the database.
    """
    if request.method == "POST":
        item_id = request.form.get("id")
        name = request.form.get("name")
        description = request.form.get("description")

        existing_item = Items.get(item_id)
        if existing_item:
            return "Item already exists", 409  # 409 Conflict

        new_item = Items(item_id, name, description)
        new_item.add()

        return redirect(url_for("items_bp.items"))
    else:
        return "Invalid request method", 405  # 405 Method Not Allowed
