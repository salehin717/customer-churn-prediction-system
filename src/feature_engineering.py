"""
Feature engineering module for the Customer Churn Prediction System.

Responsibilities:
- Construct domain-driven features from raw attributes.
- Create interaction terms between existing features.
- Aggregate customer service usage metrics.
- Select the most informative features for modelling.

TODO: Implement all feature engineering steps.
"""

import logging
from typing import List

import pandas as pd

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------


def create_tenure_groups(df: pd.DataFrame) -> pd.DataFrame:
    """Bin the continuous 'tenure' column into categorical groups.

    Args:
        df: Input DataFrame containing a 'tenure' column.

    Returns:
        DataFrame with an additional 'tenure_group' column.

    TODO: Define sensible bin edges and group labels.
    """
    logger.info("Creating tenure group feature.")
    # TODO: pd.cut(df["tenure"], bins=[...], labels=[...])
    raise NotImplementedError("create_tenure_groups is not yet implemented.")


def create_monthly_charges_ratio(df: pd.DataFrame) -> pd.DataFrame:
    """Compute the ratio of monthly charges to total charges.

    Args:
        df: Input DataFrame with 'MonthlyCharges' and 'TotalCharges'.

    Returns:
        DataFrame with an additional 'charges_ratio' column.

    TODO: Handle division-by-zero when TotalCharges == 0.
    """
    logger.info("Creating monthly charges ratio feature.")
    # TODO: df["charges_ratio"] = (
    #     df["MonthlyCharges"] / df["TotalCharges"].replace(0, 1)
    # )
    raise NotImplementedError("create_monthly_charges_ratio is not yet implemented.")


def create_service_count(df: pd.DataFrame) -> pd.DataFrame:
    """Count the total number of active services per customer.

    Args:
        df: Input DataFrame with individual service columns.

    Returns:
        DataFrame with an additional 'service_count' column.

    TODO: Identify and sum boolean service indicator columns.
    """
    logger.info("Creating service count feature.")
    # TODO: service_cols = [...]; df["service_count"] = df[service_cols].sum(axis=1)
    raise NotImplementedError("create_service_count is not yet implemented.")


def select_features(df: pd.DataFrame, target_column: str = "Churn") -> List[str]:
    """Return a list of feature column names excluding the target.

    Args:
        df: Fully engineered DataFrame.
        target_column: Name of the target variable column.

    Returns:
        List of feature column names.

    TODO: Apply feature selection (e.g., correlation threshold, RFE).
    """
    logger.info("Selecting features (excluding '%s').", target_column)
    # TODO: implement feature selection logic
    raise NotImplementedError("select_features is not yet implemented.")


def run_feature_engineering_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    """Execute all feature engineering steps in sequence.

    Args:
        df: Preprocessed DataFrame.

    Returns:
        DataFrame enriched with engineered features.

    TODO: Chain all feature construction functions.
    """
    logger.info("Starting feature engineering pipeline.")
    # TODO: df = create_tenure_groups(df)
    # TODO: df = create_monthly_charges_ratio(df)
    # TODO: df = create_service_count(df)
    raise NotImplementedError(
        "run_feature_engineering_pipeline is not yet implemented."
    )
