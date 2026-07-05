.PHONY: help install format lint test clean

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

install:  ## Install dependencies
	pip install -r requirements.txt

format:  ## Auto-format code with Black and isort
	black src/ app/ tests/
	isort src/ app/ tests/

lint:  ## Run Flake8 linter
	flake8 src/ app/ tests/

test:  ## Run the test suite with pytest
	pytest tests/ -v

clean:  ## Remove Python cache files
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	rm -rf .pytest_cache .coverage htmlcov/
