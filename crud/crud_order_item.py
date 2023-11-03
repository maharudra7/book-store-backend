from datetime import datetime
from sqlmodel import Session, select
from models.model_order_item import OrderItem
from fastapi import HTTPException
from config import db
from sqlalchemy.sql import func
    
async def get_all_order_item():
    with Session(db.engine) as session:
        statement = select(OrderItem).where(OrderItem.deleted_at == None) 
        db_order = session.exec(statement).all()
        return db_order
    
async def create_order_item(order_item:OrderItem):
    with Session(db.engine) as session:
        session.add(order_item)
        session.commit()
        session.refresh(order_item)
        return order_item
    
async def get_order_item(order_item_id:int):
    with Session(db.engine) as session:
        statement = select(OrderItem).where(OrderItem.id == order_item_id)
        db_order_item = session.exec(statement).first()
        if db_order_item is None:
           raise HTTPException(status_code=404, detail="OrderItem not found")
        else:
            return db_order_item
         
async def update_order_item(order_item_id: int, updated_order_item: OrderItem):
    with Session(db.engine) as session:
        statement = select(OrderItem).where(OrderItem.id == order_item_id)
        db_order_item = session.exec(statement).first()
        if db_order_item is None:
            raise HTTPException(status_code = 404, detail="OrderItem not found")
        else:
            db_order_item.quntity = updated_order_item.quantity
            session.add(db_order_item)
            session.commit()
            session.refresh(db_order_item)
            return db_order_item
        
async def delete_order_item(order_item_id: int):
    with Session(db.engine) as session:
          statement = select(OrderItem).where(OrderItem.id == "order_item.id")
          db_order_item = session.exec(statement).first()
          if db_order_item is None:
               raise HTTPException(status_code=404, detail="OrderItem not found")
          else:
              db_order_item.deleted_at = func.now()
              session.add(db_order_item)
              session.commit()
              return {"message": "OrderItem Deleted"}