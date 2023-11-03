from typing import Optional, List
from datetime import datetime
from sqlalchemy.sql import func
from sqlmodel import Field, Column, SQLModel
from sqlalchemy import DateTime
from pydantic import  ValidationError, validator


class Author(SQLModel, table= True):
    id: Optional[int] = Field(default=None, primary_key= True)
    name: str = Field(max_length= 100, nullable=False)
    description: str = Field(max_length= 500, nullable=False)
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    updated_at: Optional[datetime] = Field(sa_column=Column(
        DateTime(timezone=True),
        nullable=True,
        server_default=func.now(),
        server_onupdate=func.now(),
    ))
    deleted_at: Optional[datetime] = Field(nullable=True)

    @validator('name')
    def name_is_required(cls, v):
        if len(v)==0:
            raise ValueError('Name is required')
        return v.title()

    @validator('description')
    def description_is_required(cls, v):
        if len(v)==0:
            raise ValueError('Description is required')
        return v.title()

    @validator('description')
    def description_length(cls, v):
        if len(v)>250:
            raise ValueError('Description length exceeds')
        return v.title()


