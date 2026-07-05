"""
Shared utility functions for the Customer Churn Prediction System.

Provides helper utilities used across multiple pipeline modules:
- File I/O helpers
- Logging configuration
- Reproducibility utilities
- Data validation helpers

TODO: Implement utility functions as needed by other modules.
"""

import logging
import random
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import numpy as np

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------


@dataclass
class PipelineConfig:
    """Central configuration for the ML pipeline.

    Attributes:
        raw_data_dir: Path to the raw data directory.
        processed_data_dir: Path to the processed data directory.
        models_dir: Path to the models directory.
        reports_dir: Path to the reports directory.
        test_size: Fraction of data reserved for testing.
        random_state: Global random seed for reproducibility.
        target_column: Name of the target variable.
    """

    raw_data_dir: Path = field(
        default_factory=lambda: Path(__file__).resolve().parent.parent / "data" / "raw"
    )
    processed_data_dir: Path = field(
        default_factory=lambda: Path(__file__).resolve().parent.parent
        / "data"
        / "processed"
    )
    models_dir: Path = field(
        default_factory=lambda: Path(__file__).resolve().parent.parent / "models"
    )
    reports_dir: Path = field(
        default_factory=lambda: Path(__file__).resolve().parent.parent / "reports"
    )
    test_size: float = 0.2
    random_state: int = 42
    target_column: str = "Churn"


# ---------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------


def setup_logging(
    level: int = logging.INFO,
    log_format: str = "%(asctime)s [%(levelname)s] %(name)s – %(message)s",
) -> None:
    """Configure root logger for the application.

    Args:
        level: Logging level (e.g., logging.INFO, logging.DEBUG).
        log_format: Format string for log messages.

    TODO: Optionally add a file handler to persist logs.
    """
    logging.basicConfig(level=level, format=log_format)
    logger.info("Logging configured at level %s.", logging.getLevelName(level))


def set_random_seed(seed: int = 42) -> None:
    """Set random seeds for Python, NumPy, and any ML frameworks.

    Args:
        seed: Integer seed value.

    TODO: Extend to cover torch / tensorflow seeds if added later.
    """
    random.seed(seed)
    np.random.seed(seed)
    logger.info("Random seed set to %d.", seed)


def ensure_dir(path: Path) -> Path:
    """Create a directory (and parents) if it does not already exist.

    Args:
        path: Target directory path.

    Returns:
        The resolved directory path.
    """
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    logger.debug("Directory ensured: %s", path)
    return path


def validate_dataframe(
    df,
    required_columns: list,
    name: Optional[str] = None,
) -> bool:
    """Check that a DataFrame contains all required columns.

    Args:
        df: pandas DataFrame to validate.
        required_columns: List of expected column names.
        name: Optional label for the DataFrame used in log messages.

    Returns:
        True if all required columns are present, False otherwise.

    TODO: Add dtype validation and value range checks.
    """
    label = name or "DataFrame"
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        logger.warning("%s is missing columns: %s", label, missing)
        return False
    logger.info("%s validation passed.", label)
    return True
