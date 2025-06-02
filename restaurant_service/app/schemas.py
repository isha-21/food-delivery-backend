from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class RestaurantCreate(BaseModel):
    name: str
    is_online: Optional[bool] = True

class MenuItemCreate(BaseModel):
    restaurant_id: UUID
    name: str
    price: float
    available: Optional[bool] = True

class OrderUpdate(BaseModel):
    order_id: UUID
    status: str  # accepted, rejected, preparing, etc.

class RestaurantStatusUpdate(BaseModel):
    is_online: bool

