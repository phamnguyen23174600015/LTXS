import pandas as pd
file1= 'stocks1.csv'
file2= 'stocks2.csv'
file3 = 'companies.csv'

stock1 = pd.read_csv(file1)
stock2 = pd.read_csv(file2)
companies = pd.read_csv(file3)
stocks = pd.concat([stock1,stock2 ], axis = 0 , ignore_index= True)

#in ra 5 dòng dầu
print(companies.head)
#kết hợp stocks với companies
df_com = pd.merge(stocks , companies, on = 'symbol' , how = 'inner' ) 

#tính giá đóng cửa tb cho mỗi công tyty
average = df_com.groupby('symbol')['close'].mean()
print("giá đóng của tb của mỗi công tyty",average.head)