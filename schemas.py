# from typing import Union, List
from pydantic import BaseModel
from datetime import datetime

class TodoBase(BaseModel):
    name : str

    class Config:
        orm_mode = True

class TodoDetail(BaseModel):
    id : str
    name : str
    is_completed : bool
    created_at : datetime
    is_deleted : datetime
    is_deleted : datetime

    class Config:
        orm_mode = True
# class User(UserBase):
#     id = str
#     is_completed = bool
