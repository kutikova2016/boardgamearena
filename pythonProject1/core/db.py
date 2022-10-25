from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

import config

DATABASE_NAME = 'boardgamearena.db'
DATABASE_PATH_ABS = os.path.join(os.path.join(config.GLOBAL_PATH, 'db'), DATABASE_NAME)

assert os.path.isfile(DATABASE_PATH_ABS), "DB does not exist"

DB_URL_ABS = f"sqlite:///{DATABASE_PATH_ABS}"
engine = create_engine(DB_URL_ABS)

Session = sessionmaker(bind=engine)
Base = declarative_base()