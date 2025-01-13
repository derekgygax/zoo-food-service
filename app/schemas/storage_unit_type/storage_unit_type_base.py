from pydantic import BaseModel, Field
from datetime import date


class StorageUnitTypeBase(BaseModel):
	id: str = Field(..., max_length=100, title="Storage Unit Type", description="Unique identifier for the storage unit type, such as 'freezer' or 'dry storage'. white space is converted to _ before insertion to the DB")
	description: str = Field(..., max_length=500, title="Storage Unit Type Description", description="A short description about the storage unit type")
	
	class Config:
		json_encoders = {date: lambda v: v.isoformat()}
		from_attributes = True
	
