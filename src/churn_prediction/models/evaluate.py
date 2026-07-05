"""Model evaluation utilities."""

from typing import Any, Dict

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    RocCurveDisplay,
    accuracy_score,
    classification_report,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)


def evaluate_model(model: Any, X_test, y_test) -> Dict[str, float]:
    """Compute standard classification metrics for a fitted model.

    Args:
        model: Trained classifier with a ``predict`` / ``predict_proba`` method.
        X_test: Test feature matrix.
        y_test: True test labels.

    Returns:
        Dictionary containing accuracy, precision, recall, F1, and ROC-AUC.
    """
    y_pred = model.predict(X_test)
    y_prob = (
        model.predict_proba(X_test)[:, 1]
        if hasattr(model, "predict_proba")
        else None
    )
    metrics: Dict[str, float] = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred, zero_division=0),
        "recall": recall_score(y_test, y_pred, zero_division=0),
        "f1": f1_score(y_test, y_pred, zero_division=0),
    }
    if y_prob is not None:
        metrics["roc_auc"] = roc_auc_score(y_test, y_prob)
    return metrics


def print_classification_report(model: Any, X_test, y_test) -> None:
    """Print a full sklearn classification report.

    Args:
        model: Trained classifier.
        X_test: Test feature matrix.
        y_test: True test labels.
    """
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))


def plot_confusion_matrix(
    model: Any, X_test, y_test, ax: plt.Axes = None
) -> plt.Figure:
    """Plot a confusion matrix for the model predictions.

    Args:
        model: Trained classifier.
        X_test: Test feature matrix.
        y_test: True test labels.
        ax: Optional matplotlib axes to plot on.

    Returns:
        Matplotlib Figure object.
    """
    if ax is None:
        fig, ax = plt.subplots()
    else:
        fig = ax.get_figure()
    ConfusionMatrixDisplay.from_estimator(model, X_test, y_test, ax=ax)
    ax.set_title("Confusion Matrix")
    return fig


def plot_roc_curve(model: Any, X_test, y_test, ax: plt.Axes = None) -> plt.Figure:
    """Plot the ROC curve for the model.

    Args:
        model: Trained classifier with ``predict_proba``.
        X_test: Test feature matrix.
        y_test: True test labels.
        ax: Optional matplotlib axes to plot on.

    Returns:
        Matplotlib Figure object.
    """
    if ax is None:
        fig, ax = plt.subplots()
    else:
        fig = ax.get_figure()
    RocCurveDisplay.from_estimator(model, X_test, y_test, ax=ax)
    ax.set_title("ROC Curve")
    return fig


def feature_importance_df(model: Any, feature_names: list) -> pd.DataFrame:
    """Return a sorted DataFrame of feature importances.

    Works for tree-based models (Random Forest, XGBoost) and Logistic
    Regression (uses absolute coefficient values).

    Args:
        model: Trained model with ``feature_importances_`` or ``coef_``.
        feature_names: List of feature column names.

    Returns:
        DataFrame with columns ``feature`` and ``importance``, sorted descending.
    """
    if hasattr(model, "feature_importances_"):
        importances = model.feature_importances_
    elif hasattr(model, "coef_"):
        importances = np.abs(model.coef_[0])
    else:
        raise AttributeError(
            "Model does not expose feature_importances_ or coef_."
        )
    df = pd.DataFrame(
        {"feature": feature_names, "importance": importances}
    ).sort_values("importance", ascending=False)
    return df.reset_index(drop=True)
