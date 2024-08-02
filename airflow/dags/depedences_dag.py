from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

# Definir os argumentos padrão do DAG
default_args = {
    "owner": "Fabio",
    "start_date": datetime(2023, 1, 1),
    "retries": 1,
}

# Definir o DAG
with DAG(
    dag_id="dependences",
    default_args=default_args,
    description="Exemplo de DAG com tasks paralelas",
    schedule_interval="*/10 * * * *",  # Rodar a cada 10 minutos
    catchup=False,
    tags=["fabio"],
) as dag:

    # Definir as tasks
    task_1 = EmptyOperator(
        task_id="task_1",
    )

    task_2 = EmptyOperator(
        task_id="task_2",
    )

    task_3 = EmptyOperator(
        task_id="task_3",
    )

    task_4 = EmptyOperator(
        task_id="task_4",
    )

    task_5 = EmptyOperator(
        task_id="task_5",
    )

    task_6 = EmptyOperator(
        task_id="task_6",
    )

    task_7 = EmptyOperator(
        task_id="task_7",
    )  

    task_8 = EmptyOperator(
        task_id="task_8",
    )            
    # Definir dependências
    task_1 >> [[task_2, task_3] >> task_4], [task_4 and task_5 >> task_6] >> task_7 >> task_8
