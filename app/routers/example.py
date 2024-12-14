from typing import List, Dict, Any
from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

# local
from app.schemas.example import Example
from app.database import get_db
from app.services.example import get_all_examples


router = APIRouter(prefix="/api/v1/examples")

@router.get("/", response_model=List[Example])
async def get_animals(db: Session = Depends(get_db)):
	return get_all_examples(db=db)