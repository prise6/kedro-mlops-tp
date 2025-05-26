# %%
import matplotlib.pyplot as plt
import mlflow
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from notebooks.data_validation import read_model_input_table


# %%
def get_categorical_columns(df, max_unique_values=100):
    categorical_cols = []
    for col in df.columns:
        if df[col].dtype == "object" or df[col].nunique() <= max_unique_values:
            categorical_cols.append(col)
    return categorical_cols


# %%
MODEL_INPUT_FILEPATH = "data/03_primary/model_input_table.parquet"

# %%
mlflow.set_system_metrics_sampling_interval(interval=1)
mlflow.set_system_metrics_samples_before_logging(samples=1)

# %%
mlflow.set_experiment(experiment_name="demo")
with mlflow.start_run(
    log_system_metrics=True, tags={"env": "local", "school": "polytech"}
):
    input_table_df = read_model_input_table(MODEL_INPUT_FILEPATH)

    # metrics example: Backend store
    mlflow.log_metric(key="shape_x", value=input_table_df.shape[0])
    mlflow.log_metric(key="shape_y", value=input_table_df.shape[1])

    # figure artifacts: Artifact store
    fig, ax = plt.subplots()
    ax.hist(input_table_df["price"])
    mlflow.log_figure(fig, artifact_file="price_histogram.png")

    # raw artifact
    # mlflow.log_artifact(local_path=)

    # dataset
    dataset = mlflow.data.from_pandas(  # type: ignore
        input_table_df,
        source=MODEL_INPUT_FILEPATH,
        name="model_input_table",
        targets="price",
    )
    mlflow.log_input(dataset=dataset)

    # # test system metrics
    # time.sleep(15)

    # param example
    max_depth_param = 4
    mlflow.log_param("param_max_depth", max_depth_param)

    # model example
    # autolog actif
    mlflow.sklearn.autolog(
        log_input_examples=True, log_model_signatures=True, max_tuning_runs=1
    )

    X = input_table_df.drop(columns=["price", "id", "shuttle_location"], inplace=False)
    y = input_table_df["price"]

    categorical_cols = get_categorical_columns(X)

    # Create a ColumnTransformer for one-hot encoding
    preprocessor = ColumnTransformer(
        transformers=[("cat", OneHotEncoder(), categorical_cols)],
        remainder="passthrough",  # Laisse les colonnes non spécifiées inchangées
    )

    # Pipeline model: preprocessor and the model
    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            (
                "regressor",
                RandomForestRegressor(
                    criterion="squared_error",
                    max_depth=max_depth_param,
                    ccp_alpha=0,
                    random_state=17,
                    n_estimators=500,
                    oob_score=True,
                    verbose=False,
                ),
            ),
        ]
    )

    pipeline.fit(X=X, y=y)

    # non nécessaire si autolog actif
    # mlflow.sklearn.log_model(pipeline, artifact_path="pipeline")
    # Extract the OOB score from the RandomForestRegressor
    oob_score = pipeline.named_steps["regressor"].oob_score_

    # Log the OOB score as a metric
    mlflow.log_metric(key="oob_score", value=oob_score)

# %%
