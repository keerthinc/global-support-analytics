# Automate_KPI_Calc

**Global Support KPI Automation using Snowflake & Python**

---

## Project Overview

**Automate_KPI_Calc** is an end-to-end Python analytics pipeline that automatically **extracts, calculates, validates, and monitors global support KPIs** from Snowflake data.

The project is designed to help **Support Operations, Analytics, and Leadership teams** track:

* SLA performance
* Backlog growth
* SLA risk cases
* Daily operational health
* Data quality reliability

All outputs are generated as **CSV and TXT files**, making the solution easy to integrate with **Tableau, Power BI, Airflow, or alerting systems**.

---

## Key Objectives

* Automate daily KPI calculations
* Detect SLA risks **before breaches occur**
* Identify sudden backlog spikes
* Produce executive-friendly daily summaries
* Measure data quality health
* Enable BI & reporting consumption

---

## Project Architecture

```
Snowflake (support_cases_mock)
        |
        v
Extract (SQLAlchemy)
        |
        v
Transform & KPI Calculations
        |
        v
Aggregations & Validation
        |
        v
Advanced Ops Automation
(SLA Risk | Backlog Spike | Data Quality)
        |
        v
output/ (CSV & TXT reports)
```

---

## Tech Stack

| Category            | Technology          |
| ------------------- | ------------------- |
| Language            | Python 3.9+         |
| Data Source         | Snowflake           |
| Data Access         | SQLAlchemy + pandas |
| Analytics           | pandas, numpy       |
| Config              | python-dotenv       |
| Output              | CSV, TXT            |
| Orchestration Ready | Airflow             |

---

## Project Structure

```
AUTOMATE_KPI_CALC/
├── dags/                     # Airflow DAGs (optional)
├── logs/                     # Pipeline logs
├── output/                   # Generated reports
├── venv/                     # Virtual environment (excluded from git)
├── .env                      # Environment variables (excluded)
├── .gitignore
├── .zipignore
├── backlog_spike_detection.py
├── config.py
├── daily_ops_summary.py
├── data_quality_score.py
├── extract.py
├── main.py
├── transform.py
├── validate.py
├── sla_risk_alert.py
├── requirements.txt
├── README.md
├── Steps.md
└── structure.md
```

---

## Configuration

### Environment Variables (`.env`)

Create a `.env` file in the root directory:

```env
SNOWFLAKE_USER=your_user
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_ACCOUNT=your_account
```

> Never commit `.env` to GitHub.

---

## Pipeline Flow (Step-by-Step)

### 1. Data Extraction (`extract.py`)

* Connects to Snowflake using SQLAlchemy
* Pulls last **30 days of support cases**
* Dynamically assigns SLA targets based on priority

---

### 2. Data Normalization (`main.py`)

* Converts all datetime columns to UTC
* Ensures consistent time calculations

---

### 3. KPI Transformation (`transform.py`)

* Calculates per-case KPIs
* Adds SLA metrics and operational indicators

---

### 4. Aggregations (`aggregate_metrics`)

Generates:

* `sla_summary.csv`
* `backlog_summary.csv`
* `volume_trend.csv`

---

### 5. Data Validation (`validate.py`)

* Ensures KPI integrity
* Logs inconsistencies without breaking the pipeline

---

### 6. SLA Risk Alert (`sla_risk_alert.py`)

* Identifies open cases nearing SLA breach (≥ 80%)
* Outputs `sla_at_risk_cases.csv`

---

### 7. Backlog Spike Detection (`backlog_spike_detection.py`)

* Compares today’s backlog to 7-day average
* Flags spikes above 20% growth
* Outputs `backlog_spike_summary.csv`

---

### 8. Daily Ops Summary (`daily_ops_summary.py`)

* Creates a human-readable daily summary
* Outputs:

  * `daily_ops_summary.txt`
  * `daily_ops_summary.csv`

---

### 9. Data Quality Scoring (`data_quality_score.py`)

* Measures missing data, duplicates, invalid SLA
* Produces a **Data Quality Score (0–100)**
* Outputs `data_quality_score.csv`

---

## Output Files

All results are saved to the `output/` directory.

| File                      | Description             |
| ------------------------- | ----------------------- |
| sla_summary.csv           | SLA performance         |
| backlog_summary.csv       | Open backlog snapshot   |
| volume_trend.csv          | Case volume trend       |
| sla_at_risk_cases.csv     | SLA-risk cases          |
| backlog_spike_summary.csv | Backlog spike detection |
| daily_ops_summary.csv     | Ops snapshot            |
| daily_ops_summary.txt     | Executive summary       |
| data_quality_score.csv    | Data health score       |

---

## How to Run the Project

### 1. Create & Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Pipeline

```bash
python main.py
```

---

## Logging

Pipeline logs are written to:

```
logs/global_support_pipeline.log
```

Includes:

* Execution status
* Row counts
* Alerts & warnings

---

## Deployment & Automation

* **Airflow Ready** – can be wrapped in a PythonOperator
* **BI Ready** – CSV outputs connect directly to Tableau / Power BI
* **Scalable** – Snowflake handles large datasets efficiently

---

## Future Enhancements

* Slack / Email alerting
* Historical anomaly detection
* Config-driven SLA thresholds
* Dockerization
* Incremental Snowflake loads

---

## Intended Audience

* Analytics Engineers
* Support Operations Teams
* Data Platform Engineers
* Business Stakeholders

---

## Key Takeaways

* Fully automated KPI pipeline
* Proactive operational intelligence
* Clean, modular, production-ready design
* Easy to extend and orchestrate

---