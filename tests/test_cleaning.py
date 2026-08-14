import pandas as pd
from src.cleaning.data_cleaner import clean_market_data

def test_cleaning():
    df = pd.DataFrame({"close": [100, 100]})
    result = clean_market_data(df)
    assert len(result) == 1
