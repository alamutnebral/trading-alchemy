import os
import pandas as pd
from pandas import DataFrame, read_csv
import views


def MACD_view():
	location = os.getcwd() + r'/data/100d_4h.csv'
	#location = os.getcwd() + r'/data/2017-12-17_to_2018-03-27_100d_1h.csv'
	df = pd.read_csv(location, header=None)
	df.columns = ['timestamp', 'open', 'high', 'low', 'close', 
				  'volume', 'volume (fiat)', 'weighed_price']
	view = views.Views(df['timestamp'])
	view.MACD_view(df['open'])


def candles_view():
	location = os.getcwd() + r'/data/100d_4h.csv'
	df = pd.read_csv(location, header=None)
	df.columns = ['timestamp', 'open', 'high', 'low', 'close', 
				  'volume', 'volume (fiat)', 'weighed_price']
	view = views.Views(df['timestamp'])
	view.candles_view(df['open'], df['high'], df['low'], df['close'], df['volume'], hours=4)


if __name__ == "__main__":
	#MACD_view()
	candles_view()	