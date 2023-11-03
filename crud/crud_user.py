from datetime import datetime
from sqlmodel import Session, select
from models.model_user import User, UserBase
from fastapi import HTTPException
from config import db
from sqlalchemy.sql import func
from auth.utils import get_password, verify_password


async def get_all_user():
    with Session(db.engine) as session:
        statement = select(User).where(User.deleted_at == None) 
        db_user = session.exec(statement).all()
        return db_user

async def create_user(payload:UserBase):
    with Session(db.engine) as session:
        hash_password = get_password(payload.password)
        new_user = User(username=payload.username, password=hash_password)
        # new_user.password = hash_password
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user
        
async def get_user(user_id:int):
    with Session(db.engine) as session:
        statement = select(User).where(User.id == user_id)
        db_user = session.exec(statement).first()
        if db_user is None:
           raise HTTPException(status_code=404, detail="User not found")
        else:
            if db_user.deleted_at is not None:
                raise HTTPException(status_code=404, detail="User is Inactive")
            
            return db_user 

        
async def update_user(user_id: int, updated_user: User):
    with Session(db.engine) as session:
        statement = select(User).where(User.id == user_id)
        db_user = session.exec(statement).first()
        if db_user is None:
            raise HTTPException(status_code = 404, detail="User not found")
        else:
            db_user.username = updated_user.username
            session.add(db_user)
            session.commit()
            session.refresh(db_user)
            return db_user
            
# this is soft delete        
async def delete_user(user_id: int):
    with Session(db.engine) as session:
          statement = select(User).where(User.id == user_id)
          db_user = session.exec(statement).first()
          if db_user is None:
               raise HTTPException(status_code=404, detail="User not found")
          else:
              db_user.deleted_at = func.now()
              session.add(db_user)
              session.commit()
              return {"message": "User Deleted"}
             