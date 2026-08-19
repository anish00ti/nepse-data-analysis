from snowflake.connector.pandas_tools import write_pandas


def upload_market_summary(conn, df):

    success, nchunks, nrows, output = write_pandas(
        conn=conn,
        df=df,
        database="NEPSE_DB",
        schema="NEPSE_SCHEMA",
        table_name="MARKET_SUMMARY",
        auto_create_table=False,
        overwrite=False
    )

    return success, nrows