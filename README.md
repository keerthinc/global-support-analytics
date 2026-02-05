# Global Support Analytics Automation

## Overview
This project automates **Global Support KPI analysis** using **Python, Snowflake, and Airflow**, and prepares analytics-ready outputs for **Tableau dashboards**.  
It is designed to support **operational efficiency, SLA monitoring, and proactive risk detection** in a global customer support environment.

The pipeline runs **daily**, calculates key support metrics, validates data quality, and publishes curated datasets for reporting and decision-making.

---

## Business Context
Global Support teams operate across regions and time zones and are measured on **speed, quality, and reliability**.  
This automation helps answer questions like:
- Are we meeting SLA commitments?
- Where is backlog building up?
- Which regions or priorities are at risk?
- How can we detect issues before SLA breaches occur?

---

## KPIs Covered
- **SLA Adherence (%)**
- **First Response Time (FRT)**
- **Mean Time to Resolution (MTTR)**
- **Backlog (Open Cases)**
- **Aging Buckets (0–24h, 24–72h, >72h)**
- **Case Volume Trends**
- **Operational Risk Indicators**

---

## Tech Stack
- **Python** (pandas, numpy)
- **Snowflake** (cloud data warehouse)
- **SQLAlchemy** (database connectivity)
- **Airflow** (workflow orchestration)
- **Tableau** (visualization & dashboards)
- **GitHub** (version control)

---

## Project Architecture
