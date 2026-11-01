FROM apache/airflow:2.9.0

USER root
RUN apt-get update && apt-get install -y gcc g++ build-essential

USER airflow

RUN pip install --no-cache-dir \
    dbt-core==1.7.14 \
    dbt-postgres==1.7.14 \
    papermill \
    nbformat \
    pandas \
    sqlalchemy \
    psycopg2-binary \
    fastparquet