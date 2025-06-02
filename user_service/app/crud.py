from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="User with this email or phone already exists.")

def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(**order.model_dump())
    db.add(db_order)
    try:
        db.commit()
        db.refresh(db_order)
        return db_order
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Invalid order or duplicate entry.")

def create_rating(db: Session, rating: schemas.RatingCreate):
    db_rating = models.Rating(**rating.model_dump())
    db.add(db_rating)
    try:
        db.commit()
        db.refresh(db_rating)
        return db_rating
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Invalid rating or duplicate entry.")
