from fastapi import APIRouter, HTTPException

from app.shemas import users
from app.crud import users as users_crud

router = APIRouter()


@router.get('/')
async def check():
    return {"Hello": "Worldd"}


@router.post('/sing-up')
async def create_user(user: users.UserCreate):
    db_user = await users_crud.get_user_by_email(email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail='Email alredy registed')
    return await users_crud.create_user(user=user)   