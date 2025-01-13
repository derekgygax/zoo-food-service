from typing import List, Dict, Any
from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

# local
from app.database import get_db

# schemas
from app.schemas.food_type.food_type import FoodType

# services
from app.services.food_types import get_all_food_type_ids, get_all_food_types

router = APIRouter(prefix="/api/v1/food-types")

@router.get("/", response_model=List[FoodType])
async def get_food_types(db: Session = Depends(get_db)):
	return get_all_food_types(db=db)

@router.get("/ids", response_model=List[str])
async def get_food_type_ids(db: Session = Depends(get_db)):
	return get_all_food_type_ids(db=db)
