import json

from models import User


def get_fp(mode=str):
    return open('users.json', mode)


users = json.load(get_fp('r'))


def create_user(user: User) -> User:
    users.append(user.dict())
    json.dump(users, get_fp('w'))
    return user
