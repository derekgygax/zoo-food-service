from sqlalchemy.orm import load_only
from typing import List
from sqlalchemy.orm import Session

from app.models.food_type import FoodType

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
