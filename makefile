install:
	@poetry install

run:
	@poetry run fizz_buzz

lint:
	@poetry run flake8 fizzbuzz

test:
	@poetry run pytest

test-coverage:
	@poetry run pytest --cov=fizzbuzz --cov-report xml

build:
	@poetry build

docker-build:
	@docker build . -t fizz_buzz

package-install:
	@python3 -m pip install --user dist/*.whl