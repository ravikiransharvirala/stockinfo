# StockInfo
Exploring stock market data using python with Yahoo finance package

## Fundamental Metrics for Screening Stocks

There are **five major categories** of metrics used while fundamentally picking stocks. They are:

**Valuation** – These metrics help us gauge whether a stock is overpriced or underpriced. Also helps us understand the market expectations for a stock.

**Profitability** – These metrics help us review a company’s profitability margins and its ability to bring in greater returns for the amount invested.

**Solvency** - This shows us a company’s debt profile. The greater the debt the harder it is for a company to meet its debt payments during economic downturns. Solvency focuses on the company’s ability to survive over the longer term. 

**Liquidity** – These metrics help us assess a company’s ability to meet short term payment obligations. This provides a clearer picture as to whether a company will need to further finance their operations (borrow more money) to meet their expenses. 

**Growth** – This shows the company’s growth profile. That is, how it has grown historically, with respect to sales, profits, and cash flows. 

#### Valuation Metrics

1.	**P/E (Price to Earnings Ratio)** – This equals the company share price divided by its earnings per share. This tells us how expensive the stock is relative to its earnings (profits).
2.	**P/S (Price to Sales Ratio)** – This is measured as the company share price divided by its sales per share (revenue per share). This shows how expensive the stock is relative to its sales. 
3.	**P/CF or P/FCF (Price to Cash Flow or Price to Free Cash Flow)** – This equals the share price divided by the cashflow per share or the free cash flow per share. This measures how expensive the stock is relative to the cashflow it generates from its operations. 
4.	**PEG (Price to earnings to growth ratio)** – This ratio is calculated by dividing the PE ratio with the growth rate of earnings per share. This measure goes beyond what the PE ratio suggests by factoring in the future earnings growth potential of the stock. This way we can evaluate if a certain PE multiple of a stock is overvalued or undervalued when considering the growth of its future earnings.

#### Profitability Metrics

1.	**Gross Margin** – This is calculated by dividing the stock’s gross profit by its total revenue. This gives us the profit potential of a business before factoring in the indirect expenses associated with its operations.
2.	**Net Margin** – This is calculated by dividing the stock’s net profits/income by its total revenue. This gives us the total profit potential of the business after accounting for all the related expenses.
3.	**Return on Assets (ROA)** – This ratio is calculated by dividing the net income with the total assets of the company. This gives us an estimate of how much return the company generates relative to the total amount invested in the business (which is reflected in total assets).
4.	**Return on Equity (ROE)** – This ratio is calculated by dividing the net income with the total equity of the company. This suggests how much return the stock generates for every dollar of equity invested in the company. This ratio also hints on how leveraged (debt levels) the company is. A very high ROE indicates that there is a huge amount of debt involved in financing the businesses operations. Although it needs to be verified using the solvency ratios to find out if the business is highly leveraged or not. 

#### Solvency Metrics

1.	**Total Debt to Equity** – This is calculated by dividing the total debt in a company by its total equity. This ratio tells us how much debt the company has relative to its equity.
2.	**Long term Debt to Equity** – This is calculated by dividing the long term section of the total debt by its total equity. This ratio is used to evaluate to what extent the company has long term debt financing its operations relative to the equity invested in the company.  
3.	**Interest coverage ratio** – The formula is, Earnings before interest and taxes (EBIT) or operating profit divided by the company’s interest expenses. This shows how many times the company can pay its current interest expense with its earnings. 

#### Liquidity Metrics

1.	**Current Ratio** – This is calculated by dividing current assets with current liabilities. This tells us how much liquid assets the company has relative to its immediate short-term liabilities. 
2.	**Quick Ratio** – It is calculated by dividing the amount, current assets minus inventory, with current liabilities. This is a more stringent measure as it suggests how liquid the company is solely based on its cash and cash reserves (excluding inventory) relative to its short-term liabilities.  

#### Growth Metrics

1.	**5-year sales growth** – This is the growth rate of the company’s total revenue over a five-year period. It shows the historic growth potential of the stock’s revenue. 
2.	**5-year earnings growth** – This is the growth rate of the company’s total net profit over a five-year period. It shows the historic growth potential of the stock’s profit.  



### Data to explore with financials and stock data
1. How do I find the most undervalued company based on financials?
    - P/CF or P/FCF (Price to Cash Flow or Price to Free Cash Flow) - **DP1**

### Data Pipelines
1. DP1
    - Dataframe structure
        Symbol, Company Name, Sector, Industry, Stock Price, P/CF, Market Cap
