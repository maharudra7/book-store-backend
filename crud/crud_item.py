from datetime import datetime
from sqlmodel import Session, select
from models.model_item import Item
from fastapi import HTTPException
from config import db
from sqlalchemy.sql import func


async def get_all_item():
    with Session(db.engine) as session:
        statement = select(Item).where(Item.deleted_at == None)
        db_item = session.exec(statement).all()
        return db_item


async def create_item(item: Item):
    with Session(db.engine) as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item


async def get_item(item_id: int):
    with Session(db.engine) as session:
        statement = select(Item).where(Item.id == item_id)
        db_item = session.exec(statement).first()
        if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        else:
            if db_item.deleted_at is not None:
                raise HTTPException(status_code=404, detail="Item is Inactive")

            return db_item


async def get_all_item():
    with Session(db.engine) as session:
        statement = select(Item).where(Item.deleted_at == None)
        db_item = session.exec(statement).all()
        return db_item


async def update_item(item_id: int, updated_item: Item):
    with Session(db.engine) as session:
        statement = select(Item).where(Item.id == item_id)
        db_item = session.exec(statement).first()
        if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        else:
            db_item.title = updated_item.title
            db_item.price = updated_item.price
            db_item.author_id = updated_item.author_id
            db_item.genre_id = updated_item.genre_id
            session.add(db_item)
            session.commit()
            session.refresh(db_item)
            return db_item


# this is soft delete
async def delete_item(item_id: int):
    with Session(db.engine) as session:
        statement = select(Item).where(Item.id == item_id)
        db_item = session.exec(statement).first()
        if db_item is None:
            raise HTTPException(status_code=404, detail="Item Not found")
        else:
            db_item.deleted_at = func.now()
            session.add(db_item)
            session.commit()
            return {"message": "Item Deleted"}
