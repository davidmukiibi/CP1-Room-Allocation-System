from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker

Base = declarative_base()

class Room(Base):
    """creating the rooms table or in other terms,creating the Room model"""
    __tablename__ = 'Rooms'

    id = Column(Integer, primary_key=True, autoincrement=True)
    r_name = Column(String(32), nullable=False)
    r_type = Column(String(32), nullable=False)
    capacity = Column(Integer, nullable=False)

class Person(Base):
    """creating the people table or in other terms,creating the Person model"""
    __tablename__ = 'People'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(32), nullable=False)
    second_name = Column(String(32), nullable=False)
    person_type = Column(String(32), nullable=False)
    office_space = Column(String(32), nullable=True)
    living_space = Column(String(32), nullable=True)
    lspace_option = Column(String(32), nullable=True)

class DatabaseCreator(object):
    """creating a connection to the database and creating all the tables
    specified above"""
    def __init__(self, database_name=None):
        self.database_name = database_name
        if self.database_name:
            self.database_name = database_name + '.db'
        else:
            self.database_name = 'amity.db'
        self.engine = create_engine('sqlite:///' + self.database_name)
        self.session = sessionmaker()
        self.session.configure(bind=self.engine)
        Base.metadata.create_all(self.engine)