from fastapi import APIRouter, HTTPException
from models.model_order import Order
from crud.crud_order import create_order, get_order,update_order,delete_order,get_all_order

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)


@router.get("/")
async def get_all():
      result = await get_all_order()
      return {
          'data': result,
          'message':'All Orders Fetched',
          'status' : True
      }

@router.get("/{order_id}")
async def get_one(order_id: int):
    result = await get_order(order_id)  
    return {
        'data': result,
        'message': 'Order fetched successfully',
        'status': True
    }

@router.post("/")
async def create(order: Order):
    result = await create_order(order)
    return {
        'data': result,
        'message': 'Order created successfully',
        'status': True
    }

@router.put("/{order_id}")
async def update(order_id: int, order: Order):
   result = await update_order(order_id, order)  
   return {
        'data': result,
        'message': 'Order fetched successfully',
        'status': True
    }

@router.patch("/{order_id}")
async def delete(order_id: int):
     result = await delete_order(order_id)  
     return {
        'data': result,
        'message': 'Order deleted successfully',
        'status': True
    }