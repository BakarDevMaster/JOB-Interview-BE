from sqlmodel import SQLModel, Session, create_engine
from app.settings import DATABASE_URL

# Use the actual secret value and ensure the psycopg v3 driver is used
connection_string = DATABASE_URL.get_secret_value()

# Normalize to psycopg v3 driver URL if user provided plain postgresql://
if connection_string.startswith("postgresql://") and "+" not in connection_string.split(":", 1)[0]:
    connection_string = connection_string.replace("postgresql://", "postgresql+psycopg://", 1)

engine = create_engine(
    connection_string,
    pool_recycle=300,
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    
def get_session():
    with Session(engine) as session:
        yield session
