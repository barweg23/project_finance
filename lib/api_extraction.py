import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def downlaod_stock(ticker, start, end):
    return yf.download(ticker, start=start, end=end)

