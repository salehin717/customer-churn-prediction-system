# Contributing to Customer Churn Prediction System

Thank you for your interest in contributing! This document outlines the workflow and standards for contributing to this project.

---

## Table of Contents

- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Code Style](#code-style)
- [Running Tests](#running-tests)
- [Pull Request Guidelines](#pull-request-guidelines)

---

## Getting Started

1. **Fork** the repository on GitHub.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/<your-username>/customer-churn-prediction-system.git
   cd customer-churn-prediction-system
   ```
3. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   pip install -r requirements.txt
   ```

---

## Development Workflow

1. Create a feature branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes, following the [Code Style](#code-style) guidelines.
3. Run the test suite and linters before committing:
   ```bash
   make lint
   make test
   ```
4. Commit using a clear, descriptive message:
   ```bash
   git commit -m "feat: add preprocessing pipeline for numeric features"
   ```
5. Push your branch and open a Pull Request against `main`.

---

## Code Style

This project enforces consistent code style using the following tools:

| Tool | Purpose | Config |
|------|---------|--------|
| [Black](https://black.readthedocs.io/) | Code formatting | `pyproject.toml` |
| [isort](https://pycqa.github.io/isort/) | Import sorting | `pyproject.toml` |
| [Flake8](https://flake8.pycqa.org/) | Linting | `.flake8` |

Run all checks at once:

```bash
make format   # Auto-format with Black and isort
make lint     # Run Flake8
```

Additional style guidelines:
- Use **type hints** for all function signatures.
- Write **docstrings** (Google style) for all public modules, classes, and functions.
- Use **`pathlib.Path`** instead of `os.path` for file system operations.
- Configure **logging** instead of using `print` statements.
- Use **dataclasses** where appropriate for structured data.

---

## Running Tests

```bash
make test
# or
pytest tests/ -v
```

All new features must be accompanied by appropriate tests.

---

## Pull Request Guidelines

- Keep PRs focused and small — one logical change per PR.
- Ensure all CI checks pass before requesting a review.
- Provide a clear description of *what* changed and *why*.
- Reference any related issues using `Closes #<issue-number>`.

---

## Questions?

Open an issue on GitHub or start a Discussion. We welcome all contributions!
