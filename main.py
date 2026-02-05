import logging
import pandas as pd
import numpy as np
from extract import extract_support_cases
from transform import calculate_kpis, aggregate_metrics
from validate import validate_data
from sla_risk_alert import sla_risk_alert
from backlog_spike_detection import backlog_spike_detection
from daily_ops_summary import daily_ops_summary
from data_quality_score import data_quality_score


logging.basicConfig(
    filename="logs/global_support_pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def normalize_datetimes(df):
    datetime_cols = [
        "created_at",
        "first_response_at",
        "resolved_at"
    ]

    for col in datetime_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], utc=True)

    return df


def run_pipeline():
    logging.info("Pipeline started")

    # 1  Extract
    df = extract_support_cases()
    logging.info(f"Extracted {len(df)} rows")

    df = normalize_datetimes(df)

    # 2 Transform
    df = calculate_kpis(df)
    print("KPIs are Calculated")

    # 3️ Aggregate (existing KPI outputs)
    sla_summary, backlog, volume_trend = aggregate_metrics(df)

    sla_summary.to_csv("output/sla_summary.csv", index=False)
    backlog.to_csv("output/backlog_summary.csv", index=False)
    volume_trend.to_csv("output/volume_trend.csv", index=False)
    print("sla_summary, backlog_summary, volume_trend csv files are created in output folder")

    # 4️ Validate
    validate_data(df, sla_summary)
    print("Validation Completed")

    # # Advanced Ops Automation 
    outputs = {}

    # 6 SLA Risk Cases
    at_risk = sla_risk_alert(df)
    if at_risk is not None and not at_risk.empty:
        path = "output/sla_at_risk_cases.csv"
        at_risk.to_csv(path, index=False)
        outputs["sla_risk_cases"] = path
        print("csv is created for SLA Risk Cases")
    else:
        outputs["sla_risk_cases"] = None
        print("csv is not created as not SLA Risk Cases")

    # 7 Backlog Spike Detection
    backlog_info = backlog_spike_detection(df)
    if backlog_info:
        backlog_df = pd.DataFrame([backlog_info])
        path = "output/backlog_spike_summary.csv"
        backlog_df.to_csv(path, index=False)
        outputs["backlog_spike"] = path
        print("csv is created for Backlog Spike Detection")
    else:
        outputs["backlog_spike"] = None
        print("csv is not created as Backlog Spike not Detection")

    # 8 Daily Ops Summary (Text → CSV)
    summary_text = daily_ops_summary(df, at_risk)
    summary_df = pd.DataFrame(
        {"summary": summary_text.split("\n")}
    )
    path = "output/daily_ops_summary.csv"
    summary_df.to_csv(path, index=False)
    outputs["ops_summary"] = path
    print("csv is created for Daily Ops Summary")
    
    # 9 Data Quality Score
    quality = data_quality_score(df)
    quality_df = pd.DataFrame([quality])
    path = "output/data_quality_score.csv"
    quality_df.to_csv(path, index=False)
    outputs["data_quality"] = path
    print("csv is created for Data Quality Score")

    logging.info(f"Advanced ops outputs generated: {outputs}")

    logging.info("Pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()
