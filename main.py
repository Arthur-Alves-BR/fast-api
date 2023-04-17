# from typing import Optional
from fastapi import FastAPI

from models import User
from db import users, create_user

app = FastAPI()


@app.post('/users/')
def post_users(user: User) -> User:
    user = create_user(user)
    return user


@app.get('/users/')
def list_users() -> list:
    return users


@app.get('/users/{item_id}')
def retrieve_user(item_id: int) -> dict:
    return users[item_id - 1]
