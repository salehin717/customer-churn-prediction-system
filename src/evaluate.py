"""
Model evaluation module for the Customer Churn Prediction System.

Responsibilities:
- Compute classification metrics (accuracy, ROC-AUC, F1, precision, recall).
- Generate confusion matrix visualisations.
- Plot ROC and precision-recall curves.
- Produce SHAP-based feature importance explanations.
- Save evaluation reports to the reports/ directory.

TODO: Implement all evaluation steps.
"""

import logging
from pathlib import Path
from typing import Any, Dict

import pandas as pd

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

REPORTS_DIR = Path(__file__).resolve().parent.parent / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# ---------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------


def compute_metrics(
    y_true: pd.Series,
    y_pred: pd.Series,
    y_prob: pd.Series,
) -> Dict[str, float]:
    """Calculate standard binary classification metrics.

    Args:
        y_true: Ground truth labels.
        y_pred: Predicted class labels.
        y_prob: Predicted probabilities for the positive class.

    Returns:
        Dictionary mapping metric names to their values.

    TODO: Compute accuracy, ROC-AUC, F1, precision, recall.
    """
    logger.info("Computing classification metrics.")
    # TODO: from sklearn.metrics import accuracy_score, roc_auc_score, ...
    raise NotImplementedError("compute_metrics is not yet implemented.")


def plot_confusion_matrix(
    y_true: pd.Series,
    y_pred: pd.Series,
    save: bool = True,
) -> None:
    """Plot and optionally save the confusion matrix.

    Args:
        y_true: Ground truth labels.
        y_pred: Predicted class labels.
        save: Whether to save the figure to reports/figures/.

    TODO: Implement matplotlib confusion matrix plot.
    """
    logger.info("Plotting confusion matrix.")
    # TODO: from sklearn.metrics import ConfusionMatrixDisplay
    raise NotImplementedError("plot_confusion_matrix is not yet implemented.")


def plot_roc_curve(
    y_true: pd.Series,
    y_prob: pd.Series,
    save: bool = True,
) -> None:
    """Plot the Receiver Operating Characteristic curve.

    Args:
        y_true: Ground truth labels.
        y_prob: Predicted probabilities for the positive class.
        save: Whether to save the figure to reports/figures/.

    TODO: Implement ROC curve with AUC annotation.
    """
    logger.info("Plotting ROC curve.")
    # TODO: from sklearn.metrics import RocCurveDisplay
    raise NotImplementedError("plot_roc_curve is not yet implemented.")


def explain_with_shap(model: Any, X_test: pd.DataFrame) -> None:
    """Generate SHAP summary and waterfall plots for model explainability.

    Args:
        model: Fitted estimator compatible with SHAP.
        X_test: Test feature matrix.

    TODO: Implement SHAP TreeExplainer or LinearExplainer as appropriate.
    """
    logger.info("Generating SHAP explanations.")
    # TODO: import shap; explainer = shap.Explainer(model, X_test)
    raise NotImplementedError("explain_with_shap is not yet implemented.")


def run_evaluation_pipeline(
    model: Any,
    X_test: pd.DataFrame,
    y_test: pd.Series,
) -> Dict[str, float]:
    """Execute the full evaluation pipeline end-to-end.

    Args:
        model: Fitted estimator.
        X_test: Test feature matrix.
        y_test: Test target series.

    Returns:
        Dictionary of evaluation metrics.

    TODO: Chain metrics → confusion matrix → ROC → SHAP.
    """
    logger.info("Starting evaluation pipeline.")
    # TODO: y_pred = model.predict(X_test)
    # TODO: y_prob = model.predict_proba(X_test)[:, 1]
    # TODO: metrics = compute_metrics(y_test, y_pred, y_prob)
    # TODO: plot_confusion_matrix(y_test, y_pred)
    # TODO: plot_roc_curve(y_test, y_prob)
    # TODO: explain_with_shap(model, X_test)
    raise NotImplementedError("run_evaluation_pipeline is not yet implemented.")
