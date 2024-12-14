from typing import List
from sqlalchemy.orm import Session

from app.models.example import Example

def get_all_examples(db: Session) -> List[Example]:
    return db.query(Example).all()