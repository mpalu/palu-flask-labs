"""
This module contains the home controller blueprint.

It defines routes for rendering the index.html template.
"""

from flask import Blueprint, render_template

home_bp = Blueprint("home_bp", __name__)


@home_bp.route("/")
def index():
    """
    Render the index.html template.

    Returns:
        The rendered index.html template.
    """
    return render_template("index.html")
