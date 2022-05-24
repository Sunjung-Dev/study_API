from sqlalchemy import Column, TEXT, INT, BIGINT
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Test(Base):
    __tablename__ = 'my_info'
    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    passwd = Column(TEXT, nullable=False)

