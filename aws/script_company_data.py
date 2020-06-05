import requests
from io import StringIO
from bs4 import BeautifulSoup
from datetime import datetime
#import yahoo_fin.stock_info as si
from yahoo_fin.stock_info import tickers_dow, tickers_sp500
import csv
import boto3

bucketname = "stock-screener-relive"
now = datetime.now()
dt = now.strftime("%Y_%m_%d")


#ticker_functions = [si.tickers_dow, si.tickers_nasdaq, si.tickers_sp500]
#ticker_functions = {"dow": si.tickers_dow, "sp500": si.tickers_sp500, "nasdaq": si.tickers_nasdaq}
ticker_functions = {"dow": tickers_dow, "sp500": tickers_sp500}
missed_tickers = []
for tf in ticker_functions.keys():
    func = ticker_functions[tf]
    tickers = func()
    data = []
    for ticker in tickers:
        try:
            print(ticker)
            company_prof = [ticker]
            url = "https://finance.yahoo.com/quote/{}/profile".format(ticker)
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            company_prof.append(soup.find('h3', class_='Fz(m) Mb(10px)').get_text())
            company_prof.append(soup.find_all('span', class_='Fw(600)')[0].get_text())
            company_prof.append(soup.find_all('span', class_='Fw(600)')[1].get_text())
            company_prof.append(soup.find_all('a', target="_blank")[0].get_text())
            data.append(company_prof)
            print(company_prof)
        except:
            missed_tickers.append(ticker)
            pass
    filename= tf+"_"+dt+".csv"
    csv_buffer = StringIO()
    writer = csv.writer(csv_buffer, delimiter=",")
    writer.writerows(data)
    s3 = boto3.client('s3')
    s3.upload_fileobj(csv_buffer.getvalue(), "stock-screener-relive", "data/"+filename)