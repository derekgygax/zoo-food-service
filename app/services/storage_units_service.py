from sqlalchemy.orm import load_only
from typing import List
from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

# models
from app.models.storage_unit import StorageUnit

# schemas
from app.schemas.model_identifier import ModelIdentifier
from app.schemas.storage_unit.storage_unit_identifier import StorageUnitIdentifier
from app.schemas.storage_unit.storage_unit_base import StorageUnitBase

# services
from app.services.storage_unit_types_service import _validate_storage_unit_type_exists


def _validate_storage_unit_exists(db: Session, storage_unit_id: UUID) -> None:
    """
    Validate that the storage unit exists in the database.
    """
    if not db.query(StorageUnit).filter_by(id=storage_unit_id).first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Storage Unit does not exist."
        )
    


def get_all_storage_units(db: Session) -> List[StorageUnit]:
    return db.query(StorageUnit).all()

# Get an identification portion for all the animals
def get_all_storage_unit_identifiers(db: Session) -> List[ModelIdentifier]:
    storage_units = db.query(StorageUnit).options(
        load_only(
            StorageUnit.id,
            StorageUnit.name,
        )
    ).all()
    return [
        ModelIdentifier(id=str(unit.id), label=str(unit.name)) for unit in storage_units
    ]

def get_storage_unit_base_by_id(db: Session, storage_unit_id: UUID) -> StorageUnitBase:

    storage_unit = db.query(StorageUnit).filter(StorageUnit.id == storage_unit_id).options(
        load_only(
            StorageUnit.name,
            StorageUnit.storage_unit_type_id,
            StorageUnit.capacity,
        )
    ).first()

    if not storage_unit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Storage Unit not found"
        )
    
    return StorageUnitBase.model_validate(storage_unit)


def add_storage_unit(db: Session, storage_unit_base: StorageUnitBase) -> None:

    # Check if the specie exists
    _validate_storage_unit_type_exists(db, storage_unit_base.storage_unit_type_id)

    db_storage_unit = StorageUnit(**storage_unit_base.model_dump())
    db.add(db_storage_unit)
    db.commit()
    db.refresh(db_storage_unit)
    return

def update_storage_unit(db: Session, storage_unit_id: UUID, storage_unit_base: StorageUnitBase) -> None:

    # Check if the specie exists
    _validate_storage_unit_type_exists(db, storage_unit_base.storage_unit_type_id)

    db_storage_unit = db.query(StorageUnit).filter(StorageUnit.id == storage_unit_id).first()
    if db_storage_unit is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Storage Unit not found"
        )

    # Update fields
    db_storage_unit.name = storage_unit_base.name
    db_storage_unit.storage_unit_type_id = storage_unit_base.storage_unit_type_id
    db_storage_unit.capacity = storage_unit_base.capacity

    db.commit()
    db.refresh(db_storage_unit)
    return
