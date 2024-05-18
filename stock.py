
import yfinance as yf
def stock_price(ticker):

          stock = yf.Ticker(ticker)

          current_price = stock.history(period='1d')['Close'][0]
          company_name = stock.info['longName']
          currency = stock.info['currency']
          stock_exchange = stock.info['exchange']
          print(f"Stock: {ticker}")
          print(f"Company Name: {company_name}")
          print(f"Current Price: {current_price} {currency}")
          print(f"Stock Exchange: {stock_exchange}")
          
          return f"Company Name: {company_name} Current Price: {current_price} {currency} "
