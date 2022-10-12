# 什么是matplotlib？
1.能将数据进行可视化，更直观的呈现

2.使数据更加客观，更具说服力

3.全局中文设置
```python
from matplotlib import rcParams
config = {
    "font.family":'serif',
    "font.size": 12,
    "mathtext.fontset":'stix',   # 用于设置Latex字体
    "font.serif": ['SimSun'],     # simsun字体中文版就是宋体
}
```
## 在一个图例上绘制多个图形(多次plot)即可

## 散点图（scatter）
## 柱状图（bar）
位置不对应
```python
TypeError: barh() got multiple values for argument 'width'
```
# 直方图（hist）
