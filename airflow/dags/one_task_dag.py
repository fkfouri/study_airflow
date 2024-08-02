"""One Task DAG"""

from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow import DAG

default_args = {
    "owner": "Fabio",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "catchup": False,
    "start_date": datetime(2023, 1, 1),
}

with DAG(
    dag_id="one_task_dag",
    description="A one task Airflow DAG BASH",
    schedule_interval=None,
    default_args=default_args,
    tags=["fabio"],
) as dag:

    task1 = BashOperator(
        task_id="one_task",
        bash_command='echo "hello, world!" > /workspaces/study_airflow/lab/create-this-file.txt',
        dag=dag,
    )
