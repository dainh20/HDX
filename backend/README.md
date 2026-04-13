backend/
├── app/
│   ├── main.py                 # Entry point (Tương đương AssetManagementApplication.java)
│   │
│   ├── api/                    # Tương đương Controller layer
│   │   ├── v1/                 # Versioning cho API
│   │   │   ├── stocks.py
│   │   │   ├── orders.py
│   │   │   └── accounts.py
│   │   └── deps.py             # Dependency Injection (DB session, Auth)
│   │
│   ├── core/                   # Tương đương config/ & constant/
│   │   ├── config.py           # Pydantic Settings (Đọc .env)
│   │   ├── constants.py        # Hằng số hệ thống
│   │   └── security.py         # JWT, Password hashing
│   │
│   ├── models/                 # Tương đương entity/ (SQLAlchemy Models)
│   │   ├── base.py             # Base class cho toàn bộ model
│   │   ├── market.py           # Stocks, StockPrices
│   │   ├── trading.py          # Orders, Trades
│   │   └── account.py          # Accounts, Transactions, AssetFreezes
│   │
│   ├── repositories/           # Tương đương dao/ & repository/ (Data Access)
│   │   ├── base_repo.py        # Generic CRUD logic
│   │   ├── stock_repo.py
│   │   └── order_repo.py
│   │
│   ├── schemas/                # Tương đương dto/ (Pydantic Models)
│   │   ├── request/            # Request DTOs (Dữ liệu client gửi lên)
│   │   ├── response/           # Response DTOs (Dữ liệu trả về client)
│   │   └── enums.py            # Tương đương enumtype/
│   │
│   ├── services/               # Tương đương logic/ (Business Logic Layer)
│   │   ├── trading_service.py  # Logic khớp lệnh, check số dư
│   │   ├── market_service.py   # Xử lý giá thị trường
│   │   └── kafka_service.py    # Logic bắn/nhận message Kafka
│   │
│   ├── workers/                # Tương đương scheduler/ & Kafka Workers
│   │   ├── celery_app.py       # Cho các task chạy ngầm định kỳ
│   │   ├── kafka_consumer.py   # Lắng nghe các event giao dịch
│   │   └── tasks.py            # Định nghĩa các hàm chạy nền
│   │
│   ├── exceptions/             # Tương đương exception/ (Custom Errors)
│   │   └── base.py             # App-wide exception handlers
│   │
│   └── util/                   # Tương đương util/ (Helpers)
│       ├── format_utils.py
│       └── kafka_utils.py
│
├── alembic/                    # Tương đương db/migration/ (Database versioning)
├── tests/                      # Unit/Integration tests
├── .env                        # Biến môi trường
├── requirements.txt            # Tương đương pom.xml
└── Dockerfile