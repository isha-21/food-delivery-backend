from uuid import UUID
from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import HTTPException

def create_restaurant(db: Session, restaurant: schemas.RestaurantCreate):
    db_restaurant = models.Restaurant(**restaurant.dict())
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant

def create_menu_item(db: Session, item: schemas.MenuItemCreate):
    db_item = models.MenuItem(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_order_status(db: Session, order_id: UUID, status: str):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order.status = status
    db.commit()
    db.refresh(order)
    return order

def update_restaurant_status(db: Session, restaurant_id: str, status_data: schemas.RestaurantStatusUpdate):
    restaurant = db.query(models.Restaurant).filter(models.Restaurant.id == restaurant_id).first()
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    restaurant.is_online = status_data.is_online
    db.commit()
    db.refresh(restaurant)
    return restaurant

# def update_order_status(db: Session, order_id, status):
#     order = db.query(models.Order).filter(models.Order.id == order_id).first()
#     if not order:
#         raise HTTPException(status_code=404, detail="Order not found")
#     order.status = status
#     db.commit()
#     db.refresh(order)
#     return order