# Customer Churn Prediction System

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![CI](https://github.com/salehin717/customer-churn-prediction-system/actions/workflows/python-ci.yml/badge.svg)](https://github.com/salehin717/customer-churn-prediction-system/actions/workflows/python-ci.yml)

An end-to-end machine learning system that predicts customer churn using the Telco Customer Churn dataset. Built with Python, Scikit-learn, XGBoost, SHAP, and Streamlit.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Repository Structure](#repository-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Pipeline](#model-pipeline)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Project Overview

Customer churn — the loss of clients or subscribers — is a critical business problem. This project builds a production-quality machine learning system to identify customers at risk of churning, enabling proactive retention strategies.

> **Note:** This repository currently contains the project scaffold and development workflow. Machine learning implementation will be added in subsequent phases.

---

## Features

- **Automated Data Preprocessing** – Handles missing values, encoding, and scaling.
- **Feature Engineering** – Domain-driven feature construction for improved model accuracy.
- **Model Training & Evaluation** – Supports multiple classifiers with cross-validation and hyperparameter tuning.
- **Explainability** – SHAP-based model interpretation for business stakeholders.
- **Interactive Dashboard** – Streamlit application for real-time churn predictions.
- **CI/CD Pipeline** – GitHub Actions for automated testing and code quality checks.

---

## Repository Structure

```
customer-churn-prediction-system/
├── app/                    # Streamlit web application
│   ├── __init__.py
│   └── app.py
├── data/
│   ├── raw/                # Original, immutable data
│   ├── processed/          # Cleaned and transformed data
│   └── README.md
├── models/                 # Serialised trained models
├── notebooks/              # Exploratory data analysis notebooks
├── reports/
│   ├── figures/            # Generated plots and charts
│   └── README.md
├── src/                    # Core ML pipeline source code
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── train.py
│   ├── evaluate.py
│   ├── predict.py
│   └── utils.py
├── tests/                  # Unit and integration tests
├── .github/workflows/      # CI/CD pipeline definitions
├── requirements.txt
├── pyproject.toml
├── Makefile
├── CONTRIBUTING.md
└── README.md
```

---

## Installation

### Prerequisites

- Python 3.11+
- `pip` or a virtual environment manager (`venv`, `conda`)

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/salehin717/customer-churn-prediction-system.git
cd customer-churn-prediction-system

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate       # macOS / Linux
# .venv\Scripts\activate        # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

---

## Usage

> **TODO:** Add usage instructions once the application is implemented.

### Run the Streamlit app

```bash
streamlit run app/app.py
```

### Train the model

```bash
python -m src.train
```

### Run predictions

```bash
python -m src.predict --input data/processed/customers.csv
```

### Run tests

```bash
make test
```

### Code quality

```bash
make lint   # Run Flake8
make format # Run Black and isort
```

---

## Dataset

This project uses the [Telco Customer Churn dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) from Kaggle.

| Attribute | Details |
|-----------|---------|
| Rows | 7,043 customers |
| Columns | 21 features |
| Target | `Churn` (Yes / No) |
| Source | IBM Sample Dataset |

> **TODO:** Add dataset download instructions and preprocessing notes.

---

## Model Pipeline

```
Raw Data → Preprocessing → Feature Engineering → Model Training → Evaluation → Deployment
```

| Stage | Description | Status |
|-------|-------------|--------|
| Preprocessing | Handle nulls, encode categoricals, scale numerics | 🔲 Planned |
| Feature Engineering | Interaction terms, aggregations, domain features | 🔲 Planned |
| Model Training | Logistic Regression, Random Forest, XGBoost | 🔲 Planned |
| Evaluation | Accuracy, ROC-AUC, Precision, Recall, F1 | 🔲 Planned |
| Explainability | SHAP values, feature importance plots | 🔲 Planned |
| Deployment | Streamlit dashboard | 🔲 Planned |

---

## Future Improvements

- [ ] Hyperparameter tuning with Optuna or GridSearchCV
- [ ] MLflow experiment tracking
- [ ] Docker containerisation
- [ ] REST API with FastAPI
- [ ] Automated retraining pipeline
- [ ] Feature store integration
- [ ] A/B testing framework for model comparison

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
