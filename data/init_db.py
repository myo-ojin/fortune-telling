"""
Database initialization script.

This script creates all database tables defined in the models.
Run this script to initialize the database before using the application.

Usage:
    python data/init_db.py
"""
import sys
import os

# Add parent directory to path to import app modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from app.database import db
from app.models import (
    FortuneMethod,
    ZodiacSign,
    TarotCard,
    NumerologyMeaning,
    IChingHexagram,
    ShichuStem,
    ShichuBranch
)


def init_database():
    """
    Initialize the database by creating all tables.
    """
    # Create app with development configuration
    app = create_app('development')
    
    with app.app_context():
        print("Initializing database...")
        print(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
        
        # Drop all existing tables (use with caution!)
        print("\nDropping existing tables (if any)...")
        db.drop_all()
        
        # Create all tables
        print("\nCreating tables...")
        db.create_all()
        
        # Verify tables were created
        print("\nTables created successfully:")
        tables = [
            ('fortune_methods', FortuneMethod),
            ('zodiac_signs', ZodiacSign),
            ('tarot_cards', TarotCard),
            ('numerology_meanings', NumerologyMeaning),
            ('iching_hexagrams', IChingHexagram),
            ('shichu_stems', ShichuStem),
            ('shichu_branches', ShichuBranch)
        ]
        
        for table_name, model in tables:
            print(f"  ✓ {table_name} ({model.__name__})")
        
        print("\n✅ Database initialization complete!")
        print(f"Database file: {os.path.join(os.path.dirname(__file__), 'fortune.db')}")


if __name__ == '__main__':
    init_database()
