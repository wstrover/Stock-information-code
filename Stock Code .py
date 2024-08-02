#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import requests
get_ipython().run_line_magic('matplotlib', 'inline')

from urllib.request import urlopen
from bs4 import BeautifulSoup

import os
import sys
import calendar
import datetime
import numpy.ma as ma
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import sys
import yfinance as yf


# In[ ]:


#NOCT = Number of Companies taken
def Gainers(NOCT, info):
    url = "https://finance.yahoo.com/gainers"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 404:
        print(f"Failed to retrieve data: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, 'lxml')
    rows = soup.find_all('tr', class_='simpTblRow')
    
    if not rows:
        print("No data found")
        return
    
    symbols = []
    for row in rows[:NOCT]:
        symbol = row.find('td', {'aria-label': 'Symbol'}).text.strip()
        symbols.append(symbol)
    
    print(symbols)
    
    for name in symbols:
        ticker = yf.Ticker(name)
        try:
            cmpnme = ticker.info.get('shortName', 'N/A')
            comp_df = ticker.history(period="max")
            
            print('Short Name:', ticker.info.get('shortName', 'N/A'))
            print('Long Name:', ticker.info.get('longName', 'N/A'))
            print('Sector:', ticker.info.get('sector', 'N/A'))
            print('Industry:', ticker.info.get('industry', 'N/A'))
            print('Previous Close:', ticker.info.get('previousClose', 'N/A'))
            print('TwoHundred Day Average:', ticker.info.get('twoHundredDayAverage', 'N/A'))
            print('Fifty Day Average:', ticker.info.get('fiftyDayAverage', 'N/A'))
            print('Volume:', ticker.info.get('volume', 'N/A'))
            
            print(f"{cmpnme}'s stock price")
            
            if not comp_df.empty and info in comp_df.columns:
                comp_df[info].plot(title=f"{cmpnme}'s stock price")
                plt.xlabel("Date")
                plt.ylabel(info)
                plt.grid()
                plt.rcParams.update({'font.size': 14})
                plt.style.use('seaborn-dark')
                plt.rcParams["figure.figsize"] = (10, 6)
                plt.show()
                print(comp_df[info])
            else:
                print("No data available for plotting.")
                
        except KeyError as ke:
            print(f"Key error processing {name}: {ke}")
        except Exception as e:
            print(f"Error processing {name}: {e}")


Gainers(1, 'Close')


# In[ ]:


def Gainers6M(NOCT, info):
    url = "https://finance.yahoo.com/gainers"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 404:
        print(f"Failed to retrieve data: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, 'lxml')
    rows = soup.find_all('tr', class_='simpTblRow')
    
    if not rows:
        print("No data found")
        return
    
    symbols = []
    for row in rows[:NOCT]:
        symbol = row.find('td', {'aria-label': 'Symbol'}).text.strip()
        symbols.append(symbol)
    
    print(symbols)
    
    for name in symbols:
        ticker = yf.Ticker(name)
        try:
            cmpnme = ticker.info.get('shortName', 'N/A')
            today = datetime.date.today()
            before = today + relativedelta(months=-6)
            comp_df = yf.download(name, start=before, end=today, progress=False)
            
            print('Short Name:', ticker.info.get('shortName', 'N/A'))
            print('Long Name:', ticker.info.get('longName', 'N/A'))
            print('Sector:', ticker.info.get('sector', 'N/A'))
            print('Industry:', ticker.info.get('industry', 'N/A'))
            print('Previous Close:', ticker.info.get('previousClose', 'N/A'))
            print('TwoHundred Day Average:', ticker.info.get('twoHundredDayAverage', 'N/A'))
            print('Fifty Day Average:', ticker.info.get('fiftyDayAverage', 'N/A'))
            print('Volume:', ticker.info.get('volume', 'N/A'))
            
            print(f"{cmpnme}'s stock price for the last 6 months")
            if not comp_df.empty:
                comp_df[info].plot(title=f"{cmpnme}'s stock price 6 Months")
                plt.xlabel("Date")
                plt.ylabel(info)
                plt.grid()
                plt.rcParams.update({'font.size': 14})
                plt.style.use('seaborn-dark')
                plt.rcParams["figure.figsize"] = (10, 6)
                plt.show()
                print(comp_df[info])
            else:
                print("No data available for plotting.")
                
        except KeyError as ke:
            print(f"Key error processing {name}: {ke}")
        except Exception as e:
            print(f"Error processing {name}: {e}")

    
Gainers6M(1, 'Close')


# In[ ]:


def Actives(NOCT, info):
    url = "https://finance.yahoo.com/most-active"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 404:
        print(f"Failed to retrieve data: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, 'lxml')
    rows = soup.find_all('tr', class_='simpTblRow')
    
    if not rows:
        print("No data found")
        return
    
    symbols = []
    for row in rows[:NOCT]:
        symbol = row.find('td', {'aria-label': 'Symbol'}).text.strip()
        symbols.append(symbol)
    
    print(symbols)
    
    for name in symbols:
        ticker = yf.Ticker(name)
        try:
            cmpnme = ticker.info.get('shortName', 'N/A')
            comp_df = ticker.history(period="max")
            
            print('Short Name:', ticker.info.get('shortName', 'N/A'))
            print('Long Name:', ticker.info.get('longName', 'N/A'))
            print('Sector:', ticker.info.get('sector', 'N/A'))
            print('Industry:', ticker.info.get('industry', 'N/A'))
            print('Previous Close:', ticker.info.get('previousClose', 'N/A'))
            print('TwoHundred Day Average:', ticker.info.get('twoHundredDayAverage', 'N/A'))
            print('Fifty Day Average:', ticker.info.get('fiftyDayAverage', 'N/A'))
            print('Volume:', ticker.info.get('volume', 'N/A'))
            
            print(f"{cmpnme}'s stock price")
            
            if not comp_df.empty and info in comp_df.columns:
                comp_df[info].plot(title=f"{cmpnme}'s stock price")
                plt.xlabel("Date")
                plt.ylabel(info)
                plt.grid()
                plt.rcParams.update({'font.size': 14})
                plt.style.use('seaborn-dark')
                plt.rcParams["figure.figsize"] = (10, 6)
                plt.show()
                print(comp_df[info])
            else:
                print("No data available for plotting.")
                
        except KeyError as ke:
            print(f"Key error processing {name}: {ke}")
        except Exception as e:
            print(f"Error processing {name}: {e}")


Actives(1, 'Close')


# In[ ]:


def Actives6M(NOCT, info):
    url = "https://finance.yahoo.com/most-active"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 404:
        print(f"Failed to retrieve data: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, 'lxml')
    rows = soup.find_all('tr', class_='simpTblRow')
    
    if not rows:
        print("No data found")
        return
    
    symbols = []
    for row in rows[:NOCT]:
        symbol = row.find('td', {'aria-label': 'Symbol'}).text.strip()
        symbols.append(symbol)
    
    print(symbols)
    
    for name in symbols:
        ticker = yf.Ticker(name)
        try:
            cmpnme = ticker.info.get('shortName', 'N/A')
            today = datetime.date.today()
            before = today + relativedelta(months=-6)
            comp_df = yf.download(name, start=before, end=today, progress=False)
            
            print('Short Name:', ticker.info.get('shortName', 'N/A'))
            print('Long Name:', ticker.info.get('longName', 'N/A'))
            print('Sector:', ticker.info.get('sector', 'N/A'))
            print('Industry:', ticker.info.get('industry', 'N/A'))
            print('Previous Close:', ticker.info.get('previousClose', 'N/A'))
            print('TwoHundred Day Average:', ticker.info.get('twoHundredDayAverage', 'N/A'))
            print('Fifty Day Average:', ticker.info.get('fiftyDayAverage', 'N/A'))
            print('Volume:', ticker.info.get('volume', 'N/A'))
            
            print(f"{cmpnme}'s stock price for the last 6 months")
            
            if not comp_df.empty and info in comp_df.columns:
                comp_df[info].plot(title=f"{cmpnme}'s stock price 6 Months")
                plt.xlabel("Date")
                plt.ylabel(info)
                plt.grid()
                plt.rcParams.update({'font.size': 14})
                plt.style.use('seaborn-dark')
                plt.rcParams["figure.figsize"] = (10, 6)
                plt.show()
                print(comp_df[info])
            else:
                print("No data available for plotting.")
                
        except KeyError as ke:
            print(f"Key error processing {name}: {ke}")
        except Exception as e:
            print(f"Error processing {name}: {e}")


Actives6M(1, 'Close')


# In[ ]:


def TopETFs(NOCT, info):
    url = "https://finance.yahoo.com/etfs"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 404:
        print(f"Failed to retrieve data: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, 'lxml')
    rows = soup.find_all('tr', class_='simpTblRow')
    
    if not rows:
        print("No data found")
        return
    
    symbols = []
    for row in rows[:NOCT]:
        symbol = row.find('td', {'aria-label': 'Symbol'}).text.strip()
        symbols.append(symbol)
    
    print(symbols)
    
    for name in symbols:
        ticker = yf.Ticker(name)
        try:
            cmpnme = ticker.info.get('shortName', 'N/A')
            comp_df = ticker.history(period="max")
            
            print('Short Name:', ticker.info.get('shortName', 'N/A'))
            print('Long Name:', ticker.info.get('longName', 'N/A'))
            print('Previous Close:', ticker.info.get('previousClose', 'N/A'))
            print('TwoHundred Day Average:', ticker.info.get('twoHundredDayAverage', 'N/A'))
            print('Fifty Day Average:', ticker.info.get('fiftyDayAverage', 'N/A'))
            print('Volume:', ticker.info.get('volume', 'N/A'))
            
            print(f"{cmpnme}'s stock price")
            
            if not comp_df.empty and info in comp_df.columns:
                comp_df[info].plot(title=f"{cmpnme}'s stock price")
                plt.xlabel("Date")
                plt.ylabel(info)
                plt.grid()
                plt.rcParams.update({'font.size': 14})
                plt.style.use('seaborn-dark')
                plt.rcParams["figure.figsize"] = (10, 6)
                plt.show()
                print(comp_df[info])
            else:
                print("No data available for plotting.")
                
        except KeyError as ke:
            print(f"Key error processing {name}: {ke}")
        except Exception as e:
            print(f"Error processing {name}: {e}")


TopETFs(1, 'Close')


# In[ ]:


def TopETFs6M(NOCT, info):
    url = "https://finance.yahoo.com/etfs"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 404:
        print(f"Failed to retrieve data: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, 'lxml')
    rows = soup.find_all('tr', class_='simpTblRow')
    
    if not rows:
        print("No data found")
        return
    
    symbols = []
    for row in rows[:NOCT]:
        symbol = row.find('td', {'aria-label': 'Symbol'}).text.strip()
        symbols.append(symbol)
    
    print(symbols)
    
    for name in symbols:
        ticker = yf.Ticker(name)
        try:
            cmpnme = ticker.info.get('shortName', 'N/A')
            today = datetime.date.today()
            before = today + relativedelta(months=-6)
            comp_df = yf.download(name, start=before, end=today, progress=False)
            
            print('Short Name:', ticker.info.get('shortName', 'N/A'))
            print('Long Name:', ticker.info.get('longName', 'N/A'))
            print('Previous Close:', ticker.info.get('previousClose', 'N/A'))
            print('TwoHundred Day Average:', ticker.info.get('twoHundredDayAverage', 'N/A'))
            print('Fifty Day Average:', ticker.info.get('fiftyDayAverage', 'N/A'))
            print('Volume:', ticker.info.get('volume', 'N/A'))
            
            print(f"{name}'s stock price for the last 6 months")
            
            if not comp_df.empty and info in comp_df.columns:
                comp_df[info].plot(title=f"{name}'s stock price 6 Months")
                plt.xlabel("Date")
                plt.ylabel(info)
                plt.grid()
                plt.rcParams.update({'font.size': 14})
                plt.style.use('seaborn-dark')
                plt.rcParams["figure.figsize"] = (10, 6)
                plt.show()
                print(comp_df[info])
            else:
                print("No data available for plotting.")
                
        except KeyError as ke:
            print(f"Key error processing {name}: {ke}")
        except Exception as e:
            print(f"Error processing {name}: {e}")


TopETFs6M(1, 'Close')


# In[ ]:


# timeframe must be one of these: '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'
# info 'Close' and 'Open' are good to use
#timeFrame defaults to 'max' and info defaults to 'Close'
def get_companies_info_with_graphs(companies, timeFrame = 'max', info='Close'):
    
    if isinstance(companies, str):
        companies = [companies]
    
    for company_symbol in companies:
        print(f"\nFetching data for {company_symbol}...")
        ticker = yf.Ticker(company_symbol)
        
        try:
            cmpnme = ticker.info.get('shortName', 'N/A')
            long_name = ticker.info.get('longName', 'N/A')
            sector = ticker.info.get('sector', 'N/A')
            industry = ticker.info.get('industry', 'N/A')
            previous_close = ticker.info.get('previousClose', 'N/A')
            two_hundred_day_avg = ticker.info.get('twoHundredDayAverage', 'N/A')
            fifty_day_avg = ticker.info.get('fiftyDayAverage', 'N/A')
            volume = ticker.info.get('volume', 'N/A')
            
            print('Short Name:', cmpnme)
            print('Long Name:', long_name)
            print('Sector:', sector)
            print('Industry:', industry)
            print('Previous Close:', previous_close)
            print('200-Day Average:', two_hundred_day_avg)
            print('50-Day Average:', fifty_day_avg)
            print('Volume:', volume)
            
            comp_df = ticker.history(period=timeFrame)
            
            if not comp_df.empty and info in comp_df.columns:
                plt.figure()
                comp_df[info].plot(title=f"{cmpnme}'s {info} price")
                plt.xlabel("Date")
                plt.ylabel(info)
                plt.grid()
                plt.rcParams.update({'font.size': 14})
                plt.style.use('seaborn-dark')
                plt.rcParams["figure.figsize"] = (12, 6)
                plt.show()
                
                print(comp_df[info].tail())
            else:
                print(f"No data available for plotting '{info}' for {ticker_symbol}.")
        
        except KeyError as ke:
            print(f"Key error processing {ticker_symbol}: {ke}")
        except Exception as e:
            print(f"Error processing {ticker_symbol}: {e}")


companies = ['ICF', 'AAPL']  
#get_companies_info_with_graphs(companies, '6mo')


# In[ ]:


def Gain_finder(NOCT):
    url = "https://finance.yahoo.com/gainers"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to retrieve data: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, 'lxml')
    rows = soup.find_all('tr', class_='simpTblRow')
    
    if not rows:
        print("No data found")
        return
    
    list_rows = [re.sub(r'<.*?>', '', str(cell)) for cell in soup.find_all('td')]
    
    num_entries = 10 * (NOCT + 1)
    symbols = [list_rows[i:num_entries:10] for i in range(10)]
    
    df = pd.DataFrame({
        '[Symbol]': symbols[0],
        '[Name]': symbols[1],
        '[Price (Intraday)]': symbols[2],
        '[Change]': symbols[3],
        '[% Change]': symbols[4],
        '[Volume]': symbols[5],
        '[Avg Vol (3 month)]': symbols[6],
        '[Market Cap]': symbols[7],
        '[PE Ratio (TTM)]': symbols[8]
    })
    
    print('Stocks: Gainers')
    print(df)


Gain_finder(5)


# In[ ]:


def active_finder(NOCT):
    url = "https://finance.yahoo.com/most-active"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to retrieve data: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, 'lxml')
    rows = soup.find_all('tr', class_='simpTblRow')
    
    if not rows:
        print("No data found")
        return
    
    list_rows = [re.sub(r'<.*?>', '', str(cell)) for cell in soup.find_all('td')]
    
    num_entries = 10 * (NOCT + 1)
    symbols = [list_rows[i:num_entries:10] for i in range(10)]
    
    df = pd.DataFrame({
        '[Symbol]': symbols[0],
        '[Name]': symbols[1],
        '[Price (Intraday)]': symbols[2],
        '[Change]': symbols[3],
        '[% Change]': symbols[4],
        '[Volume]': symbols[5],
        '[Avg Vol (3 month)]': symbols[6],
        '[Market Cap]': symbols[7],
        '[PE Ratio (TTM)]': symbols[8]
    })
    
    print('Stocks: Most Actives')
    print(df)


active_finder(5)


# In[ ]:


def TopETF_finder(NOCT):
    url = "https://finance.yahoo.com/etfs"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to retrieve data: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, 'lxml')
    rows = soup.find_all('tr', class_='simpTblRow')
    
    if not rows:
        print("No data found")
        return
    
    list_rows = [re.sub(r'<.*?>', '', str(cell)) for cell in soup.find_all('td')]
    
    num_entries = 9 * (NOCT + 1)
    symbols = [list_rows[i:num_entries:9] for i in range(9)]
    
    df = pd.DataFrame({
        '[Symbol]': symbols[0],
        '[Name]': symbols[1],
        '[Price (Intraday)]': symbols[2],
        '[Change]': symbols[3],
        '[% Change]': symbols[4],
        '[Volume]': symbols[5],
        '[50 Day Average]': symbols[6],
        '[200 Day Average]': symbols[7]
    })
    
    print('Top ETFs')
    print(df)


TopETF_finder(5)


# In[ ]:


def loser_finder(NOCT):
    url = "https://finance.yahoo.com/losers"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to retrieve data: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, 'lxml')
    rows = soup.find_all('tr', class_='simpTblRow')
    
    if not rows:
        print("No data found")
        return
    
    list_rows = [re.sub(r'<.*?>', '', str(cell)) for cell in soup.find_all('td')]
    
    num_entries = 10 * (NOCT + 1)
    symbols = [list_rows[i:num_entries:10] for i in range(10)]
    
    df = pd.DataFrame({
        '[Symbol]': symbols[0],
        '[Name]': symbols[1],
        '[Price (Intraday)]': symbols[2],
        '[Change]': symbols[3],
        '[% Change]': symbols[4],
        '[Volume]': symbols[5],
        '[Avg Vol (3 month)]': symbols[6],
        '[Market Cap]': symbols[7],
        '[PE Ratio (TTM)]': symbols[8]
    })
    
    print('Stocks: Losers')
    print(df)


loser_finder(5)


# In[ ]:


def get_company_info(companyCode):
    company = yf.Ticker(companyCode)
    info = company.info
    hist = company.history(period="1mo")
    hist_metadata = company.history_metadata
    actions = company.actions
    dividends = company.dividends
    splits = company.splits
    capital_gains = getattr(company, 'capital_gains', None)  
    shares = company.get_shares_full(start="2022-01-01", end=None)
    income_stmt = company.income_stmt
    quarterly_income_stmt = company.quarterly_income_stmt
    balance_sheet = company.balance_sheet
    quarterly_balance_sheet = company.quarterly_balance_sheet
    cashflow = company.cashflow
    quarterly_cashflow = company.quarterly_cashflow
    major_holders = company.major_holders
    institutional_holders = company.institutional_holders
    mutualfund_holders = company.mutualfund_holders
    insider_transactions = company.insider_transactions
    insider_purchases = company.insider_purchases
    insider_roster_holders = company.insider_roster_holders
    sustainability = company.sustainability
    recommendations = company.recommendations
    recommendations_summary = company.recommendations_summary
    upgrades_downgrades = company.upgrades_downgrades
    earnings_dates = company.earnings_dates
    isin = getattr(company, 'isin', None)
    options = company.options
    news = company.news
    option_expiration_date = '2024-08-09'
    option_chain = company.option_chain(option_expiration_date) if option_expiration_date in company.options else None
    
    return {
        'info': info,
        'history': hist,
        'history_metadata': hist_metadata,
        'actions': actions,
        'dividends': dividends,
        'splits': splits,
        'capital_gains': capital_gains,
        'shares': shares,
        'income_statement': income_stmt,
        'quarterly_income_statement': quarterly_income_stmt,
        'balance_sheet': balance_sheet,
        'quarterly_balance_sheet': quarterly_balance_sheet,
        'cashflow': cashflow,
        'quarterly_cashflow': quarterly_cashflow,
        'major_holders': major_holders,
        'institutional_holders': institutional_holders,
        'mutualfund_holders': mutualfund_holders,
        'insider_transactions': insider_transactions,
        'insider_purchases': insider_purchases,
        'insider_roster_holders': insider_roster_holders,
        'sustainability': sustainability,
        'recommendations': recommendations,
        'recommendations_summary': recommendations_summary,
        'upgrades_downgrades': upgrades_downgrades,
        'earnings_dates': earnings_dates,
        'isin': isin,
        'options': options,
        'news': news,
        'option_chain': option_chain
    }



company_info = get_company_info("AAPL")
print(company_info)

print("Basic Information:")
print(company_info['info'])
print("\nHistorical Data (Last Month):")
print(company_info['history'])
print("\nEarnings Dates:")
print(company_info['earnings_dates'])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




