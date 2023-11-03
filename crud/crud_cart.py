from sqlmodel import Session, select
from models.model_cart import Cart
from sqlalchemy.sql import func
from config import db
from fastapi import HTTPException

async def create_cart(cart:Cart):
    with Session(db.engine) as session:
        session.add(cart)
        session.commit()
        session.refresh(cart)
        return cart
    
async def get_cart(cart_id:int):
    with Session(db.engine) as session:
        statement = select(Cart).where(Cart.id == cart_id)
        db_cart = session.exec(statement).first()
        if db_cart is None:
            raise HTTPException(status_code=404, detail="Cart not found")
        else:
            return db_cart
        
async def update_cart(cart_id: int, updated_cart: Cart):
    with Session(db.engine) as session:
        statement =  select(Cart).where(Cart.id == cart_id)
        db_cart = session.exec(statement).first()
        if db_cart is None:
            raise HTTPException(status_code=404, datail= "Cart not found")
        else:
            db_cart.quantity = updated_cart.quantity
            session.add(db_cart)
            session.commit()
            session.refresh(db_cart)
            return db_cart

async def delete_cart(cart_id: int):
    with Session(db.engine) as session: 
        statement = select(Cart).where(Cart.id == cart_id)
        db_cart = session.exec(statement).first()
        if db_cart is None:
            raise HTTPException(status_code=404, detail = "Card not found")
        else:
            
            session.add(db_cart)
            session.commit()
            return {"Message": "Cart Deleted"}