import sys
import os
from datetime import datetime, timedelta

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from tools.api import get_prices

def run_test():
    """
    Tests fetching stock prices for US, HK, and TW markets.
    """
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')

    # Add .TW for Taiwan stocks as per yfinance convention
    tickers_to_test = {
        "US Stock (AAPL)": "AAPL",
        "Hong Kong Stock (0700)": "0700", # My code should handle this and add .HK
        "Taiwan Stock (2330.TW)": "2330.TW",
    }

    print("--- Starting Stock Market Query Tests ---")
    all_tests_passed = True

    for name, ticker in tickers_to_test.items():
        print(f"\nTesting {name} with ticker '{ticker}'...")
        try:
            prices = get_prices(ticker, start_date, end_date)
            if prices and len(prices) > 0:
                print(f"  [SUCCESS] Fetched {len(prices)} data points.")
                # Assuming prices are sorted descending by date
                print(f"  Latest price for {ticker} on {prices[0].time}: {prices[0].close}")
            else:
                print(f"  [FAILURE] No data returned for {ticker}.")
                all_tests_passed = False
        except Exception as e:
            print(f"  [ERROR] An exception occurred while testing {ticker}: {e}")
            all_tests_passed = False
    
    print("\n" + "-"*30)
    if all_tests_passed:
        print("All market queries seem to be working correctly!")
    else:
        print("One or more market queries failed. Please review the logs.")
    print("-"*30)


if __name__ == "__main__":
    run_test()
