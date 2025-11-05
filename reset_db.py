"""Reset PostgreSQL database - drop all tables"""
from backend.database import engine
from sqlalchemy import text

with engine.connect() as conn:
    # Drop and recreate public schema
    conn.execute(text("DROP SCHEMA public CASCADE"))
    conn.execute(text("CREATE SCHEMA public"))
    conn.commit()
    print("✅ Database reset successfully!")
