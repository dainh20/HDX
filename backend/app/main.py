from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.core.config import settings
from app.api.deps import get_db

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Cấu hình CORS - Giúp Frontend (React/Vue) có thể gọi API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Trong SE thực tế, bạn sẽ chỉ định rõ domain của frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint kiểm tra sức khỏe hệ thống (Health Check)
@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "project": settings.PROJECT_NAME}

# Endpoint test kết nối DB Master thực tế
@app.get("/test-db", tags=["Debug"])
def test_db_connection(db: Session = Depends(get_db)):
    try:
        # Thực hiện một câu query đơn giản nhất
        db.execute(text("SELECT 1"))
        return {"message": "✅ Kết nối Database Master thành công!"}
    except Exception as e:
        return {"message": f"❌ Lỗi kết nối: {str(e)}"}

# Sau này bạn sẽ include các router vào đây
# app.include_router(stocks.router, prefix=f"{settings.API_V1_STR}/stocks", tags=["stocks"])