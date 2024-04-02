"""
This module contains the main Flask application object.
"""

import logging
from flask import Flask
from flask_wtf import CSRFProtect
from src.app.models.items import Items
from src.app.controllers.routes import register_routes

app = Flask(__name__)
csrf = CSRFProtect()

register_routes(app)


def create_app():
    """
    Creates and returns the Flask application object.

    Returns:
        Flask: The Flask application object.
    """
    return app


if __name__ != "__main__":
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

if __name__ == "__main__":
    Items.insert_initial_data()
    csrf.init_app(app)
