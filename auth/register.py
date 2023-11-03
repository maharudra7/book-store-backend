from crud.crud_user import create_user
from models.model_user import UserBase

async def sign_up(user: UserBase):
    result = dict()
    result['data'] = await create_user(user)
    result['msg'] = "you have registered successfully"
    result['status'] = True
    return result
