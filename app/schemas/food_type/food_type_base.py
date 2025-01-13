from pydantic import BaseModel, Field
from datetime import date


class FoodTypeBase(BaseModel):
	id: str = Field(..., max_length=100, title="Food Type", description="Unique identifier for the food type, such as 'meat' or 'seed'")
	description: str = Field(..., max_length=500, title="Food Type Description", description="A short description about the type of food")
	
	class Config:
		json_encoders = {date: lambda v: v.isoformat()}
		from_attributes = True
	
