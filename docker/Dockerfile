FROM python:3.12-slim as builder

WORKDIR /app

RUN apt-get update && apt-get install -y gcc

RUN pip install poetry

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false \
  && poetry install --no-root --no-interaction --no-ansi


FROM python:3.12-slim

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.12 /usr/local/lib/python3.12
COPY --from=builder /usr/local/bin /usr/local/bin

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]