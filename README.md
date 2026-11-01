Walmart Retail ELT Pipeline 
<img width="1536" height="1024" alt="ChatGPT Image May 22, 2026, 02_51_53 PM" src="https://github.com/user-attachments/assets/c0bde29b-7f94-4fa8-9372-4cd040cdd6ae" />

📌 Project Overview

This project is an End-to-End ELT Data Engineering Pipeline built using:

Apache Airflow
dbt (Data Build Tool)
PostgreSQL
Docker
Python
Pandas
SQLAlchemy

The pipeline ingests Walmart retail sales data from CSV files into PostgreSQL, 
transforms the data using dbt following a Medallion Architecture (Raw/bronze → Silver → Gold), and orchestrates the workflow using Airflow.

🏗️ Architecture
                +------------------+
                |   Walmart CSV    |
                +------------------+
                          |
                          v
                +------------------+
                | Python Ingestion |
                | Pandas + SQLA    |
                +------------------+
                          |
                          v
                +------------------+
                | PostgreSQL RAW   |
                | schema: raw      |
                +------------------+
                          |
                          v
                +------------------+
                | dbt Staging      |
                | schema: silver   |
                +------------------+
                          |
                          v
                +------------------+
                | dbt Marts        |
                | schema: gold     |
                +------------------+
                          |
                          v
                +------------------+
                | Analytics / BI   |
                +------------------+

                Orchestrated by Airflow
                
⚙️ Tech Stack

Technology	Purpose
Python	Data ingestion
Pandas	CSV processing
PostgreSQL	Data warehouse
dbt	Data transformation
Airflow	Workflow orchestration
Docker	Containerization
SQLAlchemy	Database connection
Docker Compose	Multi-container orchestration 

📂 Project Structure
project/
│
├── airflow/
│   ├── dags/
│   │   └── retail_dag.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── docker-compose.yml
│
├── ingestion/
│   └── ingestion.py
│
├── dbt_project/
│   ├── models/
│   │   ├── staging/
│   │   │   └── stg_walmart.sql
│   │   └── marts/
│   │       └── fact_sales.sql
│   │
│   ├── macros/
│   │   └── generate_schema_name.sql
│   │
│   ├── dbt_project.yml
│   └── profiles.yml
│
├── data/
│   └── raw/
│       └── walmart.csv
│
└── README.md

🔄 Pipeline Workflow
The Airflow DAG orchestrates the following tasks:

1️⃣ Ingestion
Reads Walmart CSV dataset
Normalizes column names
Loads data into PostgreSQL raw.walmart_sales
2️⃣ dbt deps
Installs dbt packages and dependencies
3️⃣ dbt run
Executes staging and mart transformations
4️⃣ dbt test
Runs data quality checks


🧱 Medallion Architecture

🥉 Raw Layer
Schema: raw

Contains:

Raw ingested Walmart data
No transformations

🥈 Silver Layer

Schema: silver

Contains:

Cleaned and standardized data
Renamed columns
Data type normalization
Business rule filtering

Example:

WHERE weekly_sales > 0
🥇 Gold Layer

Schema: gold

Contains:

Business-ready analytical models
Fact tables
KPI-ready datasets

📌 Example dbt Staging Model
SELECT
    store AS store_id,
    date AS sales_date,
    weekly_sales,
    CASE WHEN holiday_flag = 1 THEN TRUE ELSE FALSE END AS is_holiday,
    temperature AS temperature_f,
    fuel_price,
    cpi,
    unemployment AS unemployment_rate
FROM {{ source('raw', 'walmart_sales') }}
WHERE weekly_sales > 0

📌 Example dbt Mart Model
SELECT *
FROM {{ ref('stg_walmart') }}

🛠️ Dockerization

The project is fully containerized using Docker.

Containers include:

Airflow Webserver
Airflow Scheduler
PostgreSQL
Redis
Airflow Worker
Airflow Triggerer

Benefits:

Environment consistency
Easy deployment
Dependency isolation
Simplified setup

🚀 How to Run
Start Containers
docker compose up --build
Access Airflow
http://localhost:8080

Default credentials:

username: airflow
password: airflow

🧪 dbt Commands
Run Models
dbt run
Run Tests
dbt test
Generate Documentation
dbt docs generate
dbt docs serve

📊 Key Features

✅ End-to-End ELT Pipeline
✅ Automated Workflow Orchestration
✅ dbt Transformations
✅ Medallion Architecture
✅ PostgreSQL Data Warehouse
✅ Dockerized Environment
✅ Data Quality Testing
✅ Modular Project Structure
✅ Scalable Design






