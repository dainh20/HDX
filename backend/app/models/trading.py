from sqlalchemy import Column, BigInteger, String, Numeric, ForeignKey
from app.core.db import Base
from app.models.base import AuditModel

class Order(Base, AuditModel):
    __tablename__ = "orders"
    __table_args__ = {"schema": "trading"}

    account_id = Column(BigInteger, index=True, nullable=False)
    stock_id = Column(BigInteger, index=True, nullable=False)
    side = Column(String(10), nullable=False) # BUY hoặc SELL
    order_type = Column(String(20), nullable=False) # LIMIT hoặc MARKET
    price = Column(Numeric(20, 2))
    quantity = Column(BigInteger, nullable=False)
    filled_quantity = Column(BigInteger, default=0)
    status = Column(String(20), default="OPEN")

class Trade(Base, AuditModel):
    __tablename__ = "trades"
    __table_args__ = {"schema": "trading"}

    buy_order_id = Column(BigInteger, nullable=False)
    sell_order_id = Column(BigInteger, nullable=False)
    stock_id = Column(BigInteger, index=True, nullable=False)
    price = Column(Numeric(20, 2), nullable=False)
    quantity = Column(BigInteger, nullable=False)