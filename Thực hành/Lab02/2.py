import numpy as np
import csv
with open('diem_hoc_phan.csv', newline='', encoding='utf-8') as file:
    data = list(csv.reader(file, delimiter=",")) 
numpy_arr = np.array(data[1 :])
print(numpy_arr)
hp1 = numpy_arr[:,2 ].astype(float)
hp2 = numpy_arr[:, 3].astype(float)
hp3 = numpy_arr[:, 4].astype(float)
#của hp1
sum = np.sum(hp1)
tb = np.mean(hp1)
dlc = np.std(hp1)
##hp2 3 tương tự
def tranfer(grade):
    if 8.5 <= grade <= 10:
        return 'A'
    elif 8.0 <= grade < 8.5:
        return 'B+'
    elif 7.0 <= grade < 8.0:
        return 'B'
    elif 6.5 <= grade < 7.0:
        return 'C+'
    elif 5.5 <= grade < 6.5:
        return 'C'
    elif 5.0 <= grade < 5.5:
        return 'D+'
    elif 4.0 <= grade < 5.0:
        return 'D'
    else:
        return 'F'
    
grade_hp1 = [tranfer(grade) for grade in hp1 ]

def grade_count(lst):
    count = {'A': 0, 'B+': 0, 'B': 0, 'C+': 0, 'C': 0, 'D': 0, 'F': 0}
    for grade in lst:
        if grade in count:
            count[grade] += 1
    return count

dem = grade_count(grade_hp1)
print(dem)