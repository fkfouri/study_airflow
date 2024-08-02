from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime

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

with DAG(
    dag_id="exo_02",
    description="Exo 02",
    schedule_interval=None,
    default_args=default_args,
    tags=["fabio"],
) as dag:

    # Tarefa para criar a tabela no PostgreSQL
    create_database = PostgresOperator(
        task_id='create_database',
        postgres_conn_id='study_postgres',
        sql="""
        CREATE DATABASE study;
        """
    )

    # # Tarefa para criar a tabela no PostgreSQL
    # create_table = PostgresOperator(
    #     task_id='create_table_in_postgres',
    #     postgres_conn_id='my_postgres_conn_id',
    #     sql="""
    #     CREATE TABLE IF NOT EXISTS minha_tabela (
    #         coluna1 INTEGER,
    #         coluna2 TEXT
    #     );
    #     """
    # )

    # # Tarefa para inserir dados na tabela
    # insert_data = PostgresOperator(
    #     task_id='insert_data_to_postgres',
    #     postgres_conn_id='my_postgres_conn_id',
    #     sql="""
    #     INSERT INTO minha_tabela (coluna1, coluna2) VALUES
    #     (1, 'a'),
    #     (2, 'b'),
    #     (3, 'c');
    #     """
    # )

    # # Defina a ordem das tarefas
    # create_database >> create_table >> insert_data