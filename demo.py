import yahoo_fin.stock_info as si
import pandas as pd
from datetime import datetime
import numpy as np
from decimal import Decimal


def get_company_quote(ticker):
    """
    This method is used to retrieve the data from the yahoo summary page of stock
    """
    ticker = ticker.lower()
    return si.get_quote_table(ticker)


def get_p_e_ratio(ticker):
    """
    Price to earning ratio is the ratio of valuing the company that measures it's
    current share price relative to it's per-share earning. A high p/e ratio indicates
    that the stock is over valued.

    P/E ratio = market value per share/ earning per share
    """
    date = datetime.now()
    date = date.strftime("%d/%m/%Y")
    quote = si.get_quote_table(ticker)
    return {'date': date, 'p/e ratio': quote['PE Ratio (TTM)']}

def pe_ratio(ticker):
    """
    P/E (Price to Earnings Ratio) – This equals the company share price divided 
    by its earnings per share. This tells us how expensive the stock is relative to its earnings (profits).
    """
    return float(si.get_stats_valuation(ticker).iloc[2,1])

def pb_ratio(ticker):
    """
    """
    return float(si.get_stats_valuation(ticker).iloc[6,1])

def peg_ratio(ticker):
    """
    This ratio is calculated by dividing the PE ratio with the growth 
    rate of earnings per share. This measure goes beyond what the PE ratio suggests by 
    factoring in the future earnings growth potential of the stock. This way we can evaluate if a 
    certain PE multiple of a stock is overvalued or undervalued when considering the growth of its future earnings.
    """
    return float(si.get_stats_valuation(ticker).iloc[4,1])

def text_to_num(text):
    d = {'M': 3,'B': 6,'T': 9}
    if text[-1] in d:
        num, magnitude = text[:-1], text[-1]
        return float(Decimal(num) * 10 ** d[magnitude])
    else:
        return float(text)


def pfcf_ratio(ticker):
    """
    This equals the share price divided by the cashflow per share or the free cash flow per share. 
    This measures how expensive the stock is relative to the cashflow it generates from its operations.
    """
    market_cap = text_to_num(str(si.get_stats_valuation(ticker).iloc[0,1]))
    cashflow_table = si.get_cash_flow(ticker)
    cashflow_table.set_index('Breakdown', inplace=True)
    free_cash_flow  = cashflow_table.loc['Free Cash Flow'][0]
    if free_cash_flow == '-':
        free_cash_flow = cashflow_table.loc['Free Cash Flow'][1]
        if free_cash_flow == '-':
            free_cash_flow = np.nan 
        else: 
            free_cash_flow = float(free_cash_flow)
    else:
        free_cash_flow = float(free_cash_flow) 
    return market_cap/free_cash_flow

def gross_margin(ticker):
    """
    This is calculated by dividing the stock’s gross profit by its total revenue. 
    This gives us the profit potential of a business before factoring in the 
    indirect expenses associated with its operations
    """
    return (text_to_num(str(si.get_stats(ticker).iloc[46,1]))/text_to_num(str(si.get_stats(ticker).iloc[43,1])))*100

def return_on_assets(ticker):
    """
    This ratio is calculated by dividing the net income with the total assets of the company. 
    This gives us an estimate of how much return the company generates relative to the total 
    amount invested in the business (which is reflected in total assets).
    """
    roa = si.get_stats(ticker).iloc[41, 1]
    if str(roa) == 'nan':
        roa = np.nan
    else:
        roa = float(roa[:-1])
    return roa




print(pfcf_ratio('AAPL'))