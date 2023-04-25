from sqlalchemy.orm import Session

from user import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session):
    return db.query(models.User).all()


def create_user(db: Session, user: schemas.UserIn):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# class UserCRUD:

#     def __init__(self, db: Session) -> None:
#         self._db = db

#     def get_user(self, user_id: int):
#         return self._db.query(models.User).filter(models.User.id == user_id).first()

#     def get_users(self):
#         return self._db.query(models.User).all()

#     def create_user(self, user: schemas.UserIn):
#         db_user = models.User(**user.dict())
#         self._db.add(db_user)
#         self._db.commit()
#         self._db.refresh(db_user)
#         return db_user
