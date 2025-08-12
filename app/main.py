# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import create_db_and_tables
from contextlib import asynccontextmanager
from app.routers.users import router as users_router
from app.routers.categories import router as categories_router
from app.routers.session import router as session_router
import os

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Only create tables if not in Vercel environment
    if not os.getenv("VERCEL"):
        create_db_and_tables()
    yield

app = FastAPI(
    lifespan=lifespan,
    title="Interview Management Microservice",
    version="1.0.0",
)

# CORS Configuration
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    # Add other allowed origins here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # Allow cookies to be sent
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users_router)
app.include_router(categories_router)
app.include_router(session_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Interview Management API", "status": "success", "platform": "vercel"}

@app.get("/welcome")
def welcome():
    return {"message": "Simple welcome API endpoint", "working": True, "timestamp": "2025-01-12"}

# Export for Vercel
handler = app
