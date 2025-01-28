from typing import List, Dict, Any
from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

# local
from app.database import get_db

# schema
from app.schemas.storage_unit.storage_unit import StorageUnit
from app.schemas.storage_unit.storage_unit_base import StorageUnitBase
from app.schemas.storage_unit.storage_unit_identifier import StorageUnitIdentifier

# services
from app.services import storage_units_service

router = APIRouter(prefix="/api/v1/storage-units")

@router.get("/", response_model=List[StorageUnit])
async def get_storage_units(db: Session = Depends(get_db)):
	return storage_units_service.get_all_storage_units(db=db)

@router.get("/identifiers", response_model=List[StorageUnitIdentifier])
async def get_storage_unit_identifiers(db: Session = Depends(get_db)):
	return storage_units_service.get_all_storage_unit_identifiers(db=db)

@router.get("/{storage_unit_id}", response_model=StorageUnitBase)
async def get_storage_unit_base_by_id(storage_unit_id: UUID, db: Session = Depends(get_db)):
    return storage_units_service.get_storage_unit_base_by_id(db=db, storage_unit_id=storage_unit_id)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=None)
async def add_storage_unit(
    storage_unit_base: StorageUnitBase,
    db: Session = Depends(get_db),
):
    storage_units_service.add_storage_unit(db=db, storage_unit_base=storage_unit_base)
    return


@router.put("/{storage_unit_id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def update_storage_unit(
    storage_unit_id: UUID,
    storage_unit_base: StorageUnitBase,
    db: Session = Depends(get_db),
):
    storage_units_service.update_storage_unit(db=db, storage_unit_id=storage_unit_id, storage_unit_base=storage_unit_base)
    return