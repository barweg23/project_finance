from lib.api_extraction import downlaod_stock

from datetime import datetime, timedelta


tickers = ['INTC']
end_date = datetime.today()
start_date = end_date - timedelta(days=40*365)


print(downlaod_stock(tickers[0], start_date, end_date))
