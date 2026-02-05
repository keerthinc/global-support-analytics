import pandas as pd
from sqlalchemy import create_engine
from config import SNOWFLAKE_CONFIG

def extract_support_cases():
    engine = create_engine(
        f"snowflake://{SNOWFLAKE_CONFIG['user']}:{SNOWFLAKE_CONFIG['password']}@"
        f"{SNOWFLAKE_CONFIG['account']}/{SNOWFLAKE_CONFIG['database']}/"
        f"{SNOWFLAKE_CONFIG['schema']}?warehouse={SNOWFLAKE_CONFIG['warehouse']}"
    )
    
    query = f"""
        SELECT *,   CASE
        WHEN priority = 'P1' THEN 24
        WHEN priority = 'P2' THEN 72
        WHEN priority = 'P3' THEN 168
        ELSE 336
        END AS sla_target_hours
        FROM support_cases_mock
        WHERE created_at >= DATEADD(year, -30, CURRENT_DATE) 
        limit 100000; 
    """ 
    df = pd.read_sql(query, engine)
    return df
