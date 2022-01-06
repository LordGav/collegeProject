import requests
import json
import inspect
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def getBANKNIFTY():
    try:
        url = 'https://appfeeds.moneycontrol.com/jsonapi/market/indices&format=json&t_device=iphone&t_app=MC&t_version=48&ind_id=23'
        header = {
          "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
          "X-Requested-With": "XMLHttpRequest"
        }
        r = requests.get(url, headers = header, timeout = 5)
        soup = json.loads(str(BeautifulSoup(r.text, 'html.parser')))
        data = {
        'ticker' : 'BANKNIFTY',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup['indices']['lastprice']
    }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/indices/bank-nifty'
            header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
            'ticker' : 'BANKNIFTY',
            'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
            'close' : soup.find('bdo', {'class':'last-price-value'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'BANKNIFTY',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getBTC():
    try:
        startDate = (datetime.utcnow()-timedelta(minutes=2)).strftime('%Y-%m-%dT%H:%M')
        endDate = datetime.utcnow().strftime('%Y-%m-%dT%H:%M')
        url = f'https://production.api.coindesk.com/v2/price/values/BTC?start_date={startDate}&end_date={endDate}&ohlc=false'
        header = {
          "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
          "X-Requested-With": "XMLHttpRequest"
        }
        r = requests.get(url, headers = header, timeout = 5)
        soup = json.loads(str(BeautifulSoup(r.text, 'html.parser')))
        data = {
        'ticker' : 'BTC',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup['data']['entries'][-1][-1]
    }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/crypto/bitcoin'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'BTC',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.findAll('span', {'dir':'ltr'})[0].text[1:].strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'BTC',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getGOLD():
    try:
        url = 'https://markets.businessinsider.com/Ajax/Chart_GetIntradayQuotes?instrumentType=Commodity&tkData=300009,1,0,333'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = json.loads(str(BeautifulSoup(r.text, 'html.parser')))
        data = {
        'ticker' : 'GOLD',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup[-1]['Close']
    }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/commodities/gold'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'GOLD',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('bdo', {'class':'last-price-value'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'GOLD',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getUSDINR():
    try:
        url = 'https://query1.finance.yahoo.com/v8/finance/chart/INR=X?region=IN&lang=en-IN&includePrePost=false&interval=2m&useYfid=true&range=1d&corsDomain=in.finance.yahoo.com&.tsrc=finance'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = json.loads(str(BeautifulSoup(r.text, 'html.parser')))
        data = {
        'ticker' : 'USDINR',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup['chart']['result'][0]['meta']['regularMarketPrice']
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/currencies/usd-inr'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'USDINR',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('bdo', {'class':'last-price-value'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'USDINR',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getINDIA10Y():
    try:
        url = 'https://tradingeconomics.com/india/government-bond-yield'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = BeautifulSoup(r.text, 'html.parser')
        data = {
        'ticker' : 'INDIA10Y',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup.select('#p')[0].text.strip()
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/rates-bonds/india-10-year-bond-yield'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'INDIA10Y',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('span', {'id':'last_last'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'INDIA10Y',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getUK10Y():
    try:
        url = 'https://tradingeconomics.com/united-kingdom/government-bond-yield'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = BeautifulSoup(r.text, 'html.parser')
        data = {
        'ticker' : 'UK10Y',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup.select('#p')[0].text.strip()
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/rates-bonds/uk-10-year-bond-yield'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'UK10Y',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('span', {'id':'last_last'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'UK10Y',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getGERMANY10Y():
    try:
        url = 'https://tradingeconomics.com/germany/government-bond-yield'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = BeautifulSoup(r.text, 'html.parser')
        data = {
        'ticker' : 'GERMANY10Y',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup.select('#p')[0].text.strip()
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://www.investing.com/rates-bonds/germany-10-year-bond-yield'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'GERMANY10Y',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('span', {'id':'last_last'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'GERMANY10Y',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getJAPAN10Y():
    try:
        url = 'https://tradingeconomics.com/japan/government-bond-yield'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = BeautifulSoup(r.text, 'html.parser')
        data = {
        'ticker' : 'JAPAN10Y',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup.select('#p')[0].text.strip()
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/rates-bonds/japan-10-year-bond-yield'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'JAPAN10Y',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('span', {'id':'last_last'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'JAPAN10Y',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getCHINA10Y():
    try:
        url = 'https://tradingeconomics.com/china/government-bond-yield'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = BeautifulSoup(r.text, 'html.parser')
        data = {
        'ticker' : 'CHINA10Y',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup.select('#p')[0].text.strip()
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/rates-bonds/china-10-year-bond-yield'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'CHINA10Y',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('span', {'id':'last_last'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'CHINA10Y',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getUS10Y():
    try:
        url = 'https://tradingeconomics.com/united-states/government-bond-yield'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = BeautifulSoup(r.text, 'html.parser')
        data = {
        'ticker' : 'US10Y',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup.select('#p')[0].text.strip()
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/rates-bonds/u.s.-10-year-bond-yield'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'US10Y',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('span', {'id':'last_last'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'US10Y',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getHDFCBANK():
    try:
        url = 'https://priceapi.moneycontrol.com/pricefeed/bse/equitycash/HDF01'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = json.loads(str(BeautifulSoup(r.text, 'html.parser')))
        data = {
        'ticker' : 'HDFCBANK',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup['data']['pricecurrent']
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/equities/hdfc-bank-ltd'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'HDFCBANK',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('bdo', {'class':'last-price-value'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'HDFCBANK',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getRELIANCE():
    try:
        url = 'https://priceapi.moneycontrol.com/pricefeed/bse/equitycash/RI'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = json.loads(str(BeautifulSoup(r.text, 'html.parser')))
        data = {
        'ticker' : 'RELIANCE',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup['data']['pricecurrent']
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/equities/reliance-industries'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'RELIANCE',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('bdo', {'class':'last-price-value'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'RELIANCE',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getINFOSYS():
    try:
        url = 'https://priceapi.moneycontrol.com/pricefeed/bse/equitycash/IT'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = json.loads(str(BeautifulSoup(r.text, 'html.parser')))
        data = {
        'ticker' : 'INFOSYS',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup['data']['pricecurrent']
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/equities/infosys'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'INFOSYS',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('bdo', {'class':'last-price-value'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'INFOSYS',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getHDFC():
    try:
        url = 'https://priceapi.moneycontrol.com/pricefeed/bse/equitycash/HDF'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = json.loads(str(BeautifulSoup(r.text, 'html.parser')))
        data = {
        'ticker' : 'HDFC',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup['data']['pricecurrent']
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/equities/housing-development-finance'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'HDFC',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('bdo', {'class':'last-price-value'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'HDFC',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getICICIBANK():
    try:
        url = 'https://priceapi.moneycontrol.com/pricefeed/bse/equitycash/ICI02'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = json.loads(str(BeautifulSoup(r.text, 'html.parser')))
        data = {
        'ticker' : 'ICICIBANK',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup['data']['pricecurrent']
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/equities/icici-bank-ltd'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'ICICIBANK',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('bdo', {'class':'last-price-value'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'ICICIBANK',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getTCS():
    try:
        url = 'https://priceapi.moneycontrol.com/pricefeed/bse/equitycash/TCS'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = json.loads(str(BeautifulSoup(r.text, 'html.parser')))
        data = {
        'ticker' : 'TCS',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup['data']['pricecurrent']
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/equities/tata-consultancy-services'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'TCS',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('bdo', {'class':'last-price-value'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'TCS',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getKOTAK():
    try:
        url = 'https://priceapi.moneycontrol.com/pricefeed/bse/equitycash/KMF'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = json.loads(str(BeautifulSoup(r.text, 'html.parser')))
        data = {
        'ticker' : 'KOTAK',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup['data']['pricecurrent']
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/equities/kotak-mahindra-bank'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'KOTAK',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('bdo', {'class':'last-price-value'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'KOTAK',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getHUL():
    try:
        url = 'https://priceapi.moneycontrol.com/pricefeed/bse/equitycash/HL'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = json.loads(str(BeautifulSoup(r.text, 'html.parser')))
        data = {
        'ticker' : 'HUL',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup['data']['pricecurrent']
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/equities/hindustan-unilever'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'HUL',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('bdo', {'class':'last-price-value'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'HUL',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getAXISBANK():
    try:
        url = 'https://priceapi.moneycontrol.com/pricefeed/bse/equitycash/UTI10'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = json.loads(str(BeautifulSoup(r.text, 'html.parser')))
        data = {
        'ticker' : 'AXISBANK',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup['data']['pricecurrent']
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/equities/axis-bank'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'AXISBANK',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('bdo', {'class':'last-price-value'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'AXISBANK',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getITC():
    try:
        url = 'https://priceapi.moneycontrol.com/pricefeed/bse/equitycash/ITC'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = json.loads(str(BeautifulSoup(r.text, 'html.parser')))
        data = {
        'ticker' : 'ITC',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup['data']['pricecurrent']
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/equities/itc'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'ITC',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('bdo', {'class':'last-price-value'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'ITC',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getSBI():
    try:
        url = 'https://priceapi.moneycontrol.com/pricefeed/bse/equitycash/SBI'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = json.loads(str(BeautifulSoup(r.text, 'html.parser')))
        data = {
        'ticker' : 'SBI',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup['data']['pricecurrent']
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/equities/state-bank-of-india'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'SBI',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('bdo', {'class':'last-price-value'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'SBI',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getINDIAVIX():
    try:
        url = 'https://appfeeds.moneycontrol.com/jsonapi/market/indices&format=json&t_device=iphone&t_app=MC&t_version=48&ind_id=36'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = json.loads(str(BeautifulSoup(r.text, 'html.parser')))
        data = {
        'ticker' : 'INDIAVIX',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup['indices']['lastprice']
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/indices/india-vix'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text,'html.parser')
            data = {
                'ticker' : 'INDIAVIX',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('bdo', {'class':'last-price-value'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'INDIAVIX',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getVIX():
    try:
        url = 'https://query1.finance.yahoo.com/v8/finance/chart/%5EVIX?region=US&lang=en-US&includePrePost=false&interval=2m&useYfid=true&range=1d&corsDomain=finance.yahoo.com&.tsrc=finance'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = json.loads(str(BeautifulSoup(r.text, 'html.parser')))
        data = {
        'ticker' : 'VIX',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup['chart']['result'][0]['meta']['regularMarketPrice']
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/indices/volatility-s-p-500'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'VIX',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('bdo', {'class':'last-price-value'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'VIX',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getSENSEX():
    try:
        url = 'https://appfeeds.moneycontrol.com/jsonapi/market/indices&format=json&t_device=iphone&t_app=MC&t_version=48&ind_id=4'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = json.loads(str(BeautifulSoup(r.text, 'html.parser')))
        data = {
        'ticker' : 'SENSEX',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup['indices']['lastprice']
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/indices/sensex'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'SENSEX',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('bdo', {'class':'last-price-value'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'SENSEX',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getNIFTY():
    try:
        url = 'https://appfeeds.moneycontrol.com/jsonapi/market/indices&format=json&t_device=iphone&t_app=MC&t_version=48&ind_id=9'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = json.loads(str(BeautifulSoup(r.text, 'html.parser')))
        data = {
        'ticker' : 'NIFTY',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup['indices']['lastprice']
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/indices/s-p-cnx-nifty'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'NIFTY',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('bdo', {'class':'last-price-value'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'NIFTY',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getSPX():
    try:
        url = 'https://query1.finance.yahoo.com/v8/finance/chart/%5EGSPC?region=US&lang=en-US&includePrePost=false&interval=2m&useYfid=true&range=1d&corsDomain=finance.yahoo.com&.tsrc=finance'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = json.loads(str(BeautifulSoup(r.text, 'html.parser')))
        data = {
        'ticker' : 'SPX',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup['chart']['result'][0]['meta']['regularMarketPrice']
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/indices/us-spx-500'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'SPX',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('bdo', {'class':'last-price-value'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'SPX',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getDJI():
    try:
        url = 'https://query1.finance.yahoo.com/v8/finance/chart/%5EDJI?region=US&lang=en-US&includePrePost=false&interval=2m&useYfid=true&range=1d&corsDomain=finance.yahoo.com&.tsrc=finance'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = json.loads(str(BeautifulSoup(r.text, 'html.parser')))
        data = {
        'ticker' : 'DJI',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup['chart']['result'][0]['meta']['regularMarketPrice']
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/indices/us-30'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'DJI',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('bdo', {'class':'last-price-value'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'DJI',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getNASDAQ():
    try:
        url = 'https://query1.finance.yahoo.com/v8/finance/chart/%5EIXIC?region=US&lang=en-US&includePrePost=false&interval=2m&useYfid=true&range=1d&corsDomain=finance.yahoo.com&.tsrc=finance'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = json.loads(str(BeautifulSoup(r.text, 'html.parser')))
        data = {
        'ticker' : 'NASDAQ',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup['chart']['result'][0]['meta']['regularMarketPrice']
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/indices/nasdaq-composite'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'NASDAQ',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('bdo', {'class':'last-price-value'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'NASDAQ',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getWILSHIRE():
    try:
        url = 'https://query1.finance.yahoo.com/v8/finance/chart/%5EW5000?region=US&lang=en-US&includePrePost=false&interval=2m&useYfid=true&range=1d&corsDomain=finance.yahoo.com&.tsrc=finance'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = json.loads(str(BeautifulSoup(r.text, 'html.parser')))
        data = {
        'ticker' : 'WILSHIRE',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup['chart']['result'][0]['meta']['regularMarketPrice']
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/indices/wilshire-5000-total-market'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'WILSHIRE',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('bdo', {'class':'last-price-value'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'WILSHIRE',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getSSEC():
    try:
        url = 'https://query1.finance.yahoo.com/v8/finance/chart/000001.SS?region=US&lang=en-US&includePrePost=false&interval=2m&useYfid=true&range=1d&corsDomain=finance.yahoo.com&.tsrc=finance'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = json.loads(str(BeautifulSoup(r.text, 'html.parser')))
        data = {
        'ticker' : 'SSEC',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup['chart']['result'][0]['meta']['regularMarketPrice']
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/indices/shanghai-composite'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'SSEC',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('bdo', {'class':'last-price-value'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'SSEC',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getNIKKEI():
    try:
        url = 'https://query1.finance.yahoo.com/v8/finance/chart/%5EN225?region=US&lang=en-US&includePrePost=false&interval=2m&useYfid=true&range=1d&corsDomain=finance.yahoo.com&.tsrc=finance'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = json.loads(str(BeautifulSoup(r.text, 'html.parser')))
        data = {
        'ticker' : 'NIKKEI',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup['chart']['result'][0]['meta']['regularMarketPrice']
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/indices/japan-ni225'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'NIKKEI',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('bdo', {'class':'last-price-value'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'NIKKEI',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getDAX():
    try:
        url = 'https://query1.finance.yahoo.com/v8/finance/chart/%5EGDAXI?region=IN&lang=en-IN&includePrePost=false&interval=2m&useYfid=true&range=1d&corsDomain=in.finance.yahoo.com&.tsrc=finance'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = json.loads(str(BeautifulSoup(r.text, 'html.parser')))
        data = {
        'ticker' : 'DAX',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup['chart']['result'][0]['meta']['regularMarketPrice']
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/indices/germany-30'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'DAX',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('bdo', {'class':'last-price-value'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'DAX',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def getFTSE100():
    try:
        url = 'https://query1.finance.yahoo.com/v8/finance/chart/%5EFTSE?region=US&lang=en-US&includePrePost=false&interval=2m&useYfid=true&range=1d&corsDomain=finance.yahoo.com&.tsrc=finance'
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }
        r = requests.get(url, headers = header, timeout = 5)
        soup = json.loads(str(BeautifulSoup(r.text, 'html.parser')))
        data = {
        'ticker' : 'FTSE100',
        'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
        'close' : soup['chart']['result'][0]['meta']['regularMarketPrice']
        }

    except:
        print(f'Primary stream broken for {inspect.stack()[0][3]}')
        try:
            url = 'https://in.investing.com/indices/uk-100'
            header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"
            }
            r = requests.get(url, headers = header, timeout = 5)
            soup = BeautifulSoup(r.text, 'html.parser')
            data = {
                'ticker' : 'FTSE100',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : soup.find('bdo', {'class':'last-price-value'}).text.strip()
            }
        except:
            print(f'Both streams broken for {inspect.stack()[0][3]}')
            data = {
                'ticker' : 'FTSE100',
                'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:00'),
                'close' : float('NaN')
            }

    return data

def dataFromAllStreams():
    AXISBANK = getAXISBANK()
    BANKNIFTY = getBANKNIFTY()
    BTC = getBTC()
    CHINA10Y = getCHINA10Y()
    DAX = getDAX()
    DJI = getDJI()
    FTSE100 = getFTSE100()
    GERMANY10Y = getGERMANY10Y()
    GOLD = getGOLD()
    HDFCBANK = getHDFCBANK()
    HDFC = getHDFC()
    HUL = getHUL()
    ICICIBANK = getICICIBANK()
    INDIA10Y = getINDIA10Y()
    INDIAVIX = getINDIAVIX()
    INFOSYS = getINFOSYS()
    ITC = getITC()
    JAPAN10Y = getJAPAN10Y()
    KOTAK = getKOTAK()
    NASDAQ = getNASDAQ()
    NIFTY = getNIFTY()
    NIKKEI = getNIKKEI()
    RELIANCE = getRELIANCE()
    SBI = getSBI()
    SENSEX = getSENSEX()
    SPX = getSPX()
    SSEC = getSSEC()
    TCS = getTCS()
    UK10Y = getUK10Y()
    US10Y = getUS10Y()
    USDINR = getUSDINR()
    VIX = getVIX()
    WILSHIRE = getWILSHIRE()

    return [AXISBANK, BANKNIFTY, BTC, CHINA10Y, DAX,
            DJI, FTSE100, GERMANY10Y, GOLD, HDFCBANK,
            HDFC, HUL, ICICIBANK, INDIA10Y, INDIAVIX,
            INFOSYS, ITC, JAPAN10Y, KOTAK, NASDAQ, NIFTY,
            NIKKEI, RELIANCE, SBI, SENSEX,
            SPX, SSEC, TCS, UK10Y, US10Y, USDINR, 
            VIX, WILSHIRE]