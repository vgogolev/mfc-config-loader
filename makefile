install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt && \
			pre-commit install --hook-type pre-push

format:
	black *.py

test:
	python -m pytest -v

lint:
	pylint src.configloader

pre-commit-check:
	@make lint

pre-push-check:
	@make test

