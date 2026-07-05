"""Tests for data preprocessing utilities."""

import pandas as pd
import pytest

from churn_prediction.data.preprocessing import (
    clean_data,
    encode_categorical,
    scale_features,
    split_data,
)


@pytest.fixture
def sample_df():
    return pd.DataFrame(
        {
            "tenure": [1, 2, 3, 4, 5],
            "MonthlyCharges": [50.0, 60.0, 70.0, None, 90.0],
            "Contract": ["Month-to-month", "One year", "Two year", "One year", None],
            "Churn": [1, 0, 0, 1, 0],
        }
    )


def test_clean_data_removes_nulls(sample_df):
    cleaned = clean_data(sample_df)
    assert cleaned.isnull().sum().sum() == 0


def test_clean_data_no_duplicates():
    df = pd.DataFrame({"a": [1, 1, 2], "b": [3, 3, 4]})
    cleaned = clean_data(df)
    assert len(cleaned) == 2


def test_encode_categorical(sample_df):
    cleaned = clean_data(sample_df)
    encoded, encoders = encode_categorical(cleaned, ["Contract"])
    assert encoded["Contract"].dtype != object
    assert "Contract" in encoders


def test_split_data(sample_df):
    cleaned = clean_data(sample_df)
    X_train, X_test, y_train, y_test = split_data(
        cleaned, target="Churn", test_size=0.4
    )
    assert len(X_train) + len(X_test) == len(cleaned)
    assert "Churn" not in X_train.columns


def test_scale_features(sample_df):
    cleaned = clean_data(sample_df)
    X_train, X_test, _, _ = split_data(
        cleaned[["tenure", "MonthlyCharges", "Churn"]],
        target="Churn",
        test_size=0.4,
    )
    X_train_s, X_test_s, scaler = scale_features(X_train, X_test)
    assert X_train_s.shape == X_train.shape
    assert X_test_s.shape == X_test.shape
