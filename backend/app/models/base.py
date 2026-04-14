from sqlalchemy import Column, BigInteger, DateTime
from sqlalchemy.sql import func
from app.core.db import Base

class TimestampModel:
    """
    Mixin class để tự động thêm 2 cột created_at và updated_at
    vì bảng nào trong ERD của bạn cũng có 2 trường này.
    """
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

class AuditModel(TimestampModel):
    """
    Base class cho các model có ID là kiểu Long (BigInteger)
    """
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)