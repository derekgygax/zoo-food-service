from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from sqlalchemy.orm import load_only
from typing import List
from sqlalchemy.orm import Session

# Models
from app.models.storage_unit_type import StorageUnitType

# Schemas
from app.schemas.model_identifier import ModelIdentifier
from app.schemas.storage_unit_type.storage_unit_type_base import StorageUnitTypeBase

def _validate_storage_unit_type_exists(db: Session, storage_unit_type_id: str) -> None:
    if not db.query(StorageUnitType).filter_by(id=storage_unit_type_id).first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Storage unit type '{storage_unit_type_id}' does not exist."
        )
    



def get_all_storage_unit_types(db: Session) -> List[StorageUnitType]:
    return db.query(StorageUnitType).all()

def get_all_storage_unit_type_ids(db: Session) -> List[str]:
    storage_unit_types = db.query(StorageUnitType).options(
        load_only(
            StorageUnitType.id
        )
    ).all()
    return [
        type.id for type in storage_unit_types
    ]

def get_all_storage_unit_type_bases(db: Session) -> List[StorageUnitTypeBase]:
    storage_unit_type = db.query(StorageUnitType).options(
        load_only(
            StorageUnitType.id,
            StorageUnitType.description
        )
    ).all()
    return [
        StorageUnitTypeBase.model_validate(type) for type in storage_unit_type
    ]

def get_all_storage_unit_type_identifiers(db: Session) -> List[ModelIdentifier]:
    storage_unit_type_ids = get_all_storage_unit_type_ids(db=db)
    return [
        ModelIdentifier(id=str(id), label=str(id)) for id in storage_unit_type_ids
    ]

def get_storage_unit_type_base_by_id(db: Session, storage_unit_type_id: str) -> StorageUnitTypeBase:
    storage_unit_type = db.query(StorageUnitType).filter(StorageUnitType.id == storage_unit_type_id).options(
        load_only(
            StorageUnitType.id,
            StorageUnitType.description
        )
    ).first()

    if not storage_unit_type:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Storage Unit Type with the id ${storage_unit_type_id} not found"
        )
    
    return storage_unit_type

def add_storage_unit_type(db: Session, storage_unit_type_base: StorageUnitTypeBase) -> None:
    db_storage_unit_type = StorageUnitType(**storage_unit_type_base.model_dump())
    try:
        db.add(db_storage_unit_type)
        db.commit()
        db.refresh(db_storage_unit_type)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Storage unit type with ID '{db_storage_unit_type.id}' already exists."
        )

def update_storage_unit_type(db: Session, storage_unit_type_id: str, storage_unit_type: StorageUnitTypeBase) -> None:
    db_storage_unit_type = db.query(StorageUnitType).filter(
        StorageUnitType.id == storage_unit_type_id
    ).first()

    if db_storage_unit_type is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Storage unit type '{storage_unit_type_id}' not found"
        )

    # Update fields
    db_storage_unit_type.description = storage_unit_type.description

    db.commit()
    db.refresh(db_storage_unit_type)
