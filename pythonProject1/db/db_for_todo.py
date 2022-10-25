from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric
import os

from core import config

DATABASE_NAME = 'boardgamearena.db'
DATABASE_PATH_ABS = os.path.join(os.path.join(config.GLOBAL_PATH, 'db'), DATABASE_NAME)

assert os.path.isfile(DATABASE_PATH_ABS), "DB does not exist"

st = f"sqlite:///{DATABASE_PATH_ABS}"
#st = f"sqlite:///{DATABASE_NAME}"
#st = r'sqlite:///C:\Users\Nontar\PycharmProjects\pythonProject1\boardgamearena.db'
print(st)
Engine = create_engine(st)

Session = sessionmaker(bind=Engine)
Base = declarative_base()


#engine.connect()


class GAMER(Base):
    __tablename__ = 'GAMER'
    id = Column(Integer, primary_key=True)
    nick = Column(String(100), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    games_history = Column(String(1000), default='')

    def __repr__(self):
        return f'Игрок {self.nick}, id: {self.id}'



# def create_db():
#     Base.metadata.create_all(Engine)


# create_db()
#
# ses = Session()
""" add two first gamers to the db
gamer1 = GAMER(nick='gamer-tester', password='12345')
gamer2 = GAMER(nick='gamer-notester', password='12345')
ses.add(gamer1)
ses.add(gamer2)
ses.commit()
"""
#ses.close()
ses = sessionmaker(bind=Engine)
session = ses()
session.close()


def db_get_all_gamers():
        sesi = ses()
        res = sesi.query(GAMER).all()
        #res = ses.execute("SELECT * FROM GAMER").fetchall()
        #ses.close()
        print('res', res)
        retu = '<==>'.join([e.nick for e in res])
        print(retu)
        return retu

print(db_get_all_gamers())