from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter()

@router.post("/users")
def register_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return crud.create_user(db, user)

@router.post("/orders")
def place_order(order: schemas.OrderCreate, db: Session = Depends(database.get_db)):
    return crud.create_order(db, order)

@router.post("/ratings")
def leave_rating(rating: schemas.RatingCreate, db: Session = Depends(database.get_db)):
    return crud.create_rating(db, rating)
