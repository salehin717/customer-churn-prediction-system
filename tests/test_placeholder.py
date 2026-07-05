"""
Placeholder tests for the Customer Churn Prediction System.

These tests verify that the project scaffolding is correctly set up and that
each module is importable. Full unit and integration tests will be added
alongside implementation in subsequent development phases.

TODO: Replace placeholder tests with meaningful unit tests for each module.
"""

import importlib
from pathlib import Path

# ---------------------------------------------------------------------------
# Project structure tests
# ---------------------------------------------------------------------------


def test_src_package_importable() -> None:
    """Verify that the src package can be imported without errors."""
    module = importlib.import_module("src")
    assert module is not None


def test_app_package_importable() -> None:
    """Verify that the app package can be imported without errors."""
    module = importlib.import_module("app")
    assert module is not None


def test_required_src_modules_exist() -> None:
    """Verify that all required src module files are present on disk."""
    src_dir = Path(__file__).resolve().parent.parent / "src"
    expected_modules = [
        "__init__.py",
        "preprocessing.py",
        "feature_engineering.py",
        "train.py",
        "evaluate.py",
        "predict.py",
        "utils.py",
    ]
    for module_file in expected_modules:
        assert (
            src_dir / module_file
        ).is_file(), f"Expected src/{module_file} to exist."


def test_required_app_files_exist() -> None:
    """Verify that all required app files are present on disk."""
    app_dir = Path(__file__).resolve().parent.parent / "app"
    expected_files = ["__init__.py", "app.py"]
    for filename in expected_files:
        assert (app_dir / filename).is_file(), f"Expected app/{filename} to exist."


def test_data_directories_exist() -> None:
    """Verify that data subdirectories are present."""
    base = Path(__file__).resolve().parent.parent / "data"
    assert (base / "raw").is_dir(), "data/raw/ directory should exist."
    assert (base / "processed").is_dir(), "data/processed/ directory should exist."


def test_models_directory_exists() -> None:
    """Verify that the models directory is present."""
    models_dir = Path(__file__).resolve().parent.parent / "models"
    assert models_dir.is_dir(), "models/ directory should exist."


def test_requirements_file_exists() -> None:
    """Verify that requirements.txt is present at the project root."""
    req_file = Path(__file__).resolve().parent.parent / "requirements.txt"
    assert req_file.is_file(), "requirements.txt should exist at the project root."


def test_pyproject_toml_exists() -> None:
    """Verify that pyproject.toml is present at the project root."""
    pyproject = Path(__file__).resolve().parent.parent / "pyproject.toml"
    assert pyproject.is_file(), "pyproject.toml should exist at the project root."


# ---------------------------------------------------------------------------
# Utility module tests
# ---------------------------------------------------------------------------


def test_pipeline_config_defaults() -> None:
    """Verify that PipelineConfig initialises with sensible defaults."""
    from src.utils import PipelineConfig

    config = PipelineConfig()
    assert config.test_size == 0.2
    assert config.random_state == 42
    assert config.target_column == "Churn"
    assert config.raw_data_dir.name == "raw"
    assert config.processed_data_dir.name == "processed"


def test_ensure_dir_creates_directory(tmp_path: Path) -> None:
    """Verify that ensure_dir creates a new directory."""
    from src.utils import ensure_dir

    new_dir = tmp_path / "test_subdir" / "nested"
    result = ensure_dir(new_dir)
    assert result.is_dir()


def test_validate_dataframe_passes_with_all_columns() -> None:
    """Verify that validate_dataframe returns True when all columns present."""
    import pandas as pd

    from src.utils import validate_dataframe

    df = pd.DataFrame({"a": [1], "b": [2], "Churn": [0]})
    assert validate_dataframe(df, ["a", "b", "Churn"]) is True


def test_validate_dataframe_fails_with_missing_column() -> None:
    """Verify that validate_dataframe returns False when a column is missing."""
    import pandas as pd

    from src.utils import validate_dataframe

    df = pd.DataFrame({"a": [1]})
    assert validate_dataframe(df, ["a", "missing_col"]) is False


def test_set_random_seed_runs_without_error() -> None:
    """Verify that set_random_seed does not raise an exception."""
    from src.utils import set_random_seed

    set_random_seed(0)  # should not raise


# ---------------------------------------------------------------------------
# Stub / NotImplementedError tests
# ---------------------------------------------------------------------------


def test_preprocessing_stubs_raise_not_implemented() -> None:
    """Verify that preprocessing stubs raise NotImplementedError."""
    import pytest

    from src.preprocessing import (
        encode_categoricals,
        handle_missing_values,
        load_raw_data,
        scale_numerics,
    )

    with pytest.raises(NotImplementedError):
        load_raw_data()
    with pytest.raises(NotImplementedError):
        handle_missing_values(None)  # type: ignore[arg-type]
    with pytest.raises(NotImplementedError):
        encode_categoricals(None)  # type: ignore[arg-type]
    with pytest.raises(NotImplementedError):
        scale_numerics(None)  # type: ignore[arg-type]


def test_train_stubs_raise_not_implemented() -> None:
    """Verify that training stubs raise NotImplementedError."""
    import pytest

    from src.train import get_candidate_models

    with pytest.raises(NotImplementedError):
        get_candidate_models()


def test_predict_stubs_raise_not_implemented() -> None:
    """Verify that prediction stubs raise NotImplementedError."""
    import pytest

    from src.predict import load_model

    with pytest.raises(NotImplementedError):
        load_model()
