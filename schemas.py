# from typing import Union, List
from datetime import datetime

from pydantic import BaseModel


class TodoBase(BaseModel):
    name: str


class TodoDetail(BaseModel):
    id: str
    name: str

    class Config:
        orm_mode = True


# class User(UserBase):
#     id = str
#     is_completed = bool
