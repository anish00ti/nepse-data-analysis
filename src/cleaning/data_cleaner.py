import pandas as pd

def clean_market_data(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result = result.drop_duplicates()
    return result
