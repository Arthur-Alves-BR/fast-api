import json

from user.models import UserIn


def get_fp(mode=str):
    return open('users.json', mode)


users = json.load(get_fp('r'))


def create_user(user: UserIn) -> UserIn:
    users.append(user.dict())
    json.dump(users, get_fp('w'))
    return user
