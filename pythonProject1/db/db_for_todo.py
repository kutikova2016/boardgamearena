import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric


BASE_DIR = os.path.dirname(os.path.abspath(__name__))
DB_path = os.path.join(BASE_DIR, 'todo', 'database', 'DB')
print(BASE_DIR)
print(__name__)
print(os.path.abspath(__name__))
print(os.getcwd())

Base = declarative_base()
engine = create_engine()


class GAMER(Base):
    __tablename__ = 'GAMER'
    id = Column(Integer, primary_key=True)
    nick = Column(String(100), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    games_history = Column(String(1000))