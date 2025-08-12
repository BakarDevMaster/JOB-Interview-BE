# Vercel entry point - imports the main application
from app.main import app

# Export for Vercel
handler = app
application = app
