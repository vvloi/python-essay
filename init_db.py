"""
Database Initialization Script
Automatically creates database tables without using Alembic
Run this for quick setup
"""

from backend.database import engine, Base

def init_database():
    """Initialize database tables

    WARNING: This will delete all existing data in the database.
    All tables will be dropped and recreated, resulting in complete data loss.
    """
    print("=" * 60)
    print("Initializing Recipe Book Database...")
    print("=" * 60)

    try:
        # Drop all existing tables (for fresh start)
        print("\n[1/2] Dropping existing tables...")
        Base.metadata.drop_all(bind=engine)
        print("✓ Existing tables dropped")

        # Create all tables
        print("\n[2/2] Creating new tables...")
        Base.metadata.create_all(bind=engine)
        print("✓ Tables created successfully")

        print("\n" + "=" * 60)
        print("Database Schema Created:")
        print("=" * 60)
        print("  ✓ recipes")
        print("  ✓ ingredients")
        print("  ✓ steps")
        print("  ✓ pantry")
        print("\n✅ Database initialization complete!")
        print("\nYou can now run:")
        print("  uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000")

    except Exception as e:
        print(f"\n❌ Error initializing database: {str(e)}")
        raise

if __name__ == "__main__":
    init_database()
