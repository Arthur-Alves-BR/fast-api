from fastapi import APIRouter, status, HTTPException, Request

from database import engine

from user import models, schemas, crud


models.Base.metadata.create_all(bind=engine)

user_router = APIRouter(prefix='/users')


@user_router.post('/')
def post_users(request: Request, user: schemas.UserIn) -> schemas.UserOut:
    return crud.create_user(request.state.db, user)


@user_router.get('/')
def list_users(request: Request) -> list[schemas.UserOut]:
    return crud.get_users(request.state.db)


@user_router.get('/{user_id}')
def retrieve_user(request: Request, user_id: int) -> schemas.UserOut:
    user = crud.get_user(request.state.db, user_id)
    if user:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
