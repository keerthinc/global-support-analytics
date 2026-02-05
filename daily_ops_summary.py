import numpy as np
import pandas as pd
from datetime import datetime


def daily_ops_summary(df, at_risk_cases):
    closed = df[df["resolved_at"].notna()].copy()

    sla_pct = (
        (closed["resolved_at"] - closed["created_at"])
        .dt.total_seconds()
        / 3600
        <= closed["sla_target_hours"]
    ).mean() * 100

    backlog_count = df[df["resolved_at"].isna()].shape[0]
    risk_count = len(at_risk_cases)

    summary = f"""
        DAILY GLOBAL SUPPORT SUMMARY
        Date: {datetime.utcnow().date()}

        SLA Adherence: {sla_pct:.2f}%
        Open Backlog: {backlog_count}
        SLA-At-Risk Cases: {risk_count}

        Action: Review at-risk cases and backlog growth.
        """

    with open("output/daily_ops_summary.txt", "w") as f:
        f.write(summary)

    print(summary)
    return summary
