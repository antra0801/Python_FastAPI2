from .database import Base
from sqlalchemy import Column , String , Integer

class Blog(Base):
    __tablename__ = 'blogA'
    id = Column(Integer , primary_key=True , index=True)
    title = Column(String)
    body = Column(String)


class User(Base):
    __tablename__ = 'UserTable'

    id = Column(Integer, primary_key=True , index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
