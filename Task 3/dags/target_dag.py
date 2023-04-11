from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from datetime import datetime

default_args = {
    'owner':'rohit',
    'retries':2,
    'retry_dely':timedelta(minutes=2)
}

def _cleaning():
    print('Clearning from target DAG')


with DAG(
    dag_id='target_dag', 
    description='this is a target dag',
    start_date=datetime(2023,4,11),
    schedule_interval='@daily', 
    default_args=default_args, 
    catchup=False) as dag:

    storing = BashOperator(
        task_id='storing',
        bash_command='sleep 1'
    )

    cleaning = PythonOperator(
        task_id='cleaning',
        python_callable=_cleaning
    )

    storing >> cleaning