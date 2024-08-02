from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime
import pandas as pd
from os import getenv
from sqlalchemy import create_engine

# Defina o DAG
default_args = {
    "owner": "Fabio",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "catchup": False,
    "start_date": datetime(2023, 1, 1),
}

def save_dataframe_to_postgres():
    # Dados de exemplo
    df = pd.read_csv(
        "/workspaces/study_airflow/data/orchestrated/airflow-transform-data.csv"
    )

    # Conectar ao PostgreSQL
    engine = create_engine(
        f"postgresql+psycopg2://{getenv('POSTGRES_USER')}:{getenv('POSTGRES_PASSWORD')}@{getenv('POSTGRES_HOST')}:{getenv('POSTGRES_PORT')}/study"
    )

    # Salvar o DataFrame na tabela 'minha_tabela'
    df.to_sql("minha_tabela", engine, if_exists="replace", index=False)

    print("Dados salvos com sucesso no PostgreSQL!")

with DAG(
    dag_id="exo_02",
    description="Exo 02",
    schedule_interval=None,
    default_args=default_args,
    tags=["fabio"],
) as dag:

    # Tarefa para criar a tabela no PostgreSQL
    create_table = PostgresOperator(
        task_id='create_table_in_postgres',
        postgres_conn_id='study_postgres',
        sql="""
        CREATE TABLE IF NOT EXISTS example (
            coluna1 INTEGER,
            coluna2 TEXT
        );
        """
    )

    save_data_task = PythonOperator(
        task_id="save_data_to_postgres", python_callable=save_dataframe_to_postgres
    )

    create_table >> save_data_task


