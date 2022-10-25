from typing import List
from pydantic import BaseModel, constr, EmailStr, validator
from starlette import status
from starlette.responses import Response
from sqlalchemy import Column, String, Integer, Boolean
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

from core.db import Base

class USER_ALCH (Base, SQLAlchemyBaseUserTable):
    name = Column(String, )

#from db.db_for_todo import Base

class USER(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    nick = Column(String(100), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    games_history = Column(String(1000), default='')

    def __repr__(self):
        return f'Игрок {self.nick}, id: {self.id}'



class User(BaseModel):
    id: int
    nick: constr(max_length=120)  # constr = ограниченная строка, существуют и другие con ... типы
    isbn: str
    #@validator(nick)
    #def validate_isbn(cls, nick):
    """
        Код валидации номер isbn (реализация опущена)
        Возвращает строку isbn после проверки
        Если валидация не прошла, кидает исключение ValueError
    """
    # return nick