.PHONY: test
test:
	poetry run python -m pytest tests/


.PHONY: cleancode
cleancode:
	isort .
	black .
	mypy .