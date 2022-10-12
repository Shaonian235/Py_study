import matplotlib.pyplot as plt
import random

# x = range(2, 40, 2)
# y = [12, 45, 23, 25, 29, 33, 24, 12, 25, 14]
# # 设置图片大小
# plt.figure(figsize=(20, 8), dpi=80)
# plt.plot(x, y)
# # 设置x轴刻度
# xtick_labels = [i / 2 for i in (2, 49)]
# plt.xticks(range(2, 50))
# plt.yticks(range(min(y), max(y)))
# plt.show()
# 这种方式是设置全局字体，图例和坐标轴都可以使用中文。但好像会更改默认设置？（也可能是自己修改了配置文件导致的）
# 设置公式字体
from matplotlib import rcParams

config = {
    "font.family": 'serif',
    "font.size": 12,
    "mathtext.fontset": 'stix',  # 用于设置Latex字体
    "font.serif": ['SimSun'],  # simsun字体中文版就是宋体
}
rcParams.update(config)
plt.figure(figsize=(20, 8))
x = range(120)
random.seed(10)  # 设置随机种子，让不同时刻的随机得到的数都一样
y = [random.uniform(20, 35) for i in range(120)]
plt.plot(x, y)
x_ticks = ["10点{}分".format(i) for i in x if i < 60]
x_ticks += ["11点{}分".format(i - 60) for i in x if i > 60]
# 默认不支持中文，需设置
plt.xticks(x[::5], x_ticks[::5], rotation=45)  # 使用rotation使得字符串旋转90°
# plt.xticks(x[::5], x_ticks[::5], rotation=45, fontproperties="STSong")  # 使用rotation使得字符串旋转90°
#添加描述信息
plt.xlabel("时间")
plt.ylabel("温度 单位（℃）")
plt.title("10点到12点的温度变化")
plt.show()

