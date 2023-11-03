from fastapi import FastAPI, Response
from  routers import router_users, router_author,router_genres, router_items, router_orders, router_order_items

from models.model_user import User, UserBase, UserPassword, ResetPassword
from models.model_order import Order
from models.model_order_item import OrderItem
from models.model_item import Item
from models.model_author import Author
from models.model_genre import Genre
from models.model_coupon import Coupon
from sqlmodel import Field, Session, SQLModel, create_engine, select
from auth.login import sign_in
from auth.register import sign_up
from config import db
from auth.password import change_password, create_new_password, create_reset_token
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_users.router)
app.include_router(router_author.router)
app.include_router(router_genres.router)
app.include_router(router_items.router)
app.include_router(router_orders.router)
app.include_router(router_order_items.router)

db.create_db_and_table()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/login")
def login_user(user: UserBase, response: Response):
    result = sign_in(user, response=response)
    return result

@app.post("/register")
async def register_user(user: UserBase):
    result = await sign_up(user)
    return result

@app.put("/change password")
async def update_password(user: UserPassword):
    result = await change_password(user)
    return result

@app.post("/forgot password")
async def forgot_password(username: str):
    result = await create_reset_token(username)
    return result

@app.post("/reset password")
async def reset_password(token: ResetPassword):
    result = await create_new_password(token)
    return result
