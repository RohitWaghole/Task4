from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

from datetime import datetime

default_args = {
    'owner':'rohit',
    'retries':2,
    'retry_dely':timedelta(minutes=2)
}

def _downloading():
    print('trigger dag executed')

with DAG(
    dag_id='trigger_dag', 
    description='this is a trigger dag',
    start_date=datetime(2023,4,11),
    schedule_interval='@daily', 
    default_args=default_args, 
    catchup=False) as dag:

    downloading = PythonOperator(
        task_id='downloading',
        python_callable=_downloading
    )

    trigger_target = TriggerDagRunOperator(
        task_id='trigger_target',
        trigger_dag_id='target_dag'
    )