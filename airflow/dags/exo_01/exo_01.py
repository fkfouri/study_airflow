'''One Task DAG'''
from datetime import datetime
from airflow.operators.bash import BashOperator 
from airflow import DAG

default_args = {
        'owner': 'Fabio',
        'depends_on_past': False,
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 0,
        'catchup': False,
        'start_date': datetime(2023, 1, 1)
}

with DAG(
        dag_id='exo_01',
        description='Exo 01',
        schedule_interval=None,
        default_args=default_args,
        tags=['fabio']
    ) as dag:

    t00 = BashOperator(
            task_id='create path',
            bash_command='mkdir -p /workspaces/study_airflow/data',
            dag=dag)
    
    t10 = BashOperator(
            task_id='extract_task',
            bash_command='wget -c https://raw.githubusercontent.com/LinkedInLearning/hands-on-introduction-data-engineering-4395021/main/data/top-level-domain-names.csv' /
                         '-O /workspaces/study_airflow/data/top-level-domain-names.csv',
            dag=dag)
    
    t00 >> t10