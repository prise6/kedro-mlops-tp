# hooks/mlflow_experience_hook.py
import os

import mlflow
from kedro.framework.hooks import hook_impl


class MlflowExperienceHook:
    @hook_impl
    def before_pipeline_run(self, pipeline, catalog, run_params, **kwargs):
        os.environ["MLFLOW_ENABLE_SYSTEM_METRICS_LOGGING"] = "1"
        mlflow.enable_system_metrics_logging()
        mlflow.set_system_metrics_sampling_interval(interval=1)
        mlflow.set_system_metrics_samples_before_logging(samples=1)
