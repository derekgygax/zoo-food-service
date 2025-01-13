from sqlalchemy.orm import load_only
from typing import List
from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

# models
from app.models.food_stock import FoodStock

def get_all_food_stocks(db: Session) -> List[FoodStock]:
    return db.query(FoodStock).all()

