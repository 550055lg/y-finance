import yfinance as yf
from typing import Optional, List, Dict, Any
import pandas as pd


def get_current_price(ticker: str) -> Optional[float]:
    """
    Get the current stock price for a given ticker
    
    Args:
        ticker (str): Stock ticker symbol (e.g., 'AAPL', 'GOOGL')
    
    Returns:
        float: Current stock price
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period='1d')
    
    if not data.empty:
        current_price = data['Close'].iloc[-1]
        return current_price
    else:
        return None

def get_historical_prices(ticker: str, period: str = '1mo') -> pd.DataFrame:
    """
    Get historical stock prices
    
    Args:
        ticker (str): Stock ticker symbol
        period (str): Time period - valid values: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
    
    Returns:
        pandas.DataFrame: Historical price data
    """
    stock = yf.Ticker(ticker)
    historical_data = stock.history(period=period)
    return historical_data

def get_stock_info(ticker: str) -> Dict[str, Any]:
    """
    Get detailed information about a stock
    
    Args:
        ticker (str): Stock ticker symbol
    
    Returns:
        dict: Stock information
    """
    stock = yf.Ticker(ticker)
    info = stock.info
    
    return {
        'Symbol': ticker,
        'Company Name': info.get('longName', 'N/A'),
        'Current Price': info.get('currentPrice', 'N/A'),
        'Previous Close': info.get('previousClose', 'N/A'),
        'Open': info.get('open', 'N/A'),
        'Day High': info.get('dayHigh', 'N/A'),
        'Day Low': info.get('dayLow', 'N/A'),
        'Volume': info.get('volume', 'N/A'),
        'Market Cap': info.get('marketCap', 'N/A'),
    }

def get_multiple_stocks(tickers: List[str]) -> Dict[str, Optional[float]]:
    """
    Get current prices for multiple stocks
    
    Args:
        tickers (list): List of stock ticker symbols
    
    Returns:
        dict: Dictionary with ticker symbols as keys and prices as values
    """
    prices: Dict[str, Optional[float]] = {}
    for ticker in tickers:
        price = get_current_price(ticker)
        prices[ticker] = price
    return prices

# Example usage
if __name__ == "__main__":
    # Single stock example
    ticker = "AAPL"
    print(f"\n{'='*50}")
    print(f"Current Price for {ticker}")
    print(f"{'='*50}")
    
    current_price = get_current_price(ticker)
    if current_price:
        print(f"${current_price:.2f}")
    else:
        print("Unable to fetch price")
    
    # Detailed stock info
    print(f"\n{'='*50}")
    print(f"Detailed Information for {ticker}")
    print(f"{'='*50}")
    
    info = get_stock_info(ticker)
    for key, value in info.items():
        print(f"{key}: {value}")
    
    # Historical data
    print(f"\n{'='*50}")
    print(f"Historical Prices (Last 5 Days) for {ticker}")
    print(f"{'='*50}")
    
    historical = get_historical_prices(ticker, period='5d')
    print(historical[['Open', 'High', 'Low', 'Close', 'Volume']])
    
    # Multiple stocks
    print(f"\n{'='*50}")
    print("Multiple Stocks")
    print(f"{'='*50}")
    
    tickers = ['AAPL', 'GOOGL', 'MSFT', 'TSLA']
    multiple_prices = get_multiple_stocks(tickers)
    
    for ticker, price in multiple_prices.items():
        if price:
            print(f"{ticker}: ${price:.2f}")
        else:
            print(f"{ticker}: Unable to fetch price")
