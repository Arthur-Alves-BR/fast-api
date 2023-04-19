from sqlalchemy import Column, Integer, String, Date

from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    registration_date = Column(Date, nullable=False)
    email = Column(String, unique=True, index=True)
    birth_date = Column(Date, nullable=False)
    password = Column(String)
    name = Column(String)
