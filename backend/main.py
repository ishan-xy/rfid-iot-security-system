from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from backend.core.config import get_settings
from backend.db.database import connect_db, disconnect_db
from backend.routers.access import router as access_router

settings = get_settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db()
    yield
    await disconnect_db()

app = FastAPI(
    title="RFID Access Control API",
    description="API for managing users and RFID cards for access control",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(access_router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}