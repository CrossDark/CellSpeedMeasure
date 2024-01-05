import numpy as np
import csv

data = []

with open('/Users/liuhanbo/Downloads/CellCirculation.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        try:
            data.append(float(line[2]))
        except ValueError:
            pass

print(data)
choose = data[0:4]
print(choose)
mean_value = np.mean(choose)
print("平均值为：", mean_value)

diff_squared = [((x - mean_value) ** 2) ** 0.5 for x in choose]
print(diff_squared)
# 或者使用 np.square() 函数
# diff_squared = np.square([x - mean_value for x in data])
total = 0
for i in diff_squared:
    total += i
print(total)
