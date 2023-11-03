from fastapi import APIRouter, HTTPException
from models.model_cart import Cart
from crud.crud_cart import create_cart, get_cart, update_cart, delete_cart

router = APIRouter(
    prefix="/carts",
    tags=["carts"]
)

@router.post("/")
async def store(cart: Cart):
    result = await create_cart(cart)
    return {
        'data': result,
        'message': 'Cart created successfully',
        'status': True
    }

@router.get("/{cart_id}")
async def get_one(cart_id: int):
    result = await get_cart(cart_id)
    return {
        'data': result,
        'message': 'Cart fetched successfully',
        'status': True
    }

@router.put("/{cart_id}")
async def update(cart_id: int, cart: Cart):
    result = await update_cart(cart_id, cart)
    return {
        'data': result,
        'message': 'Cart updated successfully',
        'status': True
    }

@router.patch("/{cart_id}")
async def delete(cart_id: int):
    result = await delete_cart(cart_id)
    return {
        'data': result,
        'message': 'Cart deleted successfully',
        'status': True
    }