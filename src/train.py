"""
Model training module for the Customer Churn Prediction System.

Responsibilities:
- Define candidate classifiers (Logistic Regression, Random Forest, XGBoost).
- Configure hyperparameter search spaces.
- Train models using cross-validation.
- Serialise the best model to the models/ directory using joblib.

TODO: Implement all training steps.
"""

import logging
from pathlib import Path
from typing import Any, Dict, Optional

import pandas as pd

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

MODELS_DIR = Path(__file__).resolve().parent.parent / "models"
DEFAULT_RANDOM_STATE = 42

# ---------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------


def get_candidate_models() -> Dict[str, Any]:
    """Return a dictionary of candidate sklearn-compatible estimators.

    Returns:
        Mapping of model name to estimator instance.

    TODO: Instantiate LogisticRegression, RandomForestClassifier, XGBClassifier.
    """
    logger.info("Building candidate model dictionary.")
    # TODO: from sklearn.linear_model import LogisticRegression
    # TODO: from sklearn.ensemble import RandomForestClassifier
    # TODO: from xgboost import XGBClassifier
    raise NotImplementedError("get_candidate_models is not yet implemented.")


def train_model(
    model: Any,
    X_train: pd.DataFrame,
    y_train: pd.Series,
    model_name: str = "model",
) -> Any:
    """Fit a single estimator on the training data.

    Args:
        model: An sklearn-compatible estimator.
        X_train: Training feature matrix.
        y_train: Training target series.
        model_name: Identifier used for logging.

    Returns:
        The fitted estimator.

    TODO: Add cross-validation scoring before final fit.
    """
    logger.info("Training model: %s", model_name)
    # TODO: model.fit(X_train, y_train)
    raise NotImplementedError("train_model is not yet implemented.")


def tune_hyperparameters(
    model: Any,
    X_train: pd.DataFrame,
    y_train: pd.Series,
    param_grid: Dict[str, Any],
    cv: int = 5,
) -> Any:
    """Run a grid search to find the best hyperparameters.

    Args:
        model: Base estimator to tune.
        X_train: Training feature matrix.
        y_train: Training target series.
        param_grid: Dictionary of parameter names to search values.
        cv: Number of cross-validation folds.

    Returns:
        Best fitted estimator from the grid search.

    TODO: Implement GridSearchCV or RandomizedSearchCV.
    """
    logger.info("Tuning hyperparameters with %d-fold CV.", cv)
    # TODO: from sklearn.model_selection import GridSearchCV
    raise NotImplementedError("tune_hyperparameters is not yet implemented.")


def save_model(model: Any, filename: str = "churn_model.pkl") -> Path:
    """Serialise a trained model to disk using joblib.

    Args:
        model: Fitted estimator to save.
        filename: Output filename within the models/ directory.

    Returns:
        Path to the saved model file.

    TODO: Implement model serialisation with versioning.
    """
    output_path = MODELS_DIR / filename
    logger.info("Saving model to %s", output_path)
    # TODO: import joblib; joblib.dump(model, output_path)
    raise NotImplementedError("save_model is not yet implemented.")


def run_training_pipeline(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    output_filename: Optional[str] = None,
) -> Any:
    """Execute the full training pipeline end-to-end.

    Args:
        X_train: Training feature matrix.
        y_train: Training target series.
        output_filename: Optional filename for the saved model.

    Returns:
        The best fitted estimator.

    TODO: Chain candidate models → tuning → save best model.
    """
    logger.info("Starting training pipeline.")
    # TODO: models = get_candidate_models()
    # TODO: train, tune, evaluate each model
    # TODO: save_model(best_model)
    raise NotImplementedError("run_training_pipeline is not yet implemented.")
