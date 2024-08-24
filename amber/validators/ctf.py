from typing import List
from pydantic import BaseModel

class PostFlags(BaseModel):
    flags: List[str]
