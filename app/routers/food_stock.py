from typing import List, Dict, Any
from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

# local
from app.database import get_db

# models
from app.schemas.food_stock.food_stock import FoodStock

# services
from app.services.food_stock import get_all_food_stocks

router = APIRouter(prefix="/api/v1/food-stocks")

@router.get("/", response_model=List[FoodStock])
async def get_food_stocks(db: Session = Depends(get_db)):
	return get_all_food_stocks(db=db)



# @router.post("/")
# async def add_food_stock(db: Session = Depends(get_db)):
	