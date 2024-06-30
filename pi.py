import yfinance as yf
import matplotlib.colors as nclrs
import matplotlib.pyplot as plt
import logging as log
import math

from datetime import date


def run():
    print("Hi..")

    today = date.today()
    btc = yf.download('BTC-USD', start='2016-01-01', end=today)

    # Calculate the moving averages
    slow = 360
    quick = math.floor(slow / 3.14159)
    btc[str(slow) + '_MA'] = btc['Close'].rolling(window=slow).mean() * 2
    btc[str(quick) + '_MA'] = btc['Close'].rolling(window=quick).mean()

    # Create a logger
    log.basicConfig(filename='matplotlib_styles.log', level=log.INFO, filemode='w')

    # Log background styles
    styles = plt.style.available
    log.info('Available styles in Matplotlib: %s', styles)

    # Log named colors
    colors = nclrs.CSS4_COLORS
    for color_name in colors:
        log.info('Color name: %s, RGB value: %s', color_name, colors[color_name])

    # Plot the closing price and the moving average
    plt.style.use ('fivethirtyeight')
    plt.figure(figsize=(14, 7))
    plt.plot(btc['Close'], label='Bitcoin', color='darkgray', linewidth=0.5)
    plt.plot(btc[str(slow) + '_MA'], label=str(slow) + '-day MA', color='crimson', linewidth=0.7)
    plt.plot(btc[str(quick) + '_MA'], label=str(quick) + '-day MA', color='forestgreen', linewidth=0.9)
    plt.title('BTC Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    run()
