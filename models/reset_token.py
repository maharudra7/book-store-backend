from typing import Optional
from sqlmodel import Field, SQLModel
from sqlalchemy.sql import func
from datetime import datetime


class Reset_Token(SQLModel, table= True):
    id: Optional[int] = Field(default=None, primary_key= True)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    token: str = Field(nullable= False)
    created_at: Optional[str] = Field(default_factory=datetime.utcnow, nullable=True)



