from fastapi import FastAPI

# Create the most basic FastAPI app possible
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from Vercel!", "status": "working"}

@app.get("/test")
def test():
    return {"test": "success", "platform": "vercel"}

# Export for Vercel (multiple ways to ensure compatibility)
handler = app
application = app
