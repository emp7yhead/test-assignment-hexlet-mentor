install:
	@poetry install

run:
	@poetry run fizzbuzz

lint:
	@poetry run flake8 fizzbuzz

test:
	@poetry run pytest

test-coverage:
	@poetry run pytest --cov=fizzbuzz --cov-report xml