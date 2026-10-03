up:
	cp -n .env.example .env || true
	docker compose up --build
down:
	docker compose down
test:
	pytest
