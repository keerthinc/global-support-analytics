import logging
from extract import extract_support_cases
from transform import calculate_kpis, aggregate_metrics
from validate import validate_data

logging.basicConfig(
    filename = "logs/global_support_pipeline.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():
    logging.info("Pipeline started")

    df = extract_support_cases()
    logging.info("fExtracted{len(df)} rows")

    df = calculate_kpis(df)

    sla_summary, backlog, volume_trend = aggregate_metrics(df)

    #Test missing case IDs
    #df.loc[0, "case_id"] = None

    #Test invalid SLA values
    #sla_summary.loc[0, "sla_pct"] = 150
    try:
        validate_data(df, sla_summary)
        print("Validation passed")
    except AssertionError as e:
        logging.error(f"Data validation failed: {e}")
        raise

    
    sla_summary.to_csv("output/sla_summary.csv", index = False)
    backlog.to_csv("output/backlog_summary.csv", index = False)
    volume_trend.to_csv("output/volume_trend.csv", index = False)

    logging.info("Pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()