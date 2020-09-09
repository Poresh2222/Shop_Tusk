from models.database import database
from models.users import users_table
from app.shemas import users as user_schema



async def create_user(user: user_schema.UserCreate):
    query = users_table.insert().values(
        email=user.email, name=user.name, password=user.password
    )
    user_id = await database.execute(query)
    return {**user.dict(), 'id': user_id}


async def get_user(user_id: int):
    query = users_table.select().where(users_table.c.id == user_id)
    return await database.fetch_one(query)


async def get_user_by_email(email: str):
    query = users_table.select().where(users_table.c.email == email)
    return await database.fetch_one(query)    