from typing import Optional

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from backend.core.config import get_settings

settings = get_settings()

client: Optional[AsyncIOMotorClient] = None
database: Optional[AsyncIOMotorDatabase] = None


async def connect_db():
    global client, database
    client = AsyncIOMotorClient(settings.MONGODB_URL)
    database = client[settings.DATABASE_NAME]

async def disconnect_db():
    global client
    if client:
        client.close()


async def get_database() -> AsyncIOMotorDatabase:
    if database is None:
        raise RuntimeError("Database not connected. Call connect_db() first.")
    return database