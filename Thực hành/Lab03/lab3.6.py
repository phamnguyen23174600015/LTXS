import pandas as pd

# Đọc các file CSV vào DataFrame
file1= 'stocks1.csv'
file2= 'stocks2.csv'
file3 = 'companies.csv'

stock1 = pd.read_csv(file1)
stock2 = pd.read_csv(file2)
companies = pd.read_csv(file3)

# Gộp hai DataFrame stock1 và stock2 thành một DataFrame
stocks = pd.concat([stock1, stock2], axis=0, ignore_index=True)

# Tạo pivot table
pivot_table = stocks.pivot_table(
    values='close',
    index='date',
    columns='symbol',
    aggfunc='mean'
)

# Tính tổng volume cho mỗi symbol
total_volume = stocks.groupby('symbol')['volume'].sum()

total_volume_df = total_volume.reset_index()
total_volume_df.columns = ['symbol', 'Total Volume']

# Thêm tổng volume vào pivot table như một dòng mới
pivot_table_cl = pivot_table.copy()
pivot_table_cl.loc['Total Volume'] = total_volume.reindex(pivot_table.columns).values

# Tạo một DataFrame từ pivot_table để thêm cột 'Total Volume'
pivot_table_df = pivot_table.copy()
pivot_table_df['Total Volume'] = total_volume.reindex(pivot_table.columns).values

# Sắp xếp pivot table theo 'Total Volume' giảm dần
pivot_table_sorted = pivot_table.sort_values(by='Total Volume', ascending=False)
print(pivot_table_sorted.head)

