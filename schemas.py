# from typing import Union, List
from pydantic import BaseModel

class UserBase(BaseModel):
    name : str

    class Config:
        orm_mode = True


# class User(UserBase):
#     id = str
#     is_completed = bool
