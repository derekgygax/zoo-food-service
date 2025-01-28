from re import S
from sqlalchemy.orm import load_only
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from typing import List
from sqlalchemy.orm import Session

# models
from app.models.food_type import FoodType

# schemas
from app.schemas.food_type.food_type_base import FoodTypeBase
from app.schemas.model_identifier import ModelIdentifier

def _validate_food_type_exists(db: Session, food_type_id: str) -> None:
    """
    Validate that a food type exists in the database.
    """
    if not db.query(FoodType).filter_by(id=food_type_id).first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Food type '{food_type_id}' does not exist."
        )

def get_all_food_types(db: Session) -> List[FoodType]:
    return db.query(FoodType).all()

def get_all_food_type_ids(db: Session) -> List[str]:
    food_types = db.query(FoodType).options(
        load_only(
            FoodType.id
        )
    ).all()
    return [
        type.id for type in food_types
    ]

def get_all_food_type_identifiers(db: Session) -> List[ModelIdentifier]:
    food_type_ids = get_all_food_type_ids(db=db)
    return [
        ModelIdentifier(id=str(id), label=str(id)) for id in food_type_ids
    ]

def get_food_type_base_by_id(db: Session, food_type_id: str) -> FoodTypeBase:
    food_type = db.query(FoodType).filter(FoodType.id == food_type_id).options(
        load_only(
            FoodType.id,
            FoodType.description
        )
    ).first()

    if not food_type:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Food Type with the id ${food_type_id} not found"
        )
    
    return food_type

def add_food_type(db: Session, food_type_base: FoodTypeBase) -> None:
    """
    Add a new food type to the database.
    """
    db_food_type = FoodType(**food_type_base.model_dump())
    try:
        db.add(db_food_type)
        db.commit()
        db.refresh(db_food_type)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Food type with ID '{db_food_type.id}' already exists."
        )

def update_food_type(db: Session, food_type_id: str, food_type_base: FoodTypeBase) -> None:
    """
    Update an existing food type in the database.
    """
    db_food_type = db.query(FoodType).filter(
        FoodType.id == food_type_id
    ).first()

    if db_food_type is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Food type '{food_type_id}' not found."
        )

    # Update fields
    db_food_type.description = food_type_base.description

    db.commit()
    db.refresh(db_food_type)