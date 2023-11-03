from fastapi import APIRouter, HTTPException
from models.model_order_item import OrderItem
from crud.crud_order_item import create_order_item, get_order_item ,update_order_item,delete_order_item,get_all_order_item

router = APIRouter(
    prefix="/order_items",
    tags=["order_items"]
)

@router.get("/")
async def get_all():
      result = await get_all_order_item()
      return {
          'data': result,
          'message':'All OrderItem Fetched',
          'status' : True
      }

@router.get("/{order_item_id}")
async def get_one(order_item_id: int):
    result = await get_order_item(order_item_id)  
    return {
        'data': result,
        'message': 'OrderItem fetched successfully',
        'status': True
    }

@router.post("/")
async def create(order: OrderItem):
    result = await create_order_item(order)
    return {
        'data': result,
        'message': 'OrderItem created successfully',
        'status': True
    }

@router.put("/{order_item_id}")
async def update(order_item_id: int, order_item: OrderItem):
   result = await update_order_item(order_item_id, order)  
   return {
        'data': result,
        'message': 'OrderItem fetched successfully',
        'status': True
    }

@router.patch("/{order_item_id}")
async def delete(order_item_id: int):
     result = await delete_order_item(order_item_id)  
     return {
        'data': result,
        'message': 'OrderItem deleted successfully',
        'status': True
    }