from models.model_user import User, UserPassword, ResetPassword
from sqlmodel import Field, Session, SQLModel, create_engine, select
from auth.utils import get_password, verify_password
from config import db
from random import randint
from models.reset_token import Reset_Token

async def change_password(payload: UserPassword):
    with Session(db.engine) as session:
        statement = select(User).where(User.username == payload.username)
        db_user = session.exec(statement).first()
        
        if db_user is None:
            return "User not found"
        
        if not verify_password(payload.password, db_user.password):
            return "Old Password is incorrect" 
        
        hashed_password = get_password(payload.new_password)
        db_user.password = hashed_password
        session.add(db_user)
        session.commit()
        session.refresh(db_user)

    return 'Password Changed Successfully'
    return db_user


async def create_reset_token(username):
    with Session(db.engine) as session:
        statement = select(User).where(User.username == username)
        db_user = session.exec(statement).first()
        
        if db_user is None:
            return "User not found"
        
        otp = str(randint(1000,9999))

        token = Reset_Token(
            user_id=db_user.id,
            token = otp
        )

        session.add(token)
        session.commit()
    
    return 'OTP sent to your email'

async def create_new_password(payload: ResetPassword):
    with Session(db.engine) as session:
        statement = select(User).where(User.username == payload.username)
        db_user = session.exec(statement).first()
        
        if db_user is None:
            return "User not found"
        

        statement = select(Reset_Token).where(Reset_Token.user_id == db_user.id)
        db_token= session.exec(statement).first()

        if db_token is None:
            return 'Token Not found'
        
        if not db_token.token == payload.token:
            return 'Token is Incorrect'
        
        hashed_password = get_password(payload.password)
        db_user.password = hashed_password

        session.commit()

    return 'Password Changed Successfully'


        





        

