from typing import List, Dict, Any
from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

# local
from app.database import get_db

# schemas
from app.schemas.storage_unit_type.storage_unit_type import StorageUnitType
from app.schemas.storage_unit_type.storage_unit_type_base import StorageUnitTypeBase

# services
from app.services.storage_unit_types import( 
    get_all_storage_unit_types, 
    get_all_storage_unit_type_ids,
    get_all_storage_unit_type_bases,
	add_storage_unit_type as add_storage_unit_type_service,
	update_storage_unit_type as update_storage_unit_type_service
)

router = APIRouter(prefix="/api/v1/storage-unit-types")


# GET METHODS
@router.get("/",  tags=["storage_unit_type"], response_model=List[StorageUnitType])
async def get_storage_unit_types(db: Session = Depends(get_db)):
	return get_all_storage_unit_types(db=db)

@router.get("/ids", tags=["storage_unit_type"], response_model=List[str])
async def get_storage_unit_types_ids(db: Session = Depends(get_db)):
	return get_all_storage_unit_type_ids(db=db)

@router.get("/base", tags=["storage_unit_type"], response_model=List[StorageUnitTypeBase])
async def get_storage_unit_type_bases(db: Session = Depends(get_db)):
	return get_all_storage_unit_type_bases(db=db)


# POST METHODS
@router.post("/", tags=["storage_unit_type"], status_code=status.HTTP_201_CREATED, response_model=None)
async def add_storage_unit_type(
	storage_unit_type_base: StorageUnitTypeBase,
	# current_user: JWT = Depends(get_current_user),
	db: Session = Depends(get_db)
):
	add_storage_unit_type_service(db = db, storage_unit_type_base = storage_unit_type_base)
	return

# PUT METHODS

@router.put("/{storage_unit_type_id}", tags=["storage_unit_type"], status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def update_storage_unit_type(
	storage_unit_type_id: str,
	storage_unit_type_base: StorageUnitTypeBase,
	# current_user: JWT = Depends(get_current_user),
	db: Session = Depends(get_db)
):
	update_storage_unit_type_service(db=db, storage_unit_type_id=storage_unit_type_id, storage_unit_type_base=storage_unit_type_base)
	return

