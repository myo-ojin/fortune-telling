"""
Configuration file for the Fortune Telling application.
"""
import os

# Base directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Base configuration."""

    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-please-change-in-production'

    # Database settings
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'data', 'fortune.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Application settings
    FORTUNE_METHODS_COUNT = 5  # Number of fortune telling methods (minimum requirement)

    # Default values for missing birth information
    DEFAULT_BIRTH_TIME = '12:00'  # Noon
    DEFAULT_BIRTH_PLACE = '東京'  # Tokyo
    DEFAULT_LATITUDE = 35.6895
    DEFAULT_LONGITUDE = 139.6917
    DEFAULT_TIMEZONE = 'Asia/Tokyo'

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    TESTING = False

class TestingConfig(Config):
    """Testing configuration."""
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    TESTING = False

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
