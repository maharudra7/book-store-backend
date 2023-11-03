from fastapi import APIRouter, HTTPException
from models.model_user import User
from crud.crud_user import create_user, get_user,update_user, delete_user,get_all_user
from sqlmodel import Session, select

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get("/")
async def get_all():
      result = await get_all_user()
      return {
          'data': result,
          'message':'All Users Fetched',
          'status' : True
      }

@router.get("/{user_id}")
async def get_one(user_id: int):
    result = await get_user(user_id)  
    return {
        'data': result,
        'message': 'User fetched successfully',
        'status': True
    }

@router.post("/")
async def create(user: User):
    result = await create_user(user)
    return {
        'data': result,
        'message': 'User created successfully',
        'status': True
    }


@router.put("/{user_id}")
async def update(user_id: int, user: User):
   result = await update_user(user_id, user)  
   return {
        'data': result,
        'message': 'User Updated successfully',
        'status': True
    }

@router.patch("/{user_id}")
async def delete(user_id: int):
     result = await delete_user(user_id)  
     return {
        'data': result,
        'message': 'User deleted successfully',
        'status': True
    }