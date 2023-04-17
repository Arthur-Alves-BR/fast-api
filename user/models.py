from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    age: int
    email: str


class UserIn(UserBase):
    password: str
