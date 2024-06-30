import yfinance as yf
import matplotlib.pyplot as plt
import logging

from datetime import date


def run():
    today = date.today()
    btc = yf.download('BTC-USD', start='2015-01-01', end=today)

    # Calculate the 365-day moving average
    btc['365_MA'] = btc['Close'].rolling(window=365).mean()

    # Create a logger
    logging.basicConfig(filename='matplotlib_styles.log', level=logging.INFO, filemode='w')

    # Log the available styles
    styles = plt.style.available
    logging.info('Available styles in Matplotlib: %s', styles)

    # Plot the closing price and the moving average
    plt.style.use ('fivethirtyeight')
    plt.figure(figsize=(14, 7))
    plt.plot(btc['Close'], label='Bitcoin', linewidth=0.7)
    plt.plot(btc['365_MA'], label='365-day MA', linewidth=0.7)
    plt.title('BTC Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    run()
