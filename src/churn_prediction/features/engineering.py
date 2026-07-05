"""Feature engineering utilities."""

import pandas as pd


def create_interaction_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create basic interaction features where applicable.

    Looks for common churn-related column pairs and adds ratio features.

    Args:
        df: Feature DataFrame.

    Returns:
        DataFrame with additional interaction columns.
    """
    df = df.copy()
    if {"tenure", "MonthlyCharges"}.issubset(df.columns):
        df["charges_per_tenure"] = df["MonthlyCharges"] / (df["tenure"] + 1)
    if {"TotalCharges", "tenure"}.issubset(df.columns):
        df["avg_monthly_charges"] = df["TotalCharges"] / (df["tenure"] + 1)
    return df


def select_features(
    df: pd.DataFrame, drop_columns: list
) -> pd.DataFrame:
    """Drop irrelevant columns from the DataFrame.

    Args:
        df: Input DataFrame.
        drop_columns: List of column names to remove.

    Returns:
        DataFrame with specified columns removed.
    """
    existing = [c for c in drop_columns if c in df.columns]
    return df.drop(columns=existing)
