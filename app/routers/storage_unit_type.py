from typing import List, Dict, Any
from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

# local
from app.database import get_db

# models
from app.schemas.storage_unit_type.storage_unit_type import StorageUnitType

# services
from app.services.storage_unit_types import get_all_storage_unit_types, get_all_storage_unit_type_ids

router = APIRouter(prefix="/api/v1/storage-unit-types")

@router.get("/", response_model=List[StorageUnitType])
async def get_storage_unit_types(db: Session = Depends(get_db)):
	return get_all_storage_unit_types(db=db)

@router.get("/ids", response_model=List[str])
async def get_storage_unit_types_ids(db: Session = Depends(get_db)):
	return get_all_storage_unit_type_ids(db=db)
