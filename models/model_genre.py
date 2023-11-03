from typing import Optional, List
from datetime import datetime
from sqlalchemy.sql import func
from sqlmodel import Field, Column, SQLModel
from sqlalchemy import DateTime


class Genre(SQLModel, table= True):
    id: Optional[int] = Field(default=None, primary_key= True)
    title: str = Field(max_length= 100 ,nullable=False)
    description: str = Field(max_length= 200 ,nullable=False) 
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    updated_at: Optional[datetime] = Field(sa_column=Column(
        DateTime(timezone=True),
        nullable=True,
        server_default=func.now(),
        server_onupdate=func.now(),
    ))
    deleted_at: Optional[datetime] = Field(nullable=True)