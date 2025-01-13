from datetime import datetime

# schema
from app.schemas.food_type.food_type_base import FoodTypeBase


class FoodType(FoodTypeBase):
	created_at: datetime
	updated_at: datetime
	
	class Config:
		from_attributes = True