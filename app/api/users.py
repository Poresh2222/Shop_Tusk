from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.shemas import users
from app.crud import users as users_crud
from app.crud.dependencies import get_current_user

router = APIRouter()


@router.get('/')
async def check():
    return {"Hello": "Worlddd"}


@router.post('/sing-up', response_model=users.User)
async def create_user(user: users.UserCreate):
    db_user = await users_crud.get_user_by_email(email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail='Email alredy registed')
    return await users_crud.create_user(user=user)


@router.post('/auth', response_model=users.TokenBase)
async def auth(from_data: OAuth2PasswordRequestForm = Depends()):
    user = await users_crud.get_user_by_email(email=from_data.username)

    if not user:
        raise HTTPException(status_code=400, detail='Incorrect email or password')

    if not users_crud.validate_password(
        password=form_data.password, hashed_password=user['hashed_password']
    ):
        raise HTTPException(status_code=400, detail='Incorrect email or password')

    return await users_crud.create_user_token(user_id=user['id'])


@router.get('/users/me', response_model=users.UserBase)
async def read_users_me(current_user: users.User = Depends(get_current_user)):
    return current_user           