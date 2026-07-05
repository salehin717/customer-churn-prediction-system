"""
Prediction module for the Customer Churn Prediction System.

Responsibilities:
- Load a serialised model from disk.
- Accept new customer data as input.
- Return churn probability and binary prediction.
- Format predictions for downstream consumption (API, dashboard).

TODO: Implement all inference steps.
"""

import logging
from pathlib import Path
from typing import Any, Union

import pandas as pd

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

MODELS_DIR = Path(__file__).resolve().parent.parent / "models"
DEFAULT_MODEL_FILENAME = "churn_model.pkl"

# ---------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------


def load_model(filename: str = DEFAULT_MODEL_FILENAME) -> Any:
    """Deserialise a trained model from the models/ directory.

    Args:
        filename: Name of the model file to load.

    Returns:
        Loaded sklearn-compatible estimator.

    Raises:
        FileNotFoundError: If the model file does not exist.

    TODO: Implement model loading with joblib.
    """
    model_path = MODELS_DIR / filename
    logger.info("Loading model from %s", model_path)
    # TODO: import joblib; return joblib.load(model_path)
    raise NotImplementedError("load_model is not yet implemented.")


def preprocess_input(data: Union[dict, pd.DataFrame]) -> pd.DataFrame:
    """Transform raw input data into the format expected by the model.

    Args:
        data: A single customer record (dict) or a DataFrame of records.

    Returns:
        Preprocessed DataFrame ready for inference.

    TODO: Apply the same preprocessing steps used during training.
    """
    logger.info("Preprocessing prediction input.")
    # TODO: handle dict → DataFrame conversion
    # TODO: apply encoding, scaling consistent with training pipeline
    raise NotImplementedError("preprocess_input is not yet implemented.")


def predict_churn(
    model: Any,
    data: Union[dict, pd.DataFrame],
) -> pd.DataFrame:
    """Generate churn predictions for new customer data.

    Args:
        model: Fitted estimator.
        data: Raw customer data (dict or DataFrame).

    Returns:
        DataFrame with columns ['prediction', 'churn_probability'].

    TODO: Implement inference and result formatting.
    """
    logger.info("Generating churn predictions.")
    # TODO: X = preprocess_input(data)
    # TODO: predictions = model.predict(X)
    # TODO: probabilities = model.predict_proba(X)[:, 1]
    raise NotImplementedError("predict_churn is not yet implemented.")


def run_prediction_pipeline(
    input_path: Union[str, Path],
    model_filename: str = DEFAULT_MODEL_FILENAME,
    output_path: Union[str, Path, None] = None,
) -> pd.DataFrame:
    """Execute the full inference pipeline end-to-end.

    Args:
        input_path: Path to the input CSV file with customer data.
        model_filename: Name of the serialised model file.
        output_path: Optional path to save prediction results as CSV.

    Returns:
        DataFrame with prediction results.

    TODO: Chain load model → preprocess → predict → save results.
    """
    logger.info("Starting prediction pipeline.")
    # TODO: model = load_model(model_filename)
    # TODO: data = pd.read_csv(input_path)
    # TODO: results = predict_churn(model, data)
    raise NotImplementedError("run_prediction_pipeline is not yet implemented.")
