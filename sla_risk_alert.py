import pandas as pd
from datetime import datetime

def sla_risk_alert(df, threshold=0.8):
    now = pd.Timestamp.now(tz="UTC")

    df_open = df[df["resolved_at"].isna()].copy()

    df_open["elapsed_hours"] = (
        now - df_open["created_at"]
    ).dt.total_seconds() / 3600

    at_risk = df_open[
        df_open["elapsed_hours"] >= df_open["sla_target_hours"] * threshold
    ]

    if not at_risk.empty:
        at_risk.to_csv("output/sla_at_risk_cases.csv", index=False)
        print(f"⚠️ SLA RISK ALERT: {len(at_risk)} cases nearing SLA breach")

    return at_risk
