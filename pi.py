import yfinance as yf
import matplotlib.pyplot as plt
import logging
import math

from datetime import date


def run():
    today = date.today()
    btc = yf.download('BTC-USD', start='2015-01-01', end=today)

    # Calculate the moving averages
    slow = 360
    quick = math.floor(slow / 3.14159)
    btc[str(slow) + '_MA'] = btc['Close'].rolling(window=slow).mean() * 2
    btc[str(quick) + '_MA'] = btc['Close'].rolling(window=quick).mean()

    # Create a logger
    logging.basicConfig(filename='matplotlib_styles.log', level=logging.INFO, filemode='w')

    # Log the available styles
    styles = plt.style.available
    logging.info('Available styles in Matplotlib: %s', styles)

    # Plot the closing price and the moving average
    plt.style.use ('fivethirtyeight')
    plt.figure(figsize=(14, 7))
    plt.plot(btc['Close'], label='Bitcoin', linewidth=0.75)
    plt.plot(btc[str(slow) + '_MA'], label=str(slow) + '-day MA', linewidth=0.9)
    plt.plot(btc[str(quick) + '_MA'], label=str(quick) + '-day MA', linewidth=0.9)
    plt.title('BTC Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    run()
