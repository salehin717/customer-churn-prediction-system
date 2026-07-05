"""Model training utilities."""

from pathlib import Path
from typing import Any

import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier


def train_logistic_regression(X_train, y_train, **kwargs) -> LogisticRegression:
    """Train a Logistic Regression classifier.

    Args:
        X_train: Training feature matrix.
        y_train: Training labels.
        **kwargs: Additional keyword arguments forwarded to LogisticRegression.

    Returns:
        Fitted LogisticRegression model.
    """
    model = LogisticRegression(max_iter=1000, random_state=42, **kwargs)
    model.fit(X_train, y_train)
    return model


def train_random_forest(X_train, y_train, **kwargs) -> RandomForestClassifier:
    """Train a Random Forest classifier.

    Args:
        X_train: Training feature matrix.
        y_train: Training labels.
        **kwargs: Additional keyword arguments forwarded to RandomForestClassifier.

    Returns:
        Fitted RandomForestClassifier model.
    """
    model = RandomForestClassifier(n_estimators=100, random_state=42, **kwargs)
    model.fit(X_train, y_train)
    return model


def train_xgboost(X_train, y_train, **kwargs) -> XGBClassifier:
    """Train an XGBoost classifier.

    Args:
        X_train: Training feature matrix.
        y_train: Training labels.
        **kwargs: Additional keyword arguments forwarded to XGBClassifier.

    Returns:
        Fitted XGBClassifier model.
    """
    model = XGBClassifier(
        n_estimators=100,
        eval_metric="logloss",
        random_state=42,
        **kwargs,
    )
    model.fit(X_train, y_train)
    return model


def save_model(model: Any, filepath: str) -> None:
    """Persist a trained model to disk.

    Args:
        model: Trained model object.
        filepath: Destination path (e.g. ``models/xgb_model.joblib``).
    """
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, filepath)


def load_model(filepath: str) -> Any:
    """Load a persisted model from disk.

    Args:
        filepath: Path to the saved model file.

    Returns:
        Loaded model object.
    """
    return joblib.load(filepath)
