from datetime import datetime

# schema
from app.schemas.storage_unit_type.storage_unit_type_base import StorageUnitTypeBase


class StorageUnitType(StorageUnitTypeBase):
	created_at: datetime
	updated_at: datetime
	
	class Config:
		from_attributes = True