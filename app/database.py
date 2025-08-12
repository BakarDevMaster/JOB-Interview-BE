from sqlmodel import SQLModel, Session, create_engine
from app.settings import DATABASE_URL
import os

# Use the actual secret value and ensure the psycopg v3 driver is used
# Starlette's Secret object needs to be cast to string, not use get_secret_value()
connection_string = str(DATABASE_URL)

# Handle common PostgreSQL URL issues for Vercel deployment
if connection_string:
    # Fix deprecated postgres:// scheme to postgresql://
    if connection_string.startswith("postgres://"):
        connection_string = connection_string.replace("postgres://", "postgresql://", 1)
    
    # Ensure psycopg driver is specified for SQLAlchemy
    if connection_string.startswith("postgresql://") and "+" not in connection_string.split(":", 1)[0]:
        connection_string = connection_string.replace("postgresql://", "postgresql+psycopg://", 1)
else:
    # Fallback for missing DATABASE_URL (should not happen in production)
    raise ValueError("DATABASE_URL environment variable is not set")

engine = create_engine(
    connection_string,
    pool_recycle=300,
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    
def get_session():
    with Session(engine) as session:
        yield session
