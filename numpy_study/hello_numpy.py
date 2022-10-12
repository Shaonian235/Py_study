import random

import numpy as np

t1 = np.array([1, 2, 3, ])  # 根据传入数值返回一个可迭代类型

print(t1)
print(type(t1))

t2 = np.array(range(10))
print(t2)
print(type(t2))
t3 = np.arange(12)
print(t3)

print(t3.dtype)

t4 = np.array(range(1, 4), dtype='float32')  # dtype可指定类型
print(t4)
print(type(t4.dtype))
t5 = np.array([random.random() for i in range(10)])
print(t5)

t6 = np.round(t5, 2)
print(t6)
# ##############################################
# 数组的形状
t7 = np.array([[1, 2, 3], [4, 5, 6]])
print(t7.shape)  # (2, 3)两行散列
t7.reshape((6,))
print(t7)
t7.flatten()
print(t7)
t8 = np.arange(4).reshape((4, 1))
print(t8)
t9 = np.arange(10)
print(t8 - t9)

