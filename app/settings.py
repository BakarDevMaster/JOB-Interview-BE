from starlette.config import Config
from starlette.datastructures import Secret
import os

# Initialize config with better error handling for Vercel
try:
    config = Config(".env")
except FileNotFoundError:
    # On Vercel, .env file won't exist, so use environment variables directly
    config = Config()

# Get DATABASE_URL with fallback to environment variable
try:
    DATABASE_URL = config("DATABASE_URL", cast=Secret)
except Exception:
    # Fallback to direct environment variable access for Vercel
    db_url = os.getenv("DATABASE_URL")
    if db_url:
        DATABASE_URL = Secret(db_url)
    else:
        raise ValueError("DATABASE_URL environment variable is required")

# Get TEST_DATABASE_URL with similar fallback
try:
    TEST_DATABASE_URL = config("TEST_DATABASE_URL", cast=Secret)
except Exception:
    test_db_url = os.getenv("TEST_DATABASE_URL", "")
    TEST_DATABASE_URL = Secret(test_db_url) if test_db_url else None
