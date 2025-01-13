from typing import List, Dict, Any
from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

# local
from app.database import get_db

# models
from app.schemas.storage_unit.storage_unit import StorageUnit

# services
from app.services.storage_units import get_all_storage_unit_identifiers, get_all_storage_units

router = APIRouter(prefix="/api/v1/storage-units")

@router.get("/", response_model=List[StorageUnit])
async def get_storage_units(db: Session = Depends(get_db)):
	return get_all_storage_units(db=db)

@router.get("/identifiers", response_model=List[str])
async def get_storage_unit_identifiers(db: Session = Depends(get_db)):
	return get_all_storage_unit_identifiers(db=db)
