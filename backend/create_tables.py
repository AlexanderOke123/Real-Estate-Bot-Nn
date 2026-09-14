"""
Quick script to create all tables in MySQL.
Run once after creating the database:

    python create_tables.py
"""
from app.db.session import engine, Base
from app.models import Lead, Conversation, Message  # noqa: F401

if __name__ == "__main__":
    print("Creating tables in MySQL...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created successfully.")
