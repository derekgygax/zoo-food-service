from sqlalchemy.orm import load_only
from typing import List
from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

# models
from app.models.storage_unit import StorageUnit

# schemas
from app.schemas.storage_unit.storage_unit_identifier import StorageUnitIdentifier

def get_all_storage_units(db: Session) -> List[StorageUnit]:
    return db.query(StorageUnit).all()

# Get an identification portion for all the animals
def get_all_storage_unit_identifiers(db: Session) -> List[StorageUnitIdentifier]:
    storage_units = db.query(StorageUnit).options(
        load_only(
            StorageUnit.id,
            StorageUnit.name,
            StorageUnit.storage_unit_type_id
        )
    ).all()
    return [
        StorageUnitIdentifier.model_validate(unit) for unit in storage_units
    ]
