import datetime
from sqlmodel import Session, select
from sqlmodel import Session
from models.model_order import Order
from models.model_user import User
from fastapi import HTTPException
from config import db
from sqlalchemy.sql import func

async def get_all_order():
    with Session(db.engine) as session:
        statement = select(Order).where(Order.deleted_at == None) 
        db_order = session.exec(statement).all()
        return db_order

async def create_order(order:Order):
    with Session(db.engine) as session:
        statement = select(User).where(User.id == order.user_id)
        db_user = session.exec(statement).first()
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        if db_user.deleted_at is not None:
            raise HTTPException(status_code=404, detail="User is Inactive")
        session.add(order)
        session.commit()
        session.refresh(order)
        return order
        
async def get_order(order_id:int):
    with Session(db.engine) as session:
        statement = select(Order).where(Order.id == order_id)
        db_order = session.exec(statement).first()
        if db_order is None:
            raise HTTPException(status_code=404, detail="Order not found")
        else:
            if db_order.deleted_at is not None:
                raise HTTPException(status_code=404, detail="Order is Inactive")
            
            return db_order
        
async def update_order(order_id: int ,updated_order: Order):
    with Session(db.engine) as session:
        statement = select(Order).where(Order.id == order_id)
        db_order = session.exec(statement).first()
        if db_order is None:
            raise HTTPException(status_code = 404, detail="Order not found")

        else:
            db_order.total_price = updated_order.total_price
            session.add(db_order)
            session.commit()
            session.refresh(db_order)
            return db_order
            
        
async def delete_order(order_id: int):
    with Session(db.engine) as session:
          statement = select(Order).where(Order.id == order_id)
          db_order = session.exec(statement).first()
         
          if db_order is None:
              raise HTTPException(status_code=404, detail="Order not found")
          else:
              db_order.deleted_at = func.now()
              session.add(db_order)
              session.commit()
              return {"message": "Order Deleted"}
              