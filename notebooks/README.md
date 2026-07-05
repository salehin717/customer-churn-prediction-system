# Notebooks

This directory contains Jupyter notebooks for exploratory data analysis (EDA)
and ad-hoc experimentation.

## Naming Convention

Use a numbered prefix so notebooks run in a logical order:

```
01_eda_raw_data.ipynb
02_feature_exploration.ipynb
03_model_experiments.ipynb
```

## Guidelines

- Notebooks are for **exploration only** – production-ready code lives in `src/`.
- Clear all outputs before committing to keep diffs clean.
- Use `# %%` cell markers when converting to `.py` scripts for version control.

> **TODO:** Add EDA notebooks once the dataset is available.
