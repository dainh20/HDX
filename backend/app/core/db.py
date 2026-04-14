from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# 1. Tạo Engine: Là "cầu nối" trung tâm giữa Python và Postgres
# Nó quản lý các kết nối (connection pool) tới cơ sở dữ liệu
engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    # Pool size giúp kiểm soát số lượng kết nối tối đa, tránh làm sập DB khi có nhiều người truy cập
    pool_size=10, 
    max_overflow=20
)

# 2. Tạo SessionLocal: Mỗi khi có một request (ví dụ user đặt lệnh), 
# chúng ta sẽ mở một "phiên làm việc" (session) riêng biệt.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. Tạo Base class: Tất cả các Model (User, Stock, Order) 
# sau này sẽ kế thừa từ class này để SQLAlchemy hiểu đó là một bảng trong DB.
Base = declarative_base()

# 4. Dependency: Hàm này dùng để cung cấp DB session cho các API của FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        # Quan trọng: Luôn đóng kết nối sau khi dùng xong để giải phóng tài nguyên
        db.close()