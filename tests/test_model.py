"""Tests for model training and evaluation utilities."""

import pandas as pd
import pytest
from sklearn.datasets import make_classification

from churn_prediction.models.evaluate import evaluate_model, feature_importance_df
from churn_prediction.models.train import (
    train_logistic_regression,
    train_random_forest,
    train_xgboost,
)


@pytest.fixture
def classification_data():
    X, y = make_classification(
        n_samples=200,
        n_features=10,
        n_informative=5,
        random_state=42,
    )
    X = pd.DataFrame(X, columns=[f"f{i}" for i in range(10)])
    y = pd.Series(y)
    split = 160
    return X[:split], X[split:], y[:split], y[split:]


def test_train_logistic_regression(classification_data):
    X_train, X_test, y_train, y_test = classification_data
    model = train_logistic_regression(X_train, y_train)
    preds = model.predict(X_test)
    assert len(preds) == len(y_test)


def test_train_random_forest(classification_data):
    X_train, X_test, y_train, y_test = classification_data
    model = train_random_forest(X_train, y_train)
    preds = model.predict(X_test)
    assert len(preds) == len(y_test)


def test_train_xgboost(classification_data):
    X_train, X_test, y_train, y_test = classification_data
    model = train_xgboost(X_train, y_train)
    preds = model.predict(X_test)
    assert len(preds) == len(y_test)


def test_evaluate_model_returns_metrics(classification_data):
    X_train, X_test, y_train, y_test = classification_data
    model = train_random_forest(X_train, y_train)
    metrics = evaluate_model(model, X_test, y_test)
    for key in ("accuracy", "precision", "recall", "f1", "roc_auc"):
        assert key in metrics
        assert 0.0 <= metrics[key] <= 1.0


def test_feature_importance_df(classification_data):
    X_train, _, y_train, _ = classification_data
    model = train_random_forest(X_train, y_train)
    fi = feature_importance_df(model, list(X_train.columns))
    assert list(fi.columns) == ["feature", "importance"]
    assert len(fi) == X_train.shape[1]
    # Sorted descending
    assert fi["importance"].is_monotonic_decreasing
