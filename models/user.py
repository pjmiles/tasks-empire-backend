from typing import Optional
from uuid import UUID
import sqlalchemy as sa
from config.db import Base


class Users(Base):
    __tablename__ = "users"

    id: Optional[UUID] = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    email = sa.Column(sa.String)
    password = sa.Column(sa.String)
