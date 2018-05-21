import os
import pandas as pd
from pandas import DataFrame, read_csv

def compress(df, hours):
	df_h = df[df[0] % (60 * hours) == 0]
	#print(df_h[10:15])
	for i in range(len(df_h)):
		j = i * 60 * hours
		df_h.iloc[i, 2] = max(df[j:j+60*hours][2]) #high
		df_h.iloc[i, 3] = min(df[j:j+60*hours][3]) #low
		df_h.iloc[i, 4] = df.iloc[j+60*hours - 1, 4] #high
	print(df_h[15:25])
	return df_h


def minutes(days):
	return days * 24 * 60


def drop_days(days, df):
	rows_to_drop = df.shape[0] - minutes(days=days) #'all rows' - 'last 100-day rows'
	df = df.drop(df.index[:rows_to_drop])
	df[0] = (df[0] - df[0].min()) // 60 #seconds
	return df


location = os.getcwd() + r'/data/coinbaseUSD_1-min_data_2014-12-01_to_2018-03-27.csv'
df = pd.read_csv(location, header=None)

df[0] = pd.to_numeric(df[0], errors='coerse', downcast='integer')
df[0] = df[0].fillna(0.0).astype(int)
df[1] = pd.to_numeric(df[1], errors='coerse')
df[2] = pd.to_numeric(df[1], errors='coerse')
df[3] = pd.to_numeric(df[1], errors='coerse')
df[4] = pd.to_numeric(df[1], errors='coerse')
df[5] = pd.to_numeric(df[1], errors='coerse')
df[6] = pd.to_numeric(df[1], errors='coerse')
df[7] = pd.to_numeric(df[1], errors='coerse')

#del df[0] #Timestamp
#del df[1] #Open
#del df[2] #High
#del df[3] #Low
#del df[4] #Close
#del df[5] #Volume
#del df[6] #Volume(fiat)
#del df[7] #Weighted price

df = drop_days(100, df)
df_h = compress(df, hours=1)
print(len(df_h))
df_h.to_csv('100d_1h.csv', index=False, header=False)