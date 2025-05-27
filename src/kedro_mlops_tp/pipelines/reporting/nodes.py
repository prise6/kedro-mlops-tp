import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px  # noqa:  F401
import plotly.graph_objs as go
import seaborn as sn
from evidently import Report
from evidently.presets import DataDriftPreset, DataSummaryPreset


# This function uses plotly.express
def compare_passenger_capacity_exp(preprocessed_shuttles: pd.DataFrame):
    return (
        preprocessed_shuttles.groupby(["shuttle_type"])
        .mean(numeric_only=True)
        .reset_index()
    )


# This function uses plotly.graph_objects
def compare_passenger_capacity_go(preprocessed_shuttles: pd.DataFrame):
    data_frame = (
        preprocessed_shuttles.groupby(["shuttle_type"])
        .mean(numeric_only=True)
        .reset_index()
    )
    fig = go.Figure(
        [
            go.Bar(
                x=data_frame["shuttle_type"],
                y=data_frame["passenger_capacity"],
            )
        ]
    )

    return fig


def create_confusion_matrix(companies: pd.DataFrame):
    actuals = [0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1]
    predicted = [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1]
    data = {"y_Actual": actuals, "y_Predicted": predicted}
    df = pd.DataFrame(data, columns=["y_Actual", "y_Predicted"])
    confusion_matrix = pd.crosstab(
        df["y_Actual"], df["y_Predicted"], rownames=["Actual"], colnames=["Predicted"]
    )
    sn.heatmap(confusion_matrix, annot=True)
    return plt


def create_evidently_report(preprocessed_shuttles: pd.DataFrame):
    """
    Crée un rapport Evidently pour analyser la dérive des données
    """
    # Créer un rapport de dérive de données
    report = Report(metrics=[DataDriftPreset(), DataSummaryPreset()])

    # Diviser les données en deux périodes pour la comparaison
    reference_data = preprocessed_shuttles.iloc[: len(preprocessed_shuttles) // 2]
    current_data = preprocessed_shuttles.iloc[len(preprocessed_shuttles) // 2 :]

    # Générer le rapport
    my_report = report.run(reference_data=reference_data, current_data=current_data)

    # Sauvegarder le rapport au format HTML
    # my_report.save_html("data/08_reporting/evidently_report.html")
    # buffer = StringIO()
    # my_report.save_html(filename=buffer)

    return my_report._repr_html_()
