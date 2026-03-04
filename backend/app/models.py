from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    hashed_password = Column(String)


# class User(Base):
#     __tablename__= "test"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, unique=True, index=True)