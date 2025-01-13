from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import date

from app.schemas.food_stock.food_stock_base import FoodStockBase

class FoodStock(FoodStockBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
