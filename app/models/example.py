
from sqlalchemy import Column, Enum, String, Date, DateTime, func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, validates
from uuid import uuid4
from datetime import datetime
import pytz

# Local
from app.database import Base
from app.enums.example import EXAMPLE

# NOTE!!:
#   You do NOT need name to define the column name unless the 
#   the column name is different than the attribute
#   This is just there to show how

class Example(Base):
    __tablename__ = "example"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, name="id")
    name = Column(String(100), nullable=False, name="name")
    type = Column(Enum(EXAMPLE), nullable=False)

    # Timestamps - keep track of when entry was created and updated. maybe need in future
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.UTC), nullable=False, name="created_at")
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.UTC), onupdate=func.now(), nullable=False, name="updated_at")

    @validates('created_at')
    def validate_created_at(self, key, value):
        # Raise an error if `created_at` is attempted to be changed
        if getattr(self, key) is not None:
            raise ValueError("The `created_at` field cannot be modified after creation.")
        return value

# TODO FOR RETRIEVING THE TIMEZONE!!
# # Assuming `post.created_at` is a timezone-aware datetime in UTC
# user_timezone = pytz.timezone("America/New_York")  # Example user timezone
# local_time = post.created_at.astimezone(user_timezone)
# print(local_time)  # This will display the time converted to the user's timezone