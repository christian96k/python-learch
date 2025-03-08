from sqlalchemy import Column, Integer, String, Boolean
from database.database import Base

class ItemSchema(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    value = Column(String, index=True)
    active = Column(Boolean, nullable=True)
