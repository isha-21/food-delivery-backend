from pydantic import BaseModel, UUID4
from enum import Enum
from typing import Optional
from datetime import datetime

class DeliveryStatus(str, Enum):
    pending = "pending"
    picked_up = "picked_up"
    on_the_way = "on_the_way"
    delivered = "delivered"
    cancelled = "cancelled"

class DeliveryAgentBase(BaseModel):
    name: str
    is_available: Optional[bool] = True

class DeliveryAgentCreate(DeliveryAgentBase):
    pass

class DeliveryAgent(DeliveryAgentBase):
    id: UUID4

    class Config:
        orm_mode = True

class OrderStatusUpdate(BaseModel):
    order_id: UUID4
    status: DeliveryStatus

class Order(BaseModel):
    id: UUID4
    status: DeliveryStatus
    delivery_agent_id: Optional[UUID4] = None
    updated_at: datetime

    class Config:
        orm_mode = True
