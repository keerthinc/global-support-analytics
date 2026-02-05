import pandas as pd
import numpy as np

def calculate_kpis(df):
    #convert columns to datetime 
    df["created_at"] = pd.to_datetime(df["created_at"])
    df["resolved_at"] = pd.to_datetime(df["resolved_at"], errors = "coerce")
    df["first_response_at"] = pd.to_datetime(df["first_response_at"], errors ="coerce")

    now = pd.Timestamp.utcnow()
    df["resolution_hours"] = (
        df["resolved_at"].fillna(now) - df["created_at"]
    ).dt.total_seconds() / 3600

    df["first_response_hours"] = (
        df["first_response_at"] - df["created_at"]
    ).dt.total_seconds() / 3600

    df["sla_met"] = np.where(
        df["resolution_hours"] <= df["sla_target_hours"], 1, 0
    )

    df["aging_bucket"] = pd.cut(
        df["resolution_hours"],
        bins = [0, 24, 72, 10000],
        labels = ["0-24h", "24-72h", ">72h"]
    )
    return df

def aggregate_metrics(df):
    sla_summary = (
        df[df["resolved_at"].notna()]
        .groupby(["priority", "region"], observed = True)
        .agg(
            sla_pct= ("sla_met", "mean"),
            mttr_hours = ("resolution_hours", "mean"),
            case_count = ("case_id", "count")
        )
        .reset_index()
    )

    sla_summary["sla_pct"] = sla_summary["sla_pct"] * 100

    backlog = (
        df[df["resolved_at"].isna()]
        .groupby(["region", "priority", "aging_bucket"], observed = True)
        .size()
        .reset_index(name="open_cases")
    )

    volume_trend = (
        df.groupby(df["created_at"].dt.date, observed = True)
        .size()
        .reset_index(name = "cases_created")
    )
    return sla_summary, backlog, volume_trend