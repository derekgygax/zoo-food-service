from sqlalchemy.orm import load_only
from typing import List
from sqlalchemy.orm import Session

from app.models.storage_unit_type import StorageUnitType

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
