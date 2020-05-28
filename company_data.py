import requests
from bs4 import BeautifulSoup
import yahoo_fin.stock_info as si
import csv

#ticker_functions = [si.tickers_dow, si.tickers_nasdaq, si.tickers_sp500]
#ticker_functions = {"dow": si.tickers_dow, "sp500": si.tickers_sp500, "nasdaq": si.tickers_nasdaq}
ticker_functions = {"dow": si.tickers_dow, "sp500": si.tickers_sp500}
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
    filename= tf+".csv"
    with open(filename,  "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

with open('missed_tickers.txt', 'w') as filehandle:
    for tick in missed_tickers:
        filehandle.write('%s\n' % tick)