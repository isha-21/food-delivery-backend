from sqlalchemy import Column, String, Boolean, ForeignKey, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
import enum
from .database import Base
from datetime import datetime

class DeliveryStatus(str, enum.Enum):
    pending = "pending"
    picked_up = "picked_up"
    on_the_way = "on_the_way"
    delivered = "delivered"
    cancelled = "cancelled"

class DeliveryAgent(Base):
    __tablename__ = "delivery_agents"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    is_available = Column(Boolean, default=True)

    # Relationship: one agent can have many orders
    orders = relationship("Order", back_populates="delivery_agent")

class Order(Base):
    __tablename__ = "orders"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    status = Column(Enum(DeliveryStatus), default=DeliveryStatus.pending)
    delivery_agent_id = Column(UUID(as_uuid=True), ForeignKey("delivery_agents.id"), nullable=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    delivery_agent = relationship("DeliveryAgent", back_populates="orders")
