# run airflow locally
# pip3 install apache-airflow
# airflow db init
# airflow webserver -p 8080
# airflow scheduler
# open http://localhost:8080
# This Airflow DAG runs a daily Global Support KPI pipeline. 
# It orchestrates the execution of a Python-based automation that extracts data from Snowflake, 
# calculates KPIs like SLA, backlog, and MTTR, validates data quality, and produces outputs for Tableau dashboards. 
# Airflow handles scheduling, retries, and monitoring.
# Can this be more granular?”, say:

# Yes, the pipeline can be broken into extract, transform, validate, and load tasks using separate PythonOperators, 
# but for analytics workflows this single-task orchestration is often sufficient and easier to maintain.

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# -------------------------------------------------
# Absolute path to your project
# -------------------------------------------------
PROJECT_PATH = "/Users/keerthinc/saviynt/Automate_the_kpi_calc"
sys.path.insert(0, PROJECT_PATH)

from main import run_pipeline

# -------------------------------------------------
# Default arguments
# -------------------------------------------------
default_args = {
    "owner": "keerthi",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

# -------------------------------------------------
# DAG definition
# -------------------------------------------------
with DAG(
    dag_id="global_support_kpi_daily_pipeline",
    description="Daily Global Support KPI automation using Snowflake",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval="0 6 * * *",  # Daily at 6 AM
    catchup=False,
    tags=["global-support", "snowflake", "kpi"],
) as dag:

    run_global_support_pipeline = PythonOperator(
        task_id="run_global_support_pipeline",
        python_callable=run_pipeline,
    )

    run_global_support_pipeline
