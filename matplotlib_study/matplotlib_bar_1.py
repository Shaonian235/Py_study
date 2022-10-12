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
a = ["猩球崛起3：终极之战", "敦刻尔克", "蜘蛛侠：英雄归来", "战狼2"]
plt.figure(figsize=(20, 10), dpi=80)
b_16 = [15746, 312, 4497, 319]
b_15 = [12357, 156, 2045, 168]
b_14 = [2358, 399, 2358, 362]

bar_width = 0.2
x_14 = list(range(len(b_14)))
x_15 = [i + bar_width for i in x_14]
x_16 = [i + bar_width * 2 for i in x_14]
plt.bar(range(len(a)), b_14, width=bar_width)
plt.bar(x_15, b_15, width=bar_width)
plt.bar(x_16, b_16, width=bar_width)
# plt.barh(range(len(a)), b_14, height=0.5)
plt.xticks(x_15, a)  # 只需将中间的柱子对应上就行
# plt.yticks(range(len(a)), a)  # 与a对应
plt.tight_layout()
plt.show()
