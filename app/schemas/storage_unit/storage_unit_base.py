from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import date

class StorageUnitBase(BaseModel):
    name: str = Field(..., title="Name", max_length=100, description="The name of the storage unit")
    storage_unit_type_id: str = Field(..., title="Storage Unit Type", format="selector", max_length=100, description="The type of storage unit, such as 'freezer' or 'dry storage'")
    capacity: int = Field(..., title="Capacity")

    @model_validator(mode="after")
    def check_capacity(cls, model):
        if model.capacity < 0:
            raise ValueError("Capacity must be greater than or equal to 0")
        return model

    class Config:
        json_encoders = {date: lambda v: v.isoformat()}
        from_attributes = True
