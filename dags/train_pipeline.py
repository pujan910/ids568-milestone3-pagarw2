from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

def on_failure_callback(context):
    dag_id = context.get("dag").dag_id if context.get("dag") else "unknown"
    task_id = context.get("task_instance").task_id if context.get("task_instance") else "unknown"
    print(f"Task failed: DAG={dag_id}, task={task_id}")

default_args = {
    "owner": "mlops",
    "retries": 2,
    "retry_delay": timedelta(minutes=1),
    "on_failure_callback": on_failure_callback,
}

with DAG(
    dag_id="train_pipeline",
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    preprocess_data = BashOperator(
        task_id="preprocess_data",
        bash_command="echo preprocessing",
    )

    train_model = BashOperator(
        task_id="train_model",
        bash_command="python train.py",
    )

    register_model = BashOperator(
        task_id="register_model",
        bash_command="echo registering model",
    )

    preprocess_data >> train_model >> register_model