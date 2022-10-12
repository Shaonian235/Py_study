import pandas as pd
import numpy as np
import string

data = np.array(['a', 'b', 'c'])
s = pd.Series(data)
print(s)

se = pd.Series([1, 2, 3, 4], list("abcd"))
print(se)
temp_dict = {"name": "jx", "age": 18, "tel": 13}
t = pd.Series(temp_dict)
print(t)
print(t['name'])
