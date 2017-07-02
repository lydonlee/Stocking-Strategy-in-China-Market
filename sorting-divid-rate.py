import tushare as ts
import pandas as pd


FILE_RESULT = 'CSV/result.csv'

def load_to_csv_today():
	df_today_all = ts.get_today_all()
	df_today_all.to_csv('CSV/get_today_all1.csv')
	return df_today_all


def load_to_csv_profit2014_2017():

	df_profit2014 = ts.profit_data(year=2014,top=3000)
	df_profit2015 = ts.profit_data(year=2015,top=3000)
	df_profit2016 = ts.profit_data(year=2016,top=3000)
	df_profit2017 = ts.profit_data(year=2017,top=3000)

	df_profit2014.to_csv('CSV/profit2014.csv')
	df_profit2015.to_csv('CSV/profit2015.csv')
	df_profit2016.to_csv('CSV/profit2016.csv')
	df_profit2017.to_csv('CSV/profit2017.csv')

	df_profit1 = pd.merge(df_profit2014,df_profit2015,how='outer',on='code',suffixes=[2014,2015])
	df_profit2 = pd.merge(df_profit1,df_profit2016,how='outer',on='code',suffixes=["",""])
	df_profit  = pd.merge(df_profit2,df_profit2017,how='outer',on='code',suffixes=["2016",2017])

	df_profit.to_csv('CSV/profit2014-2017.csv')
	return df_profit

def updat_csv_profit2014_2017():

	df_profit2014 = pd.read_csv('CSV/profit2014.csv')
	df_profit2015 = pd.read_csv('CSV/profit2015.csv')
	df_profit2016 = pd.read_csv('CSV/profit2016.csv')
	df_profit2017 = pd.read_csv('CSV/profit2017.csv')

	df_profit1 = pd.merge(df_profit2014,df_profit2015,how='outer',on='code',suffixes=[2014,2015])
	df_profit2 = pd.merge(df_profit1,df_profit2016,how='outer',on='code',suffixes=["",""])
	df_profit  = pd.merge(df_profit2,df_profit2017,how='outer',on='code',suffixes=[2016,2017])

	df_profit.to_csv('CSV/profit2014-2017.csv')
	return df_profit

def result_csv():
	df_today_all = pd.read_csv('CSV/get_today_all1.csv')
	df_profit    = pd.read_csv('CSV/profit2014-2017.csv')
	result = pd.merge(df_today_all, df_profit, on='code')

	result['2014_profit'] = result['divi2014']/result['settlement']*100/10
	result['2015_profit'] = result['divi2015']/result['settlement']*100/10
	result['2016_profit'] = result['divi2016']/result['settlement']*100/10
	result=result.sort_values('2016_profit',ascending=False)

	result.to_csv(FILE_RESULT)

#for i, row in enumerate(df_profit.itertuples(), 1):
#df1 = ts.get_k_data("603797",start='2017-06-16',end='2017-06-16')
#df.append(df1,ignore_index=True)
#print(df)
#print(df1)


#df.to_csv('CSV/2016profit.csv')

#df['variance'] = df['budget'] + df['actual'] 

#result = pd.concat([df1, df4], axis=1, join_axes=[df1.index])


"""
time_now = datetime.now()
today=str(time_now)
print(today[:10])
print(ts.__version__)
"""

if __name__ == "__main__":
	"""
	print("result_csv:update result.csv")
	load_to_csv_today()
#	load_to_csv_profit2014_2017()
#	updat_csv_profit2014_2017()
	result_csv()
	"""
else:
	print("result.py is being imported into another module")