from bson import ObjectId

from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase

from backend.models.access import User, RFIDCard


async def create_user_controller(
    user: User,
    db: AsyncIOMotorDatabase
):
    existing_user = await db["users"].find_one({
        "email": user.email
    })

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    user_data = user.model_dump()

    result = await db["users"].insert_one(user_data)

    user_data["_id"] = str(result.inserted_id)

    return user_data


async def get_users_controller(
    db: AsyncIOMotorDatabase
):
    users = await db["users"].find().to_list(length=100)

    for user in users:
        user["_id"] = str(user["_id"])

    return users


async def create_card_controller(
    card: RFIDCard,
    db: AsyncIOMotorDatabase
):
    existing_card = await db["cards"].find_one({
        "uid": card.uid.upper()
    })

    if existing_card:
        raise HTTPException(
            status_code=400,
            detail="Card already exists"
        )

    if card.assigned_user_id:
        try:
            user = await db["users"].find_one({
                "_id": ObjectId(card.assigned_user_id)
            })

        except:
            raise HTTPException(
                status_code=400,
                detail="Invalid user id"
            )

        if not user:
            raise HTTPException(
                status_code=404,
                detail="Assigned user not found"
            )

    card_data = card.model_dump()

    result = await db["cards"].insert_one(card_data)

    card_data["_id"] = str(result.inserted_id)

    return card_data


async def get_cards_controller(
    db: AsyncIOMotorDatabase
):
    cards = await db["cards"].find().to_list(length=100)

    for card in cards:
        card["_id"] = str(card["_id"])

    return cards


async def revoke_card_controller(
    uid: str,
    db: AsyncIOMotorDatabase
):
    result = await db["cards"].update_one(
        {"uid": uid.upper()},
        {"$set": {"is_active": False}}
    )

    if result.modified_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Card not found"
        )

    return {"message": "Card revoked"}


async def activate_card_controller(
    uid: str,
    db: AsyncIOMotorDatabase
):
    result = await db["cards"].update_one(
        {"uid": uid.upper()},
        {"$set": {"is_active": True}}
    )

    if result.modified_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Card not found"
        )

    return {"message": "Card activated"}