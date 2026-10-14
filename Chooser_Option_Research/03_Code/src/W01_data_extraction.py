import os
import requests
import pandas as pd
import yfinance as yf
from dotenv import load_dotenv

load_dotenv()


# Yahoo Finance
def stock_data(ticker, start_date, end_date):
    stock = yf.Ticker(ticker)
    data = stock.history(
        start=start_date,
        end=end_date,
        auto_adjust=False,
        actions=True
    )
    return data


# FRED
def fred_data(series_id, start_date, end_date):
    url = "https://api.stlouisfed.org/fred/series/observations"

    params = {
        "series_id": series_id,
        "api_key": os.getenv("FRED_API_KEY"),
        "file_type": "json",
        "observation_start": start_date,
        "observation_end": end_date
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    data = pd.DataFrame(response.json()["observations"])

    return data