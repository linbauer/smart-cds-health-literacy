from pydantic import BaseModel
from typing import List, Optional


class SimplifiedPatient(BaseModel):
    full_name: str
    birthDate: Optional[str]
