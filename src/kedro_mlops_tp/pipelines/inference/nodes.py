import mlflow
import pandas as pd
from interpret.blackbox import LimeTabular
from mlflow.pyfunc import PyFuncModel


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


def predict(model: PyFuncModel, data: pd.DataFrame) -> pd.DataFrame:
    """prediction on features tables

    Args:
        model (LinearRegression): linear regression model
        data (pd.DataFrame): feature table

    Returns:
        pd.DataFrame: prediction (price_pred) combined with features
    """
    data["price_pred"] = model.predict(data)

    return data


def explain(regressor: PyFuncModel, X_train: pd.DataFrame, data: pd.DataFrame):
    sample_data = data.sample(n=20, random_state=17)
    data_x = sample_data.drop(columns=["price_pred"])
    data_y = sample_data["price_pred"]

    # TODO: must be built in training
    lime = LimeTabular(regressor.get_raw_model(), X_train, random_state=17)
    explanations = lime.explain_local(data_x, data_y)
    figs = [explanations.visualize(key=ix) for ix in range(sample_data.shape[0])]
    for ix, fig in enumerate(figs):
        mlflow.log_figure(fig, artifact_file=f"local_explanation_{ix}.html")
