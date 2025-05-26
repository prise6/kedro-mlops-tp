"""Project pipelines."""

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline


def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines()
    # pipelines["__default__"] = sum(pipelines.values())  # type: ignore
    pipelines["__default__"] = Pipeline(
        [
            pipelines["data_processing"],
            pipelines["data_science"],
            pipelines["inference"],
            pipelines["reporting"],
        ]
    )
    pipelines["training"] = Pipeline(
        [
            pipelines["data_processing"],
            pipelines["data_science"],
        ]
    )
    pipelines["prediction"] = Pipeline(
        [
            pipelines["inference"],
            pipelines["reporting"],
        ]
    )
    return pipelines
