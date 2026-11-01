import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:123@host.docker.internal:5432/retail_db",
    connect_args={"options": "-csearch_path=raw"}
)

csv_path = "/opt/airflow/data/raw/walmart.csv"
df = pd.read_csv(csv_path)

# normalize headers
df.columns = df.columns.str.strip().str.lower()

df.to_sql(
    "walmart_sales",
    engine,
    if_exists="append",
    index=False,
    method="multi"
)

print(f"Successfully loaded {len(df)} rows.")