import sqlalchemy
from sqlalchemy.orm import relationship
print(sqlalchemy.__version__)

from sqlalchemy import Column, Integer, String, ForeignKey

class Base:
    pass

class Student(Base):
    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    patronynic = Column(String)
    age = Column(Integer)
    address =Column(String)
    group = Column(Integer, ForeignKey('groups.id'))

    def __int__(self, full_name:list[str], age: int, address: str, id_group: int):
        self.surname = full_name[0]
        self.name = full_name[1]
        self.patronynic = full_name[2]
        self.age = age
        self.address = address
        self.group = id_group

    def __repr__(self):
        info: str = f'Студент (ФИО: {self.surname} {self.name} {self.patronynic}, '\
        f'Возраст: {self.age}, Адрес: {self.address}, ID группы: {self.group}'
        return info

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    group_name = Column(String)
    student = sqlalchemy.orm.relationship('Student')

    def __repr__(self):
        return f'Группа [ID: {self.id}, Название: {self.group_name}]'

DATABASE_NAME = 'ivaners_test2.db'

engine = sqlalchemy.create_engine(f"sqlite:///{DATABASE_NAME}")
Session = sqlalchemy.orm.sessionmaker(bind=engine)

#Base = sqlalchemy.ext.declarative.declarative_base()

engine.connect()

def create_db():
    Base.metafata.create_all(engine)
