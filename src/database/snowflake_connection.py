import os
from dotenv import load_dotenv
import snowflake.connector

load_dotenv()


def get_snowflake_connection():

    conn = snowflake.connector.connect(
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database="NEPSE_DB",
        schema="NEPSE_SCHEMA"
    )

    return conn