from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase

from backend.controllers.access import (
    create_user_controller,
    get_users_controller,
    create_card_controller,
    get_cards_controller,
    revoke_card_controller,
    activate_card_controller,
)

from backend.db.database import get_database

from backend.models.access import User, RFIDCard

router = APIRouter()


@router.post("/users", status_code=201)
async def create_user(
    user: User,
    db: AsyncIOMotorDatabase = Depends(get_database)
):
    return await create_user_controller(user, db)


@router.get("/users")
async def get_users(
    db: AsyncIOMotorDatabase = Depends(get_database)
):
    return await get_users_controller(db)


@router.post("/cards", status_code=201)
async def create_card(
    card: RFIDCard,
    db: AsyncIOMotorDatabase = Depends(get_database)
):
    return await create_card_controller(card, db)


@router.get("/cards")
async def get_cards(
    db: AsyncIOMotorDatabase = Depends(get_database)
):
    return await get_cards_controller(db)


@router.patch("/cards/{uid}/revoke")
async def revoke_card(
    uid: str,
    db: AsyncIOMotorDatabase = Depends(get_database)
):
    return await revoke_card_controller(uid, db)


@router.patch("/cards/{uid}/activate")
async def activate_card(
    uid: str,
    db: AsyncIOMotorDatabase = Depends(get_database)
):
    return await activate_card_controller(uid, db)