import numpy as np
#tạo numpy_arr với efficiency và shifts
with open('efficiency.txt') as f:
    efficiency = list(map(int, f.read().splitlines()))

with open('shifts.txt') as g:
    shifts = g.read().splitlines()

efficiency_arr = np.array(efficiency)
print("eficiency datatype: ", efficiency_arr.dtype)
shifts_arr = np.array(shifts)
print("shifts datatype: ", shifts_arr.dtype)

#tách data các ca
morning = efficiency_arr[shifts_arr == 'Morning']
Afternoon = efficiency_arr[shifts_arr == 'Afternoon']
Night = efficiency_arr[shifts_arr == 'Night']
un_morning = efficiency_arr[shifts_arr != 'Morning']\

#tính trung bình các caca
averange_night = np.mean(Night)
averange_afternoon = np.mean(Afternoon)
averange_morning = np.mean(morning)
averange_unmorning = np.mean(un_morning)

#trả về kết quả
print("Hiệu suất trung bình ca sáng: ",averange_morning)
print("Hiệu suất trung bình các ca kháckhác",averange_unmorning)
print("Hiệu suất trung bình ca tối: ", averange_night)
print("Hiệu suất trung bình ca chiều: ", averange_afternoon)

#tạo mảng dữ liệu có cấu trúc worker
worker =np.array(
    list(zip(shifts, efficiency)),
    dtype=[('shift', 'U10'), ('efficiency', 'float')])

#sắp xếp mảng worker
worker_sort = np.sort(worker , order=efficiency)

#sắp xếp hiệu xuất cao và thấp nhất
hight = worker_sort[-1]
low = worker_sort[0]

print("hiệu suất cao nhất: ", hight )

print("Hiệu suất thấp nhất: ", low)

print("Mảng worker sắp xếp thep efficiency: ", worker_sort)