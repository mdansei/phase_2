up:
	docker compose up --build
down:
	docker compose down

sub:
	docker compose exec app poetry run python investor_bulletin/event_subscriber/main.py

pub:
	docker compose exec app poetry run python investor_bulletin/core/messaging.py
