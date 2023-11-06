from typing import Optional
import uuid
from pydantic import BaseModel, Field


class CreateUser(BaseModel):
    id: Optional[int]
    name: str
    email: str
    password: str
