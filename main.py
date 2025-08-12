# Root level main.py for Vercel compatibility
from app.main import app

# This is required for Vercel to detect the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
