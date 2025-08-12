# Vercel entry point - imports the main application
import sys
import os

# Ensure the current directory is in Python path for module resolution
if os.getcwd() not in sys.path:
    sys.path.insert(0, os.getcwd())

from app.main import app

# Export for Vercel
handler = app
application = app
