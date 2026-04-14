from pydantic import BaseModel

class StockBase(BaseModel):
    symbol: str
    name: str
    exchange: str

class StockResponse(StockBase):
    id: int
    status: str

    class Config:
        from_attributes = True