dev:
	uvicorn app.main:app --reload

test:
	pytest

docker-build:
	docker compose build

docker-up:
	docker compose up

docker-test:
	docker compose run payments-api pytest

lint:
	ruff check .

format:
	ruff format .