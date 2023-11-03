from fastapi import APIRouter, HTTPException
from models.model_author import Author
from crud.crud_author import create_author, get_author,update_author,delete_author, get_all_author

router = APIRouter(
    prefix="/authors",
    tags=["authors"]
)

@router.get("/")
async def get_all():
    result = await get_all_author()
    return {
        'data': result,
        'message': 'All Author fetched successfully',
        'status': True
    }

@router.get("/{author_id}")
async def get_one(author_id: int):
    result = await get_author(author_id)  
    return {
        'data': result,
        'message': 'Author fetched successfully',
        'status': True
    }

@router.post("/")
async def create(payload:Author):
    # if len(payload.name) == 0:
    #     return {
    #         'data':None,
    #         'message':'Name is required',
    #         'status':False
    #     }
    # if len(payload.description) > 250:
    #     return {
    #         'data':None,
    #         'message':'Description length exceeds',
    #         'status':False
    #     }
    result = await create_author(payload)
    return {
        'data': result,
        'message': 'Author created successfully',
        'status': True
    }

@router.put("/{author_id}")
async def update(author_id: int, author: Author):
   result = await update_author(author_id, author)  
   return {
        'data': result,
        'message': 'Author fetched successfully',
        'status': True
    }

@router.patch("/{author_id}")
async def delete(author_id: int):
     result = await delete_author(author_id)  
     return {
        'data': result,
        'message': 'Author deleted successfully',
        'status': True
    }