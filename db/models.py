from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

# orm model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)