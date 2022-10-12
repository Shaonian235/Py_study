import matplotlib.pyplot as plt
import random
from matplotlib import rcParams

config = {
    "font.family": 'serif',
    "font.size": 12,
    "mathtext.fontset": 'stix',  # 用于设置Latex字体
    "font.serif": ['SimSun'],  # simsun字体中文版就是宋体
}
rcParams.update(config)
y_1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y_2 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
x = range(11, 31)

plt.figure(figsize=(20, 8), dpi=80)
plt.plot(x, y_1, label="me", color='r')
plt.plot(x, y_2, label="classmate")
# 设置X轴刻度
_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x, _xtick_labels)
plt.yticks(range(0, 9))
plt.xlabel("年龄")
plt.ylabel("个数")
plt.title("每年的朋友个数")
# 绘制网格
plt.grid(alpha=0.7)
plt.legend()
# 展示
plt.show()
