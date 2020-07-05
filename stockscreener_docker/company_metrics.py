import yahoo_fin.stock_info as si
import pandas as pd
import numpy as np
from decimal import Decimal
import time

def validate_number(x):
    if type(x) == str:
        x = x.replace(",", "")
        try:
            x = float(x)
        except:
            x = np.nan
    return x

d = {'M': 3,'B': 6,'T': 9}
power = {3: float(1/2), 4: float(1/3), 5: float(1/4), 6: float(1/5)}


def text_to_num(text):
    if text[-1] in d:
        num, magnitude = text[:-1], text[-1]
        return float(Decimal(num) * 10 ** d[magnitude])
    else:
        return float(text)

def pe_ratio(val_table):
    return validate_number(val_table.iloc[2,1])

def pb_ratio(val_table):
    return validate_number(val_table.iloc[6,1])

def peg(val_table):
    return validate_number(val_table.iloc[4,1])

def pfcf(cashflow_table, val_table):
    MC = text_to_num(str(val_table.iloc[0,1]))
    FCF = cashflow_table.loc['Free Cash Flow'][0]
    if FCF == '-':
        FCF = cashflow_table.loc['Free Cash Flow'][1]
        if FCF == '-':
            FCF = np.nan 
        else: 
            FCF = validate_number(FCF)
    else:
        FCF = validate_number(FCF)
        
        
    PFCF = MC/FCF
    
    return PFCF

def sales_growth(income_table):
    power = {3: float(1/2), 4: float(1/3), 5: float(1/4), 6: float(1/5)}
    S_Current = validate_number(income_table.loc['Total Revenue'][0])
    S_Past = validate_number(income_table.loc['Total Revenue'][-1]) #this is 5yr back revenue
    
    if S_Current > 0.0 and S_Past > 0.0:
        S_CAGR = (((S_Current/S_Past)**(power[income_table.loc['Total Revenue'].size]))-1)*100
    else:
        S_CAGR = np.nan
    
    return S_CAGR

def operating_income_growth(income_table):
    power = {3: float(1/2), 4: float(1/3), 5: float(1/4), 6: float(1/5)}
    if 'Operating Income' in income_table.index:
        OI_Current = validate_number(income_table.loc['Operating Income'][0].replace(",", ""))
            
        OI_Past = validate_number(income_table.loc['Operating Income'][-1].replace(",", "")) #this is 5yr back Operating Income
    else:
        OI_Current = validate_number(income_table.loc['Pretax Income'][0].replace(",", "")) #using Pretax income instead of OI
        OI_Past = validate_number(income_table.loc['Pretax Income'][-1].replace(",", ""))
            
    if OI_Current > 0.0 and OI_Past > 0.0:
        OI_CAGR = (((OI_Current/OI_Past)**(power[income_table.loc['Total Revenue'].size]))-1)*100
    else:
        OI_CAGR = np.nan
    
    return OI_CAGR

def current_ratio(stats_table):
    return validate_number(stats_table.iloc[46,1])

def operating_margin(stats_table):
    OM = stats_table.iloc[31,1]
    if str(OM) == 'nan':
        OM = np.nan
    else:
        OM = validate_number(OM[:-1])
    
    return OM

def return_on_assets(stats_table):
    ROA = stats_table.iloc[32,1]
    if str(ROA) == 'nan':
        ROA = np.nan
    else: 
        ROA = validate_number(ROA[:-1])
    
    return ROA

def gross_margin(stats_table):
    return (text_to_num(str(stats_table.iloc[37,1]))/text_to_num(str(stats_table.iloc[34,1])))*100 

def debt_to_equity(balance_sheet):
    if 'Total Debt' in balance_sheet.index:
        t_debt = balance_sheet.loc['Total Debt'][0]
    else:
        t_debt = 0
            
    if t_debt != '-':
        t_debt = validate_number(t_debt)
    else:
        t_debt = 0

    t_equity = balance_sheet.loc['Common Stock Equity'][0]
    if t_equity != '-':
        t_equity = validate_number(t_equity)
    else:
        t_equity = 0
            
    DE = t_debt/t_equity
    
    return DE

