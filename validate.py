# I validate support data by checking key identifiers for completeness and 
# enforcing sanity checks on KPIs like SLA percentage. 
#If validation fails, the pipeline stops so incorrect metrics never reach dashboards.
def validate_data(df, sla_summary):
    assert df["case_id"].notnull().all(), "Missing case IDs"
    assert sla_summary["sla_pct"].between(0, 100).all(), "Invalid SLA values"
