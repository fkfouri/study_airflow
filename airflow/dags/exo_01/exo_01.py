"""One Task DAG"""
import os
import pandas as pd
from datetime import datetime, date
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
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
    dag_id="exo_01",
    description="Exo 01",
    schedule_interval=None,
    default_args=default_args,
    tags=["fabio"],
) as dag:

    create_path = BashOperator(
        task_id="create_path",
        bash_command="mkdir -p /workspaces/study_airflow/data",
        dag=dag,
    )

    extract_task = BashOperator(
        task_id="extract_task",
        bash_command=(
            "wget"
            " -c https://raw.githubusercontent.com/LinkedInLearning/hands-on-introduction-data-engineering-4395021/main/data/top-level-domain-names.csv"
            " -O /workspaces/study_airflow/data/top-level-domain-names.csv"
        ),
        dag=dag,
    )

    def transform_data():
        """Read in the file, and write a transformed file out"""
        today = date.today()

        df = pd.read_csv("/workspaces/study_airflow/data/top-level-domain-names.csv")
        generic_type_df = df[df['Type'] == 'generic']
        generic_type_df['Date'] = today.strftime('%Y-%m-%d')
        os.makedirs('/workspaces/study_airflow/data/orchestrated/', exist_ok=True)
        generic_type_df.to_csv('/workspaces/study_airflow/data/orchestrated/airflow-transform-data.csv', index=False)


    transform_task = PythonOperator(
      task_id='transform_task',
      python_callable=transform_data,
      dag=dag)

    create_path >> extract_task >> transform_task
