from uuid import UUID
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import date

class FoodStockBase(BaseModel):

    food_type_id: str = Field(..., title="Food Type", format="selector", max_length=100, description="The unique identifier for the type of food, such as 'meat' or 'seed'")
    storage_unit_id: UUID = Field(..., title="Storage Unit", format="selector", description="The unique identifier for the storage unit, this is a UUID")
    quantity: int = Field(..., title="Quanitity of Food", ge=0, description="The quantity of the food of that type")
    expiration_date: date = Field(..., title="Expiration Date", description="The date of the expiration of the food")

    @model_validator(mode="after")
    def check_capacity(cls, model):
        if model.quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        return model

    class Config:
        json_encoders = {date: lambda v: v.isoformat()}
        from_attributes = True
