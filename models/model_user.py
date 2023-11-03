from typing import Optional, List, TYPE_CHECKING
from datetime import datetime
from sqlalchemy.sql import func
from sqlmodel import Field, Relationship, Column, SQLModel
from sqlalchemy import DateTime

if TYPE_CHECKING:
    from .order import Order

class UserBase(SQLModel):
    username: str = Field(max_length= 50 ,nullable=False)
    password: str = Field(nullable=False)

class UserPassword(UserBase):
    new_password: str 


class ResetPassword(UserBase):
    token: str


class User(SQLModel, table= True):
    id: Optional[int] = Field(default=None, primary_key= True)
    username: str = Field(max_length= 50 ,nullable=False)
    password: str = Field(nullable=False)
    email_verified: bool = Field(default=False)
    created_at: Optional[str] = Field(default_factory=datetime.utcnow, nullable=True)
    updated_at: Optional[str] = Field(sa_column=Column(
        DateTime(timezone=True),
        nullable=True,
        server_default=func.now(),
        server_onupdate=func.now(),
    ))
    deleted_at: Optional[str] = Field(nullable=True)

    orders: List["Order"] = Relationship(back_populates="user")
    



    
