
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter()

@router.post("/restaurants")
def add_restaurant(restaurant: schemas.RestaurantCreate, db: Session = Depends(database.get_db)):
    return crud.create_restaurant(db, restaurant)

@router.post("/restaurants/menu_items")
def add_menu_item(item: schemas.MenuItemCreate, db: Session = Depends(database.get_db)):
    return crud.create_menu_item(db, item)

@router.put("/restaurants/{restaurant_id}/status")
def update_status(restaurant_id: str, status: schemas.RestaurantStatusUpdate, db: Session = Depends(database.get_db)):
    return crud.update_restaurant_status(db, restaurant_id, status)

@router.put("/orders/status")
def update_order_status(order_update: schemas.OrderUpdate, db: Session = Depends(database.get_db)):
    return crud.update_order_status(db, order_update.order_id, order_update.status)

