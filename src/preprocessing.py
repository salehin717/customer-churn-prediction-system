"""
Data preprocessing module for the Customer Churn Prediction System.

Responsibilities:
- Load raw CSV data from the data/raw directory.
- Handle missing values and data type inconsistencies.
- Encode categorical features.
- Scale numerical features.
- Split data into training and test sets.
- Persist cleaned data to data/processed.

TODO: Implement all preprocessing steps.
"""

import logging
from pathlib import Path
from typing import Optional, Tuple

import pandas as pd

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

RAW_DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"
PROCESSED_DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "processed"
TARGET_COLUMN = "Churn"

# ---------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------


def load_raw_data(filename: str = "telco_churn.csv") -> pd.DataFrame:
    """Load the raw Telco Customer Churn CSV file.

    Args:
        filename: Name of the raw CSV file inside data/raw/.

    Returns:
        DataFrame containing the raw dataset.

    Raises:
        FileNotFoundError: If the specified file does not exist.

    TODO: Implement file loading with validation.
    """
    filepath = RAW_DATA_DIR / filename
    logger.info("Loading raw data from %s", filepath)
    # TODO: return pd.read_csv(filepath)
    raise NotImplementedError("load_raw_data is not yet implemented.")


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Impute or drop rows/columns with missing values.

    Args:
        df: Input DataFrame.

    Returns:
        DataFrame with missing values handled.

    TODO: Implement missing value strategy per column type.
    """
    logger.info("Handling missing values.")
    # TODO: implement imputation strategy
    raise NotImplementedError("handle_missing_values is not yet implemented.")


def encode_categoricals(df: pd.DataFrame) -> pd.DataFrame:
    """Encode categorical columns as numeric values.

    Args:
        df: Input DataFrame.

    Returns:
        DataFrame with categorical features encoded.

    TODO: Apply one-hot or ordinal encoding as appropriate.
    """
    logger.info("Encoding categorical features.")
    # TODO: implement encoding
    raise NotImplementedError("encode_categoricals is not yet implemented.")


def scale_numerics(df: pd.DataFrame) -> pd.DataFrame:
    """Standardise or normalise numerical features.

    Args:
        df: Input DataFrame.

    Returns:
        DataFrame with scaled numerical features.

    TODO: Apply StandardScaler or MinMaxScaler.
    """
    logger.info("Scaling numerical features.")
    # TODO: implement scaling
    raise NotImplementedError("scale_numerics is not yet implemented.")


def split_data(
    df: pd.DataFrame,
    test_size: float = 0.2,
    random_state: int = 42,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Split the dataset into training and test sets.

    Args:
        df: Preprocessed DataFrame including the target column.
        test_size: Proportion of data to reserve for testing.
        random_state: Seed for reproducibility.

    Returns:
        Tuple of (X_train, X_test, y_train, y_test).

    TODO: Implement train/test split with stratification.
    """
    logger.info(
        "Splitting data: test_size=%.2f, random_state=%d", test_size, random_state
    )
    # TODO: from sklearn.model_selection import train_test_split
    raise NotImplementedError("split_data is not yet implemented.")


def run_preprocessing_pipeline(
    filename: str = "telco_churn.csv",
    output_filename: Optional[str] = None,
) -> pd.DataFrame:
    """Execute the full preprocessing pipeline end-to-end.

    Args:
        filename: Raw data filename.
        output_filename: Optional filename to save processed data.

    Returns:
        Fully preprocessed DataFrame.

    TODO: Chain all preprocessing steps together.
    """
    logger.info("Starting preprocessing pipeline.")
    # TODO: chain load → missing values → encode → scale → save
    raise NotImplementedError("run_preprocessing_pipeline is not yet implemented.")
