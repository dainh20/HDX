from sqlalchemy import Column, String
from app.core.db import Base
from app.models.base import AuditModel

class User(Base, AuditModel):
    __tablename__ = "users"
    __table_args__ = {"schema": "core"} # Khai báo thuộc schema 'core'

    username = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    status = Column(String(50), default="active")