def interest_coverage_ratio(income_table):
    
    if 'Operating Income' in income_table.index:
        OI_Current = validate_number(income_table.loc['Operating Income'][0])
    else:
        OI_Current = validate_number(income_table.loc['Pretax Income'][0]) #using Pretax income instead of OI
        
        
    if 'Interest Expense' in income_table.index and income_table.loc['Interest Expense'][0] != '-':
        ICR = OI_Current/validate_number(income_table.loc['Interest Expense'][0])
    else:
        ICR = np.nan
        
    return ICR

def Screen_1(tickers):
    main_dict = {} #set a main dictionary
    j = 0
    for ticker in tickers:
        
        t_ime = time.time()
        #import all data from yahoo finance
        val_table = si.get_stats_valuation(ticker)
        try:
            cashflow_table = si.get_cash_flow(ticker).set_index('Breakdown')
            p_fcf_test = 'good to go'
        except:
            p_fcf_test = np.nan
            
        try:
            income_table = si.get_income_statement(ticker).set_index('Breakdown')
            sales_g_test = 'good to go'
            operating_income_g_test = 'good to go'
            icr_test = 'good to go'
        except:
            sales_g_test = np.nan
            operating_income_g_test = np.nan
            icr_test = np.nan
            
        try:
            balance_sheet = si.get_balance_sheet(ticker).set_index('Breakdown')
            d_to_e_test = 'good to go'
        except:
            d_to_e_test = np.nan
            
        stats_table = si.get_stats(ticker)
        print('Time taken to import all the tables {} seconds'.format(time.time()-t_ime))
        t_ime = time.time()
        #update all valuation ratios
        pe = pe_ratio(val_table)
        pb = pb_ratio(val_table)
        pe_g = peg(val_table)
        
        if p_fcf_test != np.nan:
            p_fcf = pfcf(cashflow_table, val_table)
        else:
            p_fcf = np.nan
        
        #update all growth ratios
        if sales_g_test != np.nan:
            sales_g = sales_growth(income_table)
        else:
            sales_g = np.nan
        
        if operating_income_g_test != np.nan:
            operating_income_g = operating_income_growth(income_table)
        else:
            operating_income_g = np.nan
        
        #update all liquidity ratios
        current_r = current_ratio(stats_table)
        
        #update all profitability ratios
        operating_mar = operating_margin(stats_table)
        roa = return_on_assets(stats_table)
        gross_mar = gross_margin(stats_table)
        
        #update all solvency ratios
        if d_to_e_test != np.nan:
            d_to_e = debt_to_equity(balance_sheet)
        else:
            d_to_e = np.nan
        
        if icr_test != np.nan:
            icr = interest_coverage_ratio(income_table)
        else:
            icr = np.nan
        
        #create a list named after the ticker and append each ratio
        stock_ticker = ticker
        ticker = []
        ticker.append(pe)
        ticker.append(pb)
        ticker.append(pe_g)
        ticker.append(p_fcf)
        ticker.append(sales_g)
        ticker.append(operating_income_g)
        ticker.append(current_r)
        ticker.append(operating_mar)
        ticker.append(roa)
        ticker.append(gross_mar)
        ticker.append(d_to_e)
        ticker.append(icr)
        
        #assign the updated list to main dictionary
        main_dict[stock_ticker] = ticker
        
        
        j+=1
        print (j)
        
    #create a dataframe using the main dictionary
    screened_df = pd.DataFrame(data = main_dict)
    screened_df_t = screened_df.transpose()
    
    screened_df_t.columns = ['P/E', 'P/B', 'PEG', 'P/FCF',
                             'Sales Growth %', 'Operating Income Growth %', 
                             'Current Ratio',
                             'Operating Margin %', 'Return on Assets %', 'Gross Margin %',
                             'Debt/Equity', 'Interest Coverage Ratio']
    print('Time taken to complete the rest of the code {} seconds'.format(time.time() - t_ime))
    
    return screened_df_t

