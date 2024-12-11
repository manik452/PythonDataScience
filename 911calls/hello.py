import datetime

from pandas_datareader import data

start = datetime.datetime(2010, 1, 1)

end = datetime.datetime(2013, 1, 27)

# f = wb.DataReader("F", 'yahoo', start, end)
df = data.DataReader("GDP", "fred", start, end)
df.head()
# f.ix['2010-01-04']
print(df)
