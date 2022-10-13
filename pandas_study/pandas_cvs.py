import pandas as pd

data = pd.read_csv("document/dogNames2.csv")
print(data.info)
print(data.describe())
# 显示头部几行
print(data.head(5))
# 按照字段排序
data = data.sort_values(by="Count_AnimalName",ascending=False)
# print(data.head(6))
# pandas取行或者取列的注意点
# - 方括号写数组，表示取行，对行进行操作
# - 方括号写字符串，表示取列，对列进行操作
print(data[:20])
print(data["Count_AnimalName"])

# 还有更多的经过pandas优化过的选择方式：
# 1.df.loc 通过标签索引行数据
# 2.df.iloc 通过位置获取行数据

