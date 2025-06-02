from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import crud, schemas, database

router = APIRouter()

@router.post("/agents", response_model=schemas.DeliveryAgent)
def create_agent(agent: schemas.DeliveryAgentCreate, db: Session = Depends(database.get_db)):
    return crud.create_delivery_agent(db, agent)

@router.put("/orders/status", response_model=schemas.Order)
def update_order_status(order_status: schemas.OrderStatusUpdate, db: Session = Depends(database.get_db)):
    return crud.update_order_status(db, order_status.order_id, order_status.status)

@router.put("/agents/{agent_id}/availability", response_model=schemas.DeliveryAgent)
def update_agent_availability(agent_id: str, is_available: bool, db: Session = Depends(database.get_db)):
    return crud.set_agent_availability(db, agent_id, is_available)
