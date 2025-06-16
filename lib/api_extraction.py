import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# tickers = ['SPY', "BND", "GLD", "VTI", "QQQ"]
tickers = ['INTC']

end_date = datetime.today()
print(end_date)

start_date = end_date - timedelta(days=40*365)

close_df = pd.DataFrame()

for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date)
    close_df[ticker] = data['Close']

print(close_df.reset_index())
