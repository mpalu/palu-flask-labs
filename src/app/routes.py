"""
This module contains the routes for the Flask application.
"""

from flask import Blueprint, render_template
from .controllers.home import home_bp


home_bp = Blueprint("home_bp", __name__)
items_bp = Blueprint("items_bp", __name__)


def register_routes(app) -> None:
    """
    Register the routes for the Flask application.

    Args:
      app (Flask): The Flask application object.

    Returns:
      None
    """
    app.register_blueprint(home_bp)

    @app.route("/")
    def index():
        """
        Render the index.html template.

        Returns:
          str: The rendered HTML template.
        """
        return render_template("index.html")

    @app.route("/items")
    def items():
        """
        Render the items.html template.

        Returns:
          str: The rendered HTML template.
        """
        return render_template("items.html")
