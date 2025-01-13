from uuid import UUID
from datetime import datetime

# schema
from app.schemas.storage_unit.storage_unit_base import StorageUnitBase

class StorageUnit(StorageUnitBase):
	id: UUID
	created_at: datetime
	updated_at: datetime
	
	class Config:
		from_attributes = True