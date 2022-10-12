import pandas as pd
import numpy as np

path = "document/dogNames2.csv"
csv = pd.read_csv(path)
print(csv)
# dataframe
#    0  1   2   3
# 0  0  1   2   3
# 1  4  5   6   7
# 2  8  9  10  11
# 竖着的为index（0轴），横着的是columns（1轴）
# data = pd.DataFrame(np.arange(12).reshape((3, 4)))
# print(data)
# data1 = pd.DataFrame(np.arange(12).reshape((3, 4)), index=list("abc"), columns=list("xyz"))
# print(data1)

data = {"name": ["mx", "jx"], "age": [18, 19], "tel": [10086, 10010]}
date_frame = pd.DataFrame(data)
print(date_frame)
data1 = [{"name": "mx", "age": 18, "tel": 1000}, {"name": "jx", "age": 15, "tel": 20000}, {"name": "yy", "age": 16}]
date_frame1 = pd.DataFrame(data1)
print(date_frame1)
