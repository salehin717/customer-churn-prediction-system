.PHONY: install format lint test clean

install:
	pip install -r requirements.txt

format:
	black src tests dashboard
	isort src tests dashboard

lint:
	flake8 src tests dashboard

test:
	pytest tests/

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .coverage htmlcov
