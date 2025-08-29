run:
	docker compose up --build

worker-high:
	docker compose run --rm worker celery -A myproject worker -l info -Q high_priority

worker-low:
	docker compose run --rm worker celery -A myproject worker -l info -Q low_priority

beat:
	docker compose run --rm worker celery -A myproject beat -l info
