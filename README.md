# Global Support Analytics Automation

This project automates Global Support KPI analysis using Python and Snowflake.

## KPIs Covered
- SLA Adherence
- First Response Time (FRT)
- Mean Time to Resolution (MTTR)
- Backlog & Aging Buckets
- Case Volume Trends

## Tech Stack
- Python (pandas, numpy)
- Snowflake
- SQLAlchemy
- Tableau (for visualization)

## How It Works
1. Extracts support data from Snowflake
2. Calculates KPIs
3. Validates data quality
4. Outputs aggregated datasets for Tableau
5. Runs daily via scheduler

## How to Run
```bash
pip install -r requirements.txt
python main.py
