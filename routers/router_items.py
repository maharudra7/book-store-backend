from fastapi import APIRouter, HTTPException
from models.model_item import Item
from crud.crud_item import create_item, get_item,update_item,delete_item,get_all_item
router = APIRouter(
    prefix="/items",
    tags=["items"]
)

@router.get("/")
async def get_all():
    result = await get_all_item()
    return {
        'data': result,
        'message': 'All Items fetched successfully',
        'status': True
    }

@router.get("/{item_id}")
async def get_one(item_id: int):
    result = await get_item(item_id)  
    return {
        'data': result,
        'message': 'item fetched successfully',
        'status': True
    }

@router.post("/")
async def create(item: Item):
    result = await create_item(item)
    return {
        'data': result,
        'message': 'Item created successfully',
        'status': True
    }

@router.put("/{item_id}")
async def update(item_id: int, item: Item):
   result = await update_item(item_id, item)  
   return {
        'data': result,
        'message': 'Item fetched successfully',
        'status': True
    }

@router.patch("/{item_id}")
async def delete(item_id: int):
     result = await delete_item(item_id)  
     return {
        'data': result,
        'message': 'Item fetched successfully',
        'status': True
    }