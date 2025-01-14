from typing import List, Dict, Any
from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

# local
from app.database import get_db

# schemas
from app.schemas.food_stock.food_stock import FoodStock
from app.schemas.food_stock.food_stock_base import FoodStockBase

# services
from app.services.food_stock import (
	get_all_food_stocks,
	get_food_stock_base_by_id as get_food_stock_base_by_id_service,
	add_food_stock as add_food_stock_service,
	update_food_stock as update_food_stock_service
)

router = APIRouter(prefix="/api/v1/food-stocks")

@router.get("/", response_model=List[FoodStock])
async def get_food_stocks(db: Session = Depends(get_db)):
	return get_all_food_stocks(db=db)

@router.get("/{food_stock_id}", response_model=FoodStockBase)
async def get_food_stock_base_by_id(
	food_stock_id: UUID,
	db: Session = Depends(get_db),
):
	return get_food_stock_base_by_id_service(db=db, food_stock_id=food_stock_id)


@router.post("/")
async def add_food_stock(
	food_stock_base: FoodStockBase, 
	db: Session = Depends(get_db)
):
	add_food_stock_service(db=db, food_stock_base=food_stock_base)
	return

@router.put("/{food_stock_id}")
async def add_food_stock(
	food_stock_id: UUID,
	food_stock_base: FoodStockBase, 
	db: Session = Depends(get_db)
):
	update_food_stock_service(
		db=db,
		food_stock_id=food_stock_id,
		food_stock_base=food_stock_base
	)
	return