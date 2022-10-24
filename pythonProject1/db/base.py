from databases import Database
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'potgresql://postgres:123456@localhost/microblog'

from core.config import DATABASE_URL

databases = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(DATABASE_URL)