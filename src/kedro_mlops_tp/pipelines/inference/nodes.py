import pandas as pd
from sklearn.linear_model import LinearRegression


def select_features(data: pd.DataFrame, model_options: dict) -> list:
    """select features from model input table

    Args:
        data (pd.DataFrame): model input table preprocessed
        features (list): list of features

    Returns:
        pd.DataFrame: features table
    """
    X_features = data[model_options.get("features", [])]
    return X_features


def predict(model: LinearRegression, data: pd.DataFrame) -> pd.DataFrame:
    """prediction on features tables

    Args:
        model (LinearRegression): linear regression model
        data (pd.DataFrame): feature table

    Returns:
        pd.DataFrame: prediction (price_pred) combined with features
    """
    data["price_pred"] = model.predict(data)

    return data
