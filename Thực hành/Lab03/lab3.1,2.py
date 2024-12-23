import pandas as pd
#đọc file vaò dataframe
file = 'stocks1.csv'
stocks1 = pd.read_csv(file)

#in ra 5 dòng đầuđầu
print(stocks1.head())

#in ra kiểu dữ liệu của các cột
print(stocks1.dtypes)

#in ra thông tin tổng quan của dữu liệu stocks11
stocks1.info()

#kiểm tra có giá trị null ở các cột k
print(stocks1.isnull().any())

#thay thế null ở cột high(low) thành mean của cột high(low)
mean_high = stocks1['high'].mean()
mean_low = stocks1['low'].mean()
stocks1['high'].fillna(mean_high, inplace = True)
stocks1['low'].fillna(mean_low, inplace = True)
print(stocks1.head)

#kiểm tra xem còn giá trị null nào k
stocks1.info()