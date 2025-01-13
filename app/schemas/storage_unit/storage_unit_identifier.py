from uuid import UUID
from pydantic import BaseModel, Field
from datetime import date

class StorageUnitIdentifier(BaseModel):
	id: UUID = Field(..., title="ID", description="The unique identifier for the storage unit")
	name: str = Field(..., title="Name", max_length=100, description="The name of the storage unit")
	storage_unit_type_id: str = Field(..., title="Storage Unit Type", format="selector", max_length=100, description="The type of storage unit, such as 'freezer' or 'dry storage'")
	
	class Config:
		json_encoders = {date: lambda v: v.isoformat()}
		from_attributes = True
	
