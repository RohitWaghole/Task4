from datetime import datetime, timedelta
from airflow.decorators import dag, task


default_args = {
    'owner':'rohit',
    'retries':2,
    'retry_delay':timedelta(minutes=5)
}

@dag(dag_id='dag_with_date_commands',
     default_args=default_args,
     start_date=datetime(2023,4,11),
     schedule_interval='*/5 * * * *')
def date_command():

    @task()
    def get_date_and_time():
        print(f"Welcome to the Airflow, the current date and time is {datetime.now()}")

    @task()
    def success():
        print("Dag executed succesfully")

    get_date_and_time()
    success()
    

date_dag = date_command()