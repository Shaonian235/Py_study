import numpy as np
import matplotlib.pyplot as plt

us_file_path = "document/USvideos0123.csv"
uk_file_path = "document/GBvideos0123.csv"
us_data = np.loadtxt(us_file_path, delimiter=",", dtype=int)  # delimiter->按照什么把数据分割,unpack->转置
uk_data = np.loadtxt(uk_file_path, delimiter=",", dtype=int)  # delimiter->按照什么把数据分割,unpack->转置
us_comments = us_data[:-1]
# 选择比5000小的数据
us_comments = us_comments[us_comments <= 5000]
print(us_comments.max(), us_comments.min())

d = 500
bin_nums = (us_comments.max() - us_comments.min()) // d
print(bin_nums)
plt.figure(figsize=(20, 8), dpi=90)
plt.hist(us_comments, bin_nums)
plt.show()
