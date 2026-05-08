import os
import time
import mlflow


class MLflowTracker:

    def __init__(self):

        tracking_dir = os.path.abspath(
            "storage/mlflow"
        )

        os.makedirs(
            tracking_dir,
            exist_ok=True
        )

        tracking_uri = (
            f"sqlite:///{tracking_dir}/mlflow.db"
        )

        mlflow.set_tracking_uri(
            tracking_uri
        )

        mlflow.set_experiment(
            "ResearchOpsAI"
        )

    def start_run(
        self,
        run_name
    ):

        mlflow.start_run(
            run_name=run_name
        )

        self.start_time = time.time()

    def log_param(
        self,
        key,
        value
    ):

        mlflow.log_param(
            key,
            value
        )

    def log_metric(
        self,
        key,
        value
    ):

        mlflow.log_metric(
            key,
            value
        )

    def log_text(
        self,
        text,
        artifact_file
    ):

        mlflow.log_text(
            text,
            artifact_file
        )

    def end_run(self):

        total_time = (
            time.time() -
            self.start_time
        )

        mlflow.log_metric(
            "workflow_duration_seconds",
            total_time
        )

        mlflow.end_run()