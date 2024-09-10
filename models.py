from sqlalchemy import Column, Integer, String

from database import SQLBase


class User(SQLBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    tg = Column(String, unique=True)
    specialty = Column(String)
