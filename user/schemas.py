from datetime import date
from pydantic import BaseModel


class UserBase(BaseModel):
    registration_date: date
    birth_date: date
    email: str
    name: str

    class Config:
        orm_mode = True


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    id: int
