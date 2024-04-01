"""
This module contains the routes for the Flask application.
"""

from src.app.controllers.home import home_bp
from src.app.controllers.items import items_bp


def register_routes(app) -> None:
    """
    Register the routes for the Flask application.

    Args:
      app (Flask): The Flask application object.

    Returns:
      None
    """

    app.register_blueprint(home_bp)
    app.register_blueprint(items_bp)
