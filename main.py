import cbpro
import pandas as pd
from datetime import datetime, timedelta

from products import products
from functions import historic_data_custom, tickers_since_high


client = cbpro.PublicClient()

product = products[0]

price_df = historic_data_custom(client, product)

tickers_since = tickers_since_high(price_df)
print(tickers_since)
