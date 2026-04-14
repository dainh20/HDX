from sqlalchemy import Column, String, Numeric, BigInteger
from app.core.db import Base
from app.models.base import AuditModel

class Stock(Base, AuditModel):
    __tablename__ = "stocks"
    __table_args__ = {"schema": "market"}

    symbol = Column(String(20), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=False)
    exchange = Column(String(20), nullable=False)
    status = Column(String(20), default="active")

class StockPrice(Base, AuditModel):
    __tablename__ = "stock_prices"
    __table_args__ = {"schema": "market"}

    stock_id = Column(BigInteger, index=True, nullable=False)
    price = Column(Numeric(20, 2), nullable=False)
    # Lưu ý: Theo ERD mới, bảng này chỉ có created_at, không có updated_at 
    # (vì giá là dữ liệu lịch sử, không update bản ghi cũ).