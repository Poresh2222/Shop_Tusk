from typing import Optional

from pydantic import BaseModel, EmailStr, validator


class UserBase(BaseModel):
    id: int
    email: EmailStr
    name: str


class UserCreate(BaseModel):
    email: EmailStr
    name: str
    password: str    