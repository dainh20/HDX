Source/
│
├── cmd/                        # Entry point (main app)
│   └── api/
│       └── main.go (hoặc main.py / Application.java)
│
├── internal/
│   ├── user/
│   │   ├── handler/
│   │   ├── service/
│   │   ├── repository/
│   │   ├── model/
│   │   └── router.go
│   │
│   ├── account/
│   │   ├── handler/
│   │   ├── service/
│   │   ├── repository/
│   │   ├── model/
│   │   └── router.go
│   │
│   ├── order/
│   ├── trade/
│   ├── stock/
│   ├── portfolio/
│   ├── transaction/
│   ├── deposit/
│   ├── freeze/
│   │
│   └── middleware/
│
├── pkg/                        # Shared utilities
│   ├── database/
│   ├── logger/
│   ├── auth/
│   ├── utils/
│   └── errors/
│
├── migrations/                 # SQL migration files
│   ├── 001_create_users.sql
│   ├── 002_create_accounts.sql
│   ├── ...
│
├── configs/
│   └── config.yaml
│
├── docker/
│   ├── Dockerfile
│   └── postgres/
│
├── tests/
│
├── docker-compose.yml
└── README.md



