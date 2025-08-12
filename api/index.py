# Vercel serverless function entry point
from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Create FastAPI app
app = FastAPI(title="Interview API", version="1.0.0")


@app.get("/")
def root():
    return {"message": "Interview API is live on Vercel!", "status": "success"}

@app.get("/health")
def health():
    return {"status": "healthy", "platform": "vercel"}

@app.get("/api/test")
def test():
    return {"message": "API endpoint working", "test": "passed"}

# Vercel handler
def handler(request):
    return app
