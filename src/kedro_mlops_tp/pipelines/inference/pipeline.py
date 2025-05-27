from kedro.pipeline import Pipeline, node, pipeline

from kedro_mlops_tp.pipelines.data_processing.nodes import create_model_input_table

from .nodes import explain, predict, select_features


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=create_model_input_table,
                inputs=[
                    "preprocessed_shuttles",
                    "preprocessed_companies",
                    "new_reviews",
                ],
                outputs="new_model_input_table",
                name="create_model_inference_table_node",
            ),
            node(
                func=select_features,
                inputs=["new_model_input_table", "params:model_options"],
                outputs="inference_features",
                name="select_features_node",
            ),
            node(
                func=predict,
                inputs=["selected_regressor", "inference_features"],
                outputs="new_predictions",
                name="predict_node",
            ),
            node(
                func=explain,
                inputs=["selected_regressor", "X_train", "new_predictions"],
                outputs=None,
                name="explain_node",
            ),
        ]
    )
