from datetime import datetime
from sqlmodel import Session, select
from models.model_genre import Genre
from fastapi import HTTPException
from config import db
from sqlalchemy.sql import func

async def get_all_genre():
    with Session(db.engine) as session:
        statement = select(Genre).where(Genre.deleted_at == None) 
        db_genre = session.exec(statement).all()
        return db_genre
    
async def create_genre(genre:Genre):
    with Session(db.engine) as session:
        session.add(genre)
        session.commit()
        session.refresh(genre)
        return genre
        
async def get_genre(genre_id:int):
    with Session(db.engine) as session:
        statement = select(Genre).where(Genre.id == genre_id)
        db_genre = session.exec(statement).first()
        if db_genre is None:
           raise HTTPException(status_code=404, detail="Genre not found")
        else:
            if db_genre.deleted_at is not None:
                raise HTTPException(status_code=404, detail="Genre is Inactive")
            
            return db_genre 
        
async def get_all_genre():
    with Session(db.engine) as session:
        statement = select(Genre).where(Genre.deleted_at == None)
        db_genre = session.exec(statement).all()
        return db_genre

        
async def update_genre(genre_id: int, updated_genre: Genre):
    with Session(db.engine) as session:
        statement = select(Genre).where(Genre.id == genre_id)
        db_genre = session.exec(statement).first()
        if db_genre is None:
            raise HTTPException(status_code = 404, detail="Genre not found")
        else:
            db_genre.title = updated_genre.title
            db_genre.description = updated_genre.description
            session.add(db_genre)
            session.commit()
            session.refresh(db_genre)
            return db_genre
            
# this is soft delete        
async def delete_genre(genre_id: int):
    with Session(db.engine) as session:
          statement = select(Genre).where(Genre.id == genre_id)
          db_genre = session.exec(statement).first()
          if db_genre is None:
               raise HTTPException(status_code=404, detail="Genre not found")
          else:
              db_genre.deleted_at = func.now()
              session.add(db_genre)
              session.commit()
              return {"message": "Genre Deleted"}
             