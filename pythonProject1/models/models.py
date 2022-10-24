from typing import List
from pydantic import BaseModel, constr, EmailStr, validator
from starlette import status
from starlette.responses import Response
from sqlalchemy import Column, String, Integer, Boolean

#from db.db_for_todo import Base

class GAMER(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    is_complete = Column(Boolean, default=False)



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