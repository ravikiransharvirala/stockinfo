import yahoo_fin.stock_info as si
import pandas as pd

def get_company_quote(ticker):
    ticker = ticker.lower()
    return si.get_quote_table(ticker)

print(get_company_quote('aapl'))