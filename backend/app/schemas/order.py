from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal

class OrderBase(BaseModel):
    stock_id: int
    side: str
    order_type: str
    price: Optional[Decimal] = None
    quantity: int

class OrderCreate(OrderBase):
    account_id: int

class OrderResponse(OrderBase):
    id: int
    filled_quantity: int
    status: str
    
    class Config:
        from_attributes = True