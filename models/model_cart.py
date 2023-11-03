from typing import Optional
from datetime import datetime
from sqlalchemy.sql import func
from sqlmodel import Field, Column, SQLModel 
from sqlalchemy import DateTime


class Cart(SQLModel, table= True):
    id: Optional[int] = Field(default=None, primary_key= True)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    quantity: Optional[int] = Field(default=0)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=True)
    updated_at: Optional[datetime] = Field(sa_column=Column(
        DateTime(timezone=True),
        nullable=True,
        server_default=func.now(),
        server_onupdate=func.now(),
    ))
    