import numpy as np
import pandas as pd

def backlog_spike_detection(df, spike_threshold=0.2):
    df_open = df[df["resolved_at"].isna()].copy()
    df_open["date"] = df_open["created_at"].dt.date

    daily_backlog = (
        df_open.groupby("date")
        .size()
        .reset_index(name="open_cases")
        .sort_values("date")
    )

    if len(daily_backlog) < 8:
        return None

    today = daily_backlog.iloc[-1]["open_cases"]
    avg_7d = daily_backlog.iloc[-8:-1]["open_cases"].mean()

    growth_pct = (today - avg_7d) / avg_7d

    if growth_pct > spike_threshold:
        print(
            f"🚨 BACKLOG SPIKE: {growth_pct:.1%} increase vs 7-day average"
        )

    return {
        "today_backlog": today,
        "avg_7d_backlog": round(avg_7d, 2),
        "growth_pct": round(growth_pct * 100, 2)
    }
