from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database.database import Base  # Assicurati che Base sia importato correttamente

class UserSchema(Base):
    __tablename__ = "users"  # Definisce il nome della tabella come 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    role = Column(String, default="user")
    hashed_password = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
