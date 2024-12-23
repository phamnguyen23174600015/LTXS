import pandas as pd
file1= 'stocks1.csv'
file2= 'stocks2.csv'
stock1 = pd.read_csv(file1)
stock2 = pd.read_csv(file2)

#gộp 2 stocks thnahf 1 dataframe mới
new_df = pd.concat([stock1,stock2 ], axis = 0 , ignore_index= True)
print(new_df.head)
#tính giá trị trung bình theo các ngày và in ra 5 dòng đầuđầu
average = new_df.groupby('date')[['open', 'high', 'low', 'close']].mean()
print(average.head)