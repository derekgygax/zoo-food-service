from typing import Optional, List
from pydantic import BaseModel
from uuid import UUID
from datetime import date, datetime

# local
from app.enums.example import EXAMPLE

class ExampleBase(BaseModel):
	name: str
	type: EXAMPLE

class Example(ExampleBase):
	id: UUID
	created_at: datetime
	updated_at: datetime
	
	class Config:
		from_attributes = True