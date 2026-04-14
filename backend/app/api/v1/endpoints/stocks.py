from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.db import get_db
from app.models.market import Stock
from app.schemas.stock import StockResponse

router = APIRouter()

@router.get("/", response_model=List[StockResponse])
def get_stocks(db: Session = Depends(get_db)):
    """
    Lấy danh sách tất cả các mã chứng khoán có trong DB.
    """
    stocks = db.query(Stock).all()
    return stocks

@router.get("/{symbol}", response_model=StockResponse)
def get_stock_by_symbol(symbol: str, db: Session = Depends(get_db)):
    """
    Lấy chi tiết một mã chứng khoán theo Symbol (VNM, FPT...)
    """
    stock = db.query(Stock).filter(Stock.symbol == symbol.upper()).first()
    if not stock:
        raise HTTPException(status_code=404, detail="Không tìm thấy mã chứng khoán này")
    return stock