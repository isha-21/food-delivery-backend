from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    phone: str

class OrderCreate(BaseModel):
    user_id: UUID
    restaurant_id: UUID

class RatingCreate(BaseModel):
    order_id: UUID
    restaurant_rating: int = Field(..., ge=1, le=5)
    delivery_rating: int = Field(..., ge=1, le=5)
    comment: Optional[str] = None
