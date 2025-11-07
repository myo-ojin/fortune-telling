"""
Flask application factory.
"""
from flask import Flask
from config import config

def create_app(config_name='development'):
    """
    Create and configure the Flask application.

    Args:
        config_name (str): Configuration name ('development', 'testing', 'production')

    Returns:
        Flask: Configured Flask application instance
    """
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(config[config_name])

    # Register blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
