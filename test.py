from binance.client import Client
from binance.enums import *
import config
import csv
from datetime import datetime

client = Client(config.api_key, config.api_secret)

result = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1MINUTE, "1 January, 2021")
for res in result:
    res[0] = datetime.fromtimestamp(int(res[0])/1000).strftime('%Y-%m-%d %H:%M:%S')
        

with open('./ohlcv.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(result)