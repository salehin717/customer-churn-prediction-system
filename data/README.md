# Data Directory

This directory stores all project datasets.

## Structure

```
data/
├── raw/          # Original, immutable source data – never modify these files
├── processed/    # Cleaned, transformed data ready for modelling
└── README.md     # This file
```

## Dataset

**Telco Customer Churn**
- Source: [Kaggle – Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- Rows: 7,043 customers
- Features: 21 columns (demographics, services, contract details)
- Target: `Churn` (Yes / No)

## Usage

1. Download the dataset from the Kaggle link above.
2. Place the raw CSV file in `data/raw/`.
3. Run the preprocessing pipeline to generate files in `data/processed/`:

```bash
python -m src.preprocessing
```

> **Note:** Raw data files are excluded from version control via `.gitignore`.
> Processed data may be excluded as well if files are large.
