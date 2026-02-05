import numpy as np
import pandas as pd

def data_quality_score(df):
    checks = {
        "missing_case_id": df["case_id"].isna().mean(),
        "missing_created_at": df["created_at"].isna().mean(),
        "invalid_sla": (df["sla_target_hours"] <= 0).mean(),
        "duplicates": df["case_id"].duplicated().mean()
    }

    error_rate = sum(checks.values())
    score = max(0, 100 - (error_rate * 100))

    quality_report = {
        "Data_Quality_Score": round(score, 2),
        **{k: round(v * 100, 2) for k, v in checks.items()}
    }

    pd.DataFrame([quality_report]).to_csv(
        "output/data_quality_score.csv", index=False
    )

    print(f"DATA QUALITY SCORE: {score:.2f}%")

    return quality_report
