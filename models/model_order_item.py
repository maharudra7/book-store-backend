from typing import Optional, List
from datetime import datetime
from sqlalchemy.sql import func
from sqlmodel import Field, Column, SQLModel
from sqlalchemy import DateTime

class OrderItem(SQLModel, table= True):
    id: Optional[int] = Field(default=None, primary_key= True)
    quantity: Optional[int] = Field(default=0)
    order_id: Optional[int] = Field(default=None, foreign_key="order.id")
    item_id: Optional[int] = Field(default=None, foreign_key="item.id")
    created_at: datetime = Field(default_factory=datetime.utcnow(), nullable=True)
    updated_at: Optional[datetime] = Field(sa_column=Column(
        DateTime(timezone=True),
        nullable=True,
        server_default=func.now(),
        server_onupdate=func.now(),
    ))
    deleted_at: datetime = Field(nullable=True)
