from typing import Optional
from sqlmodel import Field, SQLModel, Column
from sqlalchemy.sql import func
from datetime import datetime
from sqlalchemy import DateTime

class Coupon(SQLModel, table= True):
    id: Optional[int] = Field(default=None, primary_key= True)
    coupon_code: str = Field(nullable= False)
    discount: float = Field(nullable= False) 
    unit: str = Field(nullable= False)
    max_amount: Optional[float] = Field(default= None)
    valid_from: Optional[datetime]  = Field(nullable= True)
    valid_to: Optional[datetime]  = Field(nullable= True)
    enabled: bool = Field(default= True)
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=True)
    updated_at: Optional[datetime] = Field(sa_column=Column(
        DateTime(timezone=True),
        nullable=True,
        server_default=func.now(),
        server_onupdate=func.now(),
    ))
    deleted_at: Optional[datetime] = Field(nullable=True)
