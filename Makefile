setenv:
	cp example.env .env

build:
	docker compose build

up:
	docker compose up -d

test:
	docker compose exec api ./scripts/test.sh

enter:
	docker compose exec api bash

down:
	docker compose down
