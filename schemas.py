# from typing import Union, List
from pydantic import BaseModel
from sqlalchemy import DateTime

class UserBase(BaseModel):
    name : str

    class Config:
        orm_mode = True

class UserDetail(BaseModel):
    id : str
    name : str
    is_completed : bool
    created_at : DateTime
    update_at : DateTime
    is_deleted : bool

    class Config:
        orm_mode = True
# class User(UserBase):
#     id = str
#     is_completed = bool
