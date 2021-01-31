from datetime import datetime, timedelta
import pandas as pd
import numpy as np
def historic_data_custom(client, ticker):
    """
    input: ticker ie: BTC-USD
    output: df 15 min candle sticks for the past month
    96 candles per day. Call returns 300 candles max
    """
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=3)
    historic_price_data = []
    for i in range (5):
        new_rows = client.get_product_historic_rates(ticker, start_date.isoformat(), end_date.isoformat(), 900)
        for row in new_rows:
            if len(row) == 6:
                historic_price_data.append(row)
        end_date = start_date
        start_date = end_date - timedelta(days=3)

    return pd.DataFrame(historic_price_data, columns=['time', 'low', 'high', 'open', 'close', 'volume'])

def tickers_since_high(df):
    """ Tickers since last local high
    input: dataframe
    output: int
    """
    tickers_since_ath = 0
    for i in range(df['close'].size):
        if df['close'].iloc[i] > df['close'].iloc[tickers_since_ath]:
            tickers_since_ath = i
    return tickers_since_ath


def moving_average(df, n):
    """ Moving average for the given data
    input: dataframe, average length
    output: dataframe
    https://github.com/Crypto-toolbox/pandas-technical-indicators/blob/master/technical_indicators.py
    """
    MA = pd.Series(df['close'].rolling(n, min_periods=n).mean(), name='MA_' + str(n))
    df = df.join(MA)
    return df
