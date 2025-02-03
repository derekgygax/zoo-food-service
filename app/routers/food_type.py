from typing import List, Dict, Any
from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

# local
from app.database import get_db

# schemas
from app.schemas.food_type.food_type import FoodType
from app.schemas.food_type.food_type_base import FoodTypeBase

# services
from app.schemas.model_identifier import ModelIdentifier
from app.services import food_types_service

router = APIRouter(prefix="/api/v1/food-types")

@router.get("", tags=["food_type"], response_model=List[FoodType])
async def get_food_types(db: Session = Depends(get_db)):
	return food_types_service.get_all_food_types(db=db)

@router.get("/ids", tags=["food_type"], response_model=List[str])
async def get_food_type_ids(db: Session = Depends(get_db)):
	return food_types_service.get_all_food_type_ids(db=db)

@router.get("/identifiers", tags=["food_type"], response_model=List[ModelIdentifier])
async def get_food_type_identifiers(db: Session = Depends(get_db)):
	return food_types_service.get_all_food_type_identifiers(db=db)

@router.get("/{food_type_id}/base", tags=["food_type"], response_model=FoodTypeBase)
async def get_food_type_base_by_id(food_type_id: str, db: Session = Depends(get_db)):
	return food_types_service.get_food_type_base_by_id(db=db, food_type_id=food_type_id)

@router.post("", tags=["food_type"], status_code=status.HTTP_201_CREATED, response_model=None)
async def add_food_type(
    food_type_base: FoodTypeBase,
    db: Session = Depends(get_db),
):
    food_types_service.add_food_type(db=db, food_type_base=food_type_base)
    return

@router.put("/{food_type_id}", tags=["food_type"], status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def update_food_type(
    food_type_id: str,
    food_type_base: FoodTypeBase,
    db: Session = Depends(get_db),
):
    food_types_service.update_food_type(db=db, food_type_id=food_type_id, food_type_base=food_type_base)
    return