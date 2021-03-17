from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class MyModel(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))