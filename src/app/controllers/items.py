"""
This module contains the items controller blueprint.

It defines routes for rendering the items.html template.
"""

from flask import Blueprint, render_template

items_bp = Blueprint("items_bp", __name__)


@items_bp.route("/items")
def items():
    """
    Route handler for retrieving items.

    Returns:
        The rendered template for the items page.
    """
    return render_template("items.html")
