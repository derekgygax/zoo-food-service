from sqlalchemy import Column, Enum, Integer, String, Date, DateTime, func, ForeignKey, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, validates
from uuid import uuid4
from datetime import datetime
import pytz

# Local
from app.database import Base

class FoodStock(Base):
    __tablename__ = "food_stock"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, name="id")
    food_type_id = Column(String(100), ForeignKey("food_type.id", ondelete="RESTRICT"), nullable=False, name="food_type_id")
    storage_unit_id = Column(UUID(as_uuid=True), ForeignKey("storage_unit.id", ondelete="RESTRICT"), nullable=False, name="storage_unit_id")
    quantity = Column(Integer, nullable=False, name="quantity")
    expiration_date = Column(Date, nullable=False, name="expiration_date")

    # Relationship to the food_type
    food_type = relationship("FoodType", foreign_keys=[food_type_id], back_populates="food_stocks")

    # Relationship to the storage_unit food_type
    storage_unit = relationship("StorageUnit", foreign_keys=[storage_unit_id], back_populates="food_stocks")

    # Timestamps - keep track of when entry was created and updated. maybe need in future
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.UTC), nullable=False, name="created_at")
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.UTC), onupdate=func.now(), nullable=False, name="updated_at")

    # Ensure that capacity doesn't isn't negative
    __table_args__ = (
        CheckConstraint('quantity >= 0', name='check_quantity_non_negative'),
    )

    @validates('created_at')
    def validate_created_at(self, key, value):
        # Raise an error if `created_at` is attempted to be changed
        if getattr(self, key) is not None:
            raise ValueError("The `created_at` field cannot be modified after creation.")
        return value