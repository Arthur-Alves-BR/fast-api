from fastapi import APIRouter, status, HTTPException

from db import users, create_user
from user.models import UserBase, UserIn

user_router = APIRouter(prefix='/users')


@user_router.post('/')
def post_users(user: UserIn) -> UserBase:
    user = create_user(user)
    return user


@user_router.get('/')
def list_users() -> list[UserBase]:
    return users


@user_router.get('/{item_id}')
def retrieve_user(item_id: int) -> UserBase:
    try:
        return users[item_id - 1]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
