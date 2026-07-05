"""Data loading and preprocessing utilities."""

from pathlib import Path
from typing import Tuple

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler


def load_data(filepath: str) -> pd.DataFrame:
    """Load data from a CSV file.

    Args:
        filepath: Path to the CSV file.

    Returns:
        Loaded DataFrame.
    """
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {filepath}")
    return pd.read_csv(filepath)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean raw data by handling missing values and duplicates.

    Args:
        df: Raw DataFrame.

    Returns:
        Cleaned DataFrame.
    """
    df = df.drop_duplicates()
    for col in df.select_dtypes(include="number").columns:
        df[col] = df[col].fillna(df[col].median())
    for col in df.select_dtypes(include=["object", "string"]).columns:
        mode_vals = df[col].mode()
        df[col] = df[col].fillna(mode_vals[0] if not mode_vals.empty else "")
    return df.reset_index(drop=True)


def encode_categorical(
    df: pd.DataFrame, columns: list
) -> Tuple[pd.DataFrame, dict]:
    """Label-encode categorical columns.

    Args:
        df: DataFrame with categorical columns.
        columns: List of column names to encode.

    Returns:
        Tuple of (encoded DataFrame, mapping of column -> LabelEncoder).
    """
    encoders: dict = {}
    df = df.copy()
    for col in columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        encoders[col] = le
    return df, encoders


def split_data(
    df: pd.DataFrame,
    target: str,
    test_size: float = 0.2,
    random_state: int = 42,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Split data into train and test sets.

    Args:
        df: Full DataFrame.
        target: Name of the target column.
        test_size: Proportion of data to use for the test set.
        random_state: Random seed for reproducibility.

    Returns:
        Tuple of (X_train, X_test, y_train, y_test).
    """
    X = df.drop(columns=[target])
    y = df[target]
    return train_test_split(X, y, test_size=test_size, random_state=random_state)


def scale_features(
    X_train: pd.DataFrame, X_test: pd.DataFrame
) -> Tuple[pd.DataFrame, pd.DataFrame, StandardScaler]:
    """Standardise features using mean/std from training data.

    Args:
        X_train: Training feature matrix.
        X_test: Test feature matrix.

    Returns:
        Tuple of (scaled X_train, scaled X_test, fitted StandardScaler).
    """
    scaler = StandardScaler()
    X_train_scaled = pd.DataFrame(
        scaler.fit_transform(X_train), columns=X_train.columns
    )
    X_test_scaled = pd.DataFrame(
        scaler.transform(X_test), columns=X_test.columns
    )
    return X_train_scaled, X_test_scaled, scaler
