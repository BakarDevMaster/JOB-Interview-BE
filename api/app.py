from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World", "status": "working"}

@app.get("/api/test")
def test_endpoint():
    return {"message": "API is working on Vercel!", "endpoint": "test"}
