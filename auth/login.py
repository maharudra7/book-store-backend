from models.model_user import User, UserBase
from sqlmodel import Field, Session, SQLModel, create_engine, select
from config import db
from auth.utils import verify_password
from fastapi import Response, status


def sign_in(user: UserBase, response: Response):
    with Session(db.engine) as session:
        statement = select(User).where(User.username == user.username)
        db_user = session.exec(statement).first()
        if db_user is None:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"email": "User not found"}

        if not verify_password(user.password, db_user.password):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"password": "Password is incorrect"}

    return True
