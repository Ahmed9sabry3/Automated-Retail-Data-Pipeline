from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

INGESTION_PATH = "/opt/airflow/ingestion/ingestion.py"
DBT_DIR = "/opt/airflow/dbt_project"

with DAG(
    dag_id="etl_pipeline",
    start_date=datetime(2026, 5, 1),
    schedule="@daily",
    catchup=False
) as dag:

    ingestion = BashOperator(
        task_id="ingestion",
        bash_command=f"python {INGESTION_PATH}"
    )

    dbt_deps = BashOperator(
        task_id="dbt_deps",
        bash_command=f"cd {DBT_DIR} && dbt deps"
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"cd {DBT_DIR} && dbt run"
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"cd {DBT_DIR} && dbt test"
    )

    ingestion >> dbt_deps >> dbt_run >> dbt_test