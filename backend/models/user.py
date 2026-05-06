from enum import Enum
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, EmailStr, Field, field_validator

class PrivilegeLevel(str, Enum):
    GUEST = "guest"
    STAFF = "staff"
    SUPERVISOR = "supervisor"
    ADMIN = "admin"


class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    phone: str = Field(
        ...,
        pattern=r"^\+?[1-9]\d{6,14}$"
    )
    privilege_level: PrivilegeLevel = PrivilegeLevel.GUEST


class RFIDCard(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    uid: str = Field(..., min_length=4, max_length=32)
    assigned_user_id: Optional[UUID] = None
    is_active: bool = True

    @field_validator("uid")
    @classmethod
    def normalize_uid(cls, v: str):
        return v.upper().replace(" ", "")