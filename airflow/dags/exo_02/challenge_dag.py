''' Challenge'''
from datetime import datetime, date
import pandas as pd
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow import DAG
from sqlalchemy import create_engine
from os import getenv

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
    dag_id='challenge_dag',
    schedule=None,
    start_date=datetime(2023, 1, 1),
    default_args=default_args,
    catchup=False,
    tags=["fabio"]) as dag:

    create_path = BashOperator(
        task_id="create_path",
        bash_command="mkdir -p /workspaces/study_airflow/data/challenge",
        dag=dag,
    )

    extract_task = BashOperator(
        task_id='extract_task',
        bash_command=(
            "wget"
            " -c https://raw.githubusercontent.com/LinkedInLearning/hands-on-introduction-data-engineering-4395021/03-11e/data/constituents.csv"
            " -O /workspaces/study_airflow/data/challenge/challenge-extract-data.csv"
        ),        
        )

    def transform_data():
        """Read in the file, and write a transformed file out"""
        today = date.today()
        df = pd.read_csv('/workspaces/study_airflow/data/challenge/challenge-extract-data.csv')
        count_df = df.groupby(["Sector"])["Sector"].count().reset_index(name="count")
        count_df['Date'] = today.strftime('%Y-%m-%d')
        count_df.to_csv('/workspaces/study_airflow/data/challenge/challenge-transform-data.csv', index=False)

    transform_task = PythonOperator(
        task_id='transform_task',
        python_callable=transform_data,
        dag=dag)

    def save_dataframe_to_postgres():
        df = pd.read_csv(
            '/workspaces/study_airflow/data/challenge/challenge-transform-data.csv'
        )
        engine = create_engine(
            f"postgresql+psycopg2://{getenv('POSTGRES_USER')}:{getenv('POSTGRES_PASSWORD')}@{getenv('POSTGRES_HOST')}:{getenv('POSTGRES_PORT')}/study"
        )
        df.to_sql("challenge", engine, if_exists="replace", index=False)
        print("Dados salvos com sucesso no PostgreSQL!")

    load_task = PythonOperator(
        task_id='load_task',
        python_callable=save_dataframe_to_postgres,
        dag=dag)

    create_path >> extract_task >> transform_task >> load_task

