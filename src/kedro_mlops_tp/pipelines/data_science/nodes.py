import logging
from typing import Any

import mlflow
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import max_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


def split_data(data: pd.DataFrame, parameters: dict) -> tuple:
    """Splits data into features and targets training and test sets.

    Args:
        data: Data containing features and target.
        parameters: Parameters defined in parameters/data_science.yml.
    Returns:
        Split data.
    """
    X = data[parameters["features"]]
    y = data["price"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=parameters["test_size"], random_state=parameters["random_state"]
    )
    return X_train, X_test, y_train, y_test


def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> LinearRegression:
    """Trains the linear regression model.

    Args:
        X_train: Training data of independent features.
        y_train: Training data for price.

    Returns:
        Trained model.
    """
    mlflow.sklearn.autolog(
        log_input_examples=True, log_model_signatures=True, log_models=True
    )
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    mlflow.sklearn.autolog(disable=True)
    return regressor


def evaluate_model(
    regressor: LinearRegression, X_test: pd.DataFrame, y_test: pd.Series
) -> dict[str, Any]:
    """Calculates and logs the coefficient of determination.

    Args:
        regressor: Trained model.
        X_test: Testing data of independent features.
        y_test: Testing data for price.
    """
    y_pred = regressor.predict(X_test)
    score = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    me = max_error(y_test, y_pred)
    logger = logging.getLogger(__name__)
    logger.info("Model has a coefficient R^2 of %.3f on test data.", score)

    if not (active_run := mlflow.active_run()):
        return {"r2_score": score, "mae": mae, "max_error": me}

    run_id = active_run.info.run_id

    eval_data = X_test
    eval_data["price"] = y_test

    eval_dataset = mlflow.data.from_pandas(  # type: ignore
        eval_data,
        name="test_dataset",
        targets="price",
    )

    mlflow.evaluate(
        f"runs:/{run_id}/model",
        eval_dataset,
        model_type="regressor",
        env_manager="local",
    )

    return {
        "r2_score": {"value": score, "step": 1},
        "mae": {"value": mae, "step": 1},
        "max_error": {"value": me, "step": 1},
    }
