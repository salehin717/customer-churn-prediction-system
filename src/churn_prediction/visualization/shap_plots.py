"""SHAP-based model explanation utilities."""

from typing import Any

import matplotlib.pyplot as plt
import shap


def compute_shap_values(model: Any, X) -> shap.Explanation:
    """Compute SHAP values for the given model and dataset.

    Uses ``TreeExplainer`` for tree-based models and falls back to
    ``LinearExplainer`` for linear models.

    Args:
        model: Trained classifier (tree-based or linear).
        X: Feature matrix (pandas DataFrame or numpy array).

    Returns:
        SHAP Explanation object.
    """
    try:
        explainer = shap.TreeExplainer(model)
    except Exception:
        explainer = shap.LinearExplainer(model, X)
    return explainer(X)


def plot_shap_summary(shap_values: shap.Explanation, X, max_display: int = 20):
    """Render a SHAP beeswarm summary plot.

    Args:
        shap_values: SHAP Explanation object.
        X: Feature matrix used to compute SHAP values.
        max_display: Maximum number of features to show.

    Returns:
        Matplotlib Figure object.
    """
    shap.summary_plot(shap_values, X, max_display=max_display, show=False)
    return plt.gcf()


def plot_shap_waterfall(shap_values: shap.Explanation, index: int = 0):
    """Render a SHAP waterfall plot for a single prediction.

    Args:
        shap_values: SHAP Explanation object.
        index: Row index to explain.

    Returns:
        Matplotlib Figure object.
    """
    shap.waterfall_plot(shap_values[index], show=False)
    return plt.gcf()


def plot_shap_bar(shap_values: shap.Explanation, max_display: int = 20):
    """Render a SHAP mean absolute value bar chart.

    Args:
        shap_values: SHAP Explanation object.
        max_display: Maximum number of features to show.

    Returns:
        Matplotlib Figure object.
    """
    shap.summary_plot(
        shap_values, plot_type="bar", max_display=max_display, show=False
    )
    return plt.gcf()
