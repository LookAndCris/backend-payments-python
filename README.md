# backend-payments-python 

## Project Structure

backend-payments-python/
│
├── app/
│ ├── main.py
│ │
│ ├── api/
│ │ ├── routes.py
│ │ └── dependencies.py
│ │
│ ├── domain/
│ │ ├── models.py # Payment, Value Objects
│ │ ├── services.py # Business logic
│ │ └── exceptions.py
│ │
│ ├── application/
│ │ ├── use_cases.py # CreatePayment, GetPayment
│ │ └── dto.py
│ │
│ ├── infrastructure/
│ │ ├── db/
│ │ │ ├── models.py
│ │ │ ├── repository.py
│ │ │ └── session.py
│ │ │
│ │ ├── cache/
│ │ └── security/
│ │
│ └── config.py
│
├── tests/
│ ├── unit/
│ └── integration/
│
├── docker/
│ └── Dockerfile
│
├── docker-compose.yml
├── pyproject.toml
├── Makefile
└── README.md