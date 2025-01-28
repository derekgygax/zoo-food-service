from sqlalchemy.orm import load_only
from typing import List
from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

# models
from app.models.food_stock import FoodStock

# schemas
from app.schemas.food_stock.food_stock_base import FoodStockBase

# services
from app.services.food_types import _validate_food_type_exists
from app.services.storage_unit_types import _validate_storage_unit_type_exists
from app.services.storage_units import _validate_storage_unit_exists

def get_all_food_stocks(db: Session) -> List[FoodStock]:
    return db.query(FoodStock).all()


def get_food_stock_base_by_id(db: Session, food_stock_id: UUID) -> FoodStockBase:

    food_stock = db.query(FoodStock).filter(FoodStock.id == food_stock_id).options(
        load_only(
            FoodStock.food_type_id,
            FoodStock.storage_unit_id,
            FoodStock.quantity,
            FoodStock.expiration_date
        )
    ).first()

    if not food_stock:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Food Stock not found"
        )
    
    return FoodStockBase.model_validate(food_stock)



def add_food_stock(db: Session, food_stock_base: FoodStockBase) -> None:

    # Check if the unit exists
    _validate_storage_unit_exists(db, food_stock_base.storage_unit_id)

    # Check if the food type exists
    _validate_food_type_exists(db, food_stock_base.food_type_id)

    db_food_stock = FoodStock(**food_stock_base.model_dump())
    db.add(db_food_stock)
    db.commit()
    db.refresh(db_food_stock)
    return



def update_food_stock(db: Session, food_stock_id: UUID, food_stock_base: FoodStockBase) -> None:

    # Check if the unit exists
    _validate_storage_unit_exists(db, food_stock_base.storage_unit_id)

    # Check if the food type exists
    _validate_food_type_exists(db, food_stock_base.food_type_id)

    db_food_stock = db.query(FoodStock).filter(FoodStock.id == food_stock_id).first()
    if db_food_stock is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Food Stock not found"
        )

    # Update fields
    db_food_stock.food_type_id = food_stock_base.food_type_id
    db_food_stock.storage_unit_id = food_stock_base.storage_unit_id
    db_food_stock.quantity = food_stock_base.quantity
    db_food_stock.expiration_date = food_stock_base.expiration_date

    db.commit()
    db.refresh(db_food_stock)
    return
