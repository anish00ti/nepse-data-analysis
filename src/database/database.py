import sqlite3
import pandas as pd
from config.config import DATABASE_PATH

def save_dataframe(df: pd.DataFrame, table_name="daily_prices"):
    with sqlite3.connect(DATABASE_PATH) as conn:
        df.to_sql(table_name, conn, if_exists="append", index=False)

def read_table(table_name="daily_prices"):
    with sqlite3.connect(DATABASE_PATH) as conn:
        return pd.read_sql(f"SELECT * FROM {table_name}", conn)
