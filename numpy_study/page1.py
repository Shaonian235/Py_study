import numpy as np

# views,likes,dislikes,comment_total
us_file_path = "document/USvideos0123.csv"
uk_file_path = "document/GBvideos0123.csv"
t1 = np.loadtxt(us_file_path, delimiter=",", dtype=int)  # delimiter->按照什么把数据分割,unpack->转置

print(t1)
# 转置
a1 = np.arange(24).reshape((4, 6))
print(a1)
# 1.transpose
a1 = a1.transpose()
print(a1)
a1 = a1.swapaxes(1, 0)  # 0,1轴互相转换
print(a1)
print("*" * 100)
# 取行
print(a1[1])
print("*" * 100)
print(t1)
print("*" * 100)

# 取连续的多行,从第二行开始
print(t1[2:])
print("*" * 100)

# 取不连续的多行第2,8,10行
print(t1[[2, 8, 10]])
print("*" * 100)

# 取行
print(t1[1, :])
print(t1[2:, :])
print(t1[[2, 10, 3], :])
# 取列
print(t1[:, 1])
# 取连续的多列,取从第三列开始后面的每一列
print(t1)
print("=" * 100)
print(t1[:, 2:])
# 取不连续的多列, 第一列和第三列
print(t1[:, [0, 2]])
print("=" * 100)
# 取多行和多列 取第3行到第5行，第2列到第4列的结果
b = t1[2:5, 1:4]
print(b)
print("=" * 100)
# 去多个不相邻的点
c = t1[[0, 2], [0, 1]]
print(c)
# 把t1中小于10的数改为3
d = t1 < 10
print(d)  # 为True的就是小于10的数字
t1[t1 < 10] = 3
print(t1)
# 把小于10的数字替换为0 把大于20的数替换为20
t1 = np.where(t1 < 10, 0, 10)  # numpy的三元运算符，t1中数小与10的数等于0，否则就等于10
print(t1)
# t.clip(10,18)小于10的替换为10，大于18的替换为18

### 数组的拼接
## np.vstack((t1,t2))竖直拼接
## np.hstack(t1,t2)水平拼接
### 数组的行列交换
t1[[1, 2], :] = t1[[2, 1], :]  # 行交换
t1[:, [0, 2]] = t1[:, [2, 0]]  # 列交换

