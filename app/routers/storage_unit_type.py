from typing import List, Dict, Any
from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

# local
from app.database import get_db

# schemas
from app.schemas.model_identifier import ModelIdentifier
from app.schemas.storage_unit_type.storage_unit_type import StorageUnitType
from app.schemas.storage_unit_type.storage_unit_type_base import StorageUnitTypeBase

# services
from app.services import storage_unit_types_service

router = APIRouter(prefix="/api/v1/storage-unit-types")


# GET METHODS
@router.get("",  tags=["storage_unit_type"], response_model=List[StorageUnitType])
async def get_storage_unit_types(db: Session = Depends(get_db)):
	return storage_unit_types_service.get_all_storage_unit_types(db=db)

@router.get("/ids", tags=["storage_unit_type"], response_model=List[str])
async def get_storage_unit_types_ids(db: Session = Depends(get_db)):
	return storage_unit_types_service.get_all_storage_unit_type_ids(db=db)

@router.get("/base", tags=["storage_unit_type"], response_model=List[StorageUnitTypeBase])
async def get_storage_unit_type_bases(db: Session = Depends(get_db)):
	return storage_unit_types_service.get_all_storage_unit_type_bases(db=db)

@router.get("/identifiers", tags=["food_type"], response_model=List[ModelIdentifier])
async def get_storage_unit_type_identifiers(db: Session = Depends(get_db)):
	return storage_unit_types_service.get_all_storage_unit_type_identifiers(db=db)

@router.get("/{storage_unit_type_id}/base", tags=["food_type"], response_model=StorageUnitTypeBase)
async def get_food_type_base_by_id(storage_unit_type_id: str, db: Session = Depends(get_db)):
	return storage_unit_types_service.get_storage_unit_type_base_by_id(db=db, storage_unit_type_id=storage_unit_type_id)


# POST METHODS
@router.post("", tags=["storage_unit_type"], status_code=status.HTTP_201_CREATED, response_model=None)
async def add_storage_unit_type(
	storage_unit_type_base: StorageUnitTypeBase,
	# current_user: JWT = Depends(get_current_user),
	db: Session = Depends(get_db)
):
	storage_unit_types_service.add_storage_unit_type(db = db, storage_unit_type_base = storage_unit_type_base)
	return

# PUT METHODS

@router.put("/{storage_unit_type_id}", tags=["storage_unit_type"], status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def update_storage_unit_type(
	storage_unit_type_id: str,
	storage_unit_type_base: StorageUnitTypeBase,
	# current_user: JWT = Depends(get_current_user),
	db: Session = Depends(get_db)
):
	storage_unit_types_service.update_storage_unit_type(db=db, storage_unit_type_id=storage_unit_type_id, storage_unit_type_base=storage_unit_type_base)
	return

