from enum import Enum
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, field_validator


class PrivilegeLevel(str, Enum):
    guest = "guest"
    staff = "staff"
    supervisor = "supervisor"
    admin = "admin"


class User(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)

    email: EmailStr

    phone: str = Field(
        ...,
        pattern=r"^\+?[1-9]\d{6,14}$"
    )

    privilege_level: PrivilegeLevel = PrivilegeLevel.guest


class RFIDCard(BaseModel):
    uid: str = Field(..., min_length=4, max_length=32)

    assigned_user_id: Optional[str] = None

    is_active: bool = True

    @field_validator("uid")
    @classmethod
    def normalize_uid(cls, v: str):
        return v.upper().replace(" ", "")