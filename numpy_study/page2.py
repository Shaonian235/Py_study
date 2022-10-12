import numpy as np

## 希望把之前案例中两个国家的数据放到一起研究分析，同时保留国家的信息（每条数据的国家来源）
# 加载国家数据
# views,likes,dislikes,comment_total
us_file_path = "document/USvideos0123.csv"
uk_file_path = "document/GBvideos0123.csv"
us_data = np.loadtxt(us_file_path, delimiter=",", dtype=int)  # delimiter->按照什么把数据分割,unpack->转置
uk_data = np.loadtxt(uk_file_path, delimiter=",", dtype=int)  # delimiter->按照什么把数据分割,unpack->转置
# 添加国家信息
# 构造全为0的数据
zero_data = np.zeros((us_data.shape[0], 1)).astype(int)
one_data = np.ones((uk_data.shape[0], 1)).astype(int)
# 分别添加一列全为1和全为0的数字
us_data = np.hstack((us_data, zero_data))
uk_data = np.hstack((uk_data, one_data))
# print(us_data)
# print(uk_data)
# 拼接两组数据
final_data = np.vstack((us_data, uk_data))
print(final_data)
eye = np.eye(4)  # 快速生成对角阵
print(eye)
max_data = np.argmax(final_data, axis=0)#最大值的位置
print(max_data)
min_data = np.argmax(final_data, axis=1)# 最小值的位置
print(min_data)

np.random.random()