from fastapi import APIRouter, HTTPException
from models.model_genre import Genre
from crud.crud_genre import create_genre, get_genre,update_genre,delete_genre,get_all_genre
router = APIRouter(
    prefix="/genres",
    tags=["genres"]
)

@router.get("/")
async def get_all():
    result = await get_all_genre()
    return {
        'data': result,
        'message': 'All Genre fetched successfully',
        'status': True
    }

@router.get("/{genre_id}")
async def get_one(genre_id: int):
    result = await get_genre(genre_id)  
    return {
        'data': result,
        'message': 'Genre fetched successfully',
        'status': True
    }

@router.post("/")
async def create(genre:Genre):
    result = await create_genre(genre)
    return {
        'data': result,
        'message': 'Genre created successfully',
        'status': True
    }

@router.put("/{genre_id}")
async def update(genre_id: int, genre: Genre):
   result = await update_genre(genre_id, genre)  
   return {
        'data': result,
        'message': 'Genre fetched successfully',
        'status': True
    }

@router.patch("/{genre_id}")
async def delete(genre_id: int):
     result = await delete_genre(genre_id)  
     return {
        'data': result,
        'message': 'Genre fetched successfully',
        'status': True
    }