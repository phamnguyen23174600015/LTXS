import pandas as pd
file1= 'stocks1.csv'
file2= 'stocks2.csv'
file3 = 'companies.csv'

stock1 = pd.read_csv(file1)
stock2 = pd.read_csv(file2)
companies = pd.read_csv(file3)
stocks = pd.concat([stock1,stock2 ], axis = 0 , ignore_index= True)

#multiindex
stocks.set_index(['date' , 'symbol'], inplace = True)

#tính giá trị tb cho mỗi ngày
average_stock = stocks.groupby(['date', 'symbol']).mean()
print(average_stock)

#sắp xếp
average_stock.sort_index(inplace = True)
print(average_stock.head)