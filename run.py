"""
Application entry point.

This script runs the Flask development server.
"""
import os
from app import create_app

# Get configuration from environment variable, default to 'development'
config_name = os.environ.get('FLASK_ENV', 'development')

# Create the Flask application
app = create_app(config_name)

if __name__ == '__main__':
    # Run the development server
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
