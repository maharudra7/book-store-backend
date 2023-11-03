from datetime import datetime
from sqlmodel import Session, select
from models.model_author import Author
from fastapi import HTTPException
from config import db
from sqlalchemy.sql import func

async def get_all_author():
    with Session(db.engine) as session:
        statement = select(Author).where(Author.deleted_at == None) 
        db_author = session.exec(statement).all()
        return db_author
    

async def create_author(payload:Author):
    with Session(db.engine) as session:
        new_author = Author(name=payload.name, description=payload.description)
        session.add(new_author)
        session.commit()
        session.refresh(new_author)
        return new_author
        
async def get_author(author_id:int):
    with Session(db.engine) as session:
        statement = select(Author).where(Author.id == author_id)
        db_author = session.exec(statement).first()
        if db_author is None:
           raise HTTPException(status_code=404, detail="Author not found")
        else:
            if db_author.deleted_at is not None:
                raise HTTPException(status_code=404, detail="Author is Inactive")
            
            return db_author
        

async def get_all_author():
    with Session(db.engine) as session:
        statement = select(Author).where(Author.deleted_at == None)
        db_author = session.exec(statement).all()
        return db_author


        
async def update_author(author_id: int, updated_author: Author):
    with Session(db.engine) as session:
        statement = select(Author).where(Author.id == author_id)
        db_author = session.exec(statement).first()
        if db_author is None:
            raise HTTPException(status_code = 404, detail="Author not found")
        else:
            db_author.name = updated_author.name
            db_author.description = updated_author.description
            session.add(db_author)
            session.commit()
            session.refresh(db_author)
            return db_author
            
# this is soft delete        
async def delete_author(author_id: int):
    with Session(db.engine) as session:
          statement = select(Author).where(Author.id == author_id)
          db_author = session.exec(statement).first()
          if db_author is None:
               raise HTTPException(status_code=404, detail="Author not found")
          else:
              db_author.deleted_at = func.now()
              session.add(db_author)
              session.commit()
              return {"message": "Author Deleted"}
             