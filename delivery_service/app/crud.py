from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException

def get_delivery_agent(db: Session, agent_id):
    return db.query(models.DeliveryAgent).filter(models.DeliveryAgent.id == agent_id).first()

def create_delivery_agent(db: Session, agent: schemas.DeliveryAgentCreate):
    db_agent = models.DeliveryAgent(name=agent.name, is_available=agent.is_available)
    db.add(db_agent)
    db.commit()
    db.refresh(db_agent)
    return db_agent

def update_order_status(db: Session, order_id, status: schemas.DeliveryStatus):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order.status = status
    db.commit()
    db.refresh(order)
    return order

def set_agent_availability(db: Session, agent_id, is_available: bool):
    agent = get_delivery_agent(db, agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Delivery agent not found")
    agent.is_available = is_available
    db.commit()
    db.refresh(agent)
    return agent
