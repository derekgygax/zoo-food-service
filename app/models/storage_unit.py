from sqlalchemy import Column, Enum, Integer, String, Date, DateTime, func, ForeignKey, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, validates
from uuid import uuid4
from datetime import datetime
import pytz

# Local
from app.database import Base

class StorageUnit(Base):
    __tablename__ = "storage_unit"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, name="id")
    name = Column(String(100), nullable=False, name="name")
    storage_unit_type_id = Column(String(100), ForeignKey("storage_unit_type.id", ondelete="RESTRICT"), nullable=False, name="storage_unit_type_id")
    capacity = Column(Integer, nullable=False, name="capacity")


    # TODO
    # current amount in the unit ... see if this can be done with other
    # things like you have done in the enclosures-service in Quarkus
    # between Enclosure and the AnimalAssignments


    # Timestamps - keep track of when entry was created and updated. maybe need in future
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.UTC), nullable=False, name="created_at")
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.UTC), onupdate=func.now(), nullable=False, name="updated_at")

    # Relationship to the storage_unit_type
    storage_unit_type = relationship("StorageUnitType", foreign_keys=[storage_unit_type_id], back_populates="storage_units")

    # Relationship to the food_stock
    food_stocks = relationship("FoodStock", back_populates="storage_unit", cascade="save-update")

    # Ensure that capacity doesn't isn't negative
    __table_args__ = (
        CheckConstraint('capacity >= 0', name='check_capacity_non_negative'),
    )

    @validates('created_at')
    def validate_created_at(self, key, value):
        # Raise an error if `created_at` is attempted to be changed
        if getattr(self, key) is not None:
            raise ValueError("The `created_at` field cannot be modified after creation.")
        return value