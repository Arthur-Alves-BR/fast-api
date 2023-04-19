from sqlalchemy.orm import Session
from fastapi import APIRouter, status, HTTPException, Depends

from database import SessionLocal, engine

from user import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

user_router = APIRouter(prefix='/users')


def get_db():
    # Dependency
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@user_router.post('/')
def post_users(user: schemas.UserIn, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@user_router.get('/')
def list_users(db: Session = Depends(get_db)) -> list[schemas.UserBase]:
    return crud.get_users(db)


@user_router.get('/{user_id}')
def retrieve_user(user_id: int, db: Session = Depends(get_db)) -> schemas.UserBase:
    user = crud.get_user(db, user_id)
    if user:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
