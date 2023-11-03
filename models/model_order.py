from typing import Optional, TYPE_CHECKING
from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy import DateTime

from sqlmodel import Field, Relationship, Column, SQLModel

if TYPE_CHECKING:
    from .user import User

class Order(SQLModel, table= True):
    id: Optional[int] = Field(default=None, primary_key= True)
    total_price: Optional[float] = Field(default=None)
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    updated_at: Optional[datetime] = Field(sa_column=Column(
        DateTime(timezone=True),
        nullable=True,
        server_default=func.now(),
        server_onupdate=func.now(),
    ))
    deleted_at: Optional[datetime] = Field(nullable=True)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    
    user: Optional["User"] = Relationship(back_populates="orders")