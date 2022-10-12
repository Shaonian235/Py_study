import numpy as np


def fill_ndarray(t1):
    for i in range(t1.shape[1]):
        temp_col = t1[:, i]  # 当前的一列
        nan_num = np.count_nonzero(temp_col != temp_col)
        if nan_num != 0:
            tem_not_nan = temp_col[temp_col == temp_col]  # 当前一列不为nan的array
            tem_not_nan.mean()
            temp_col[np.isnan(temp_col)] = tem_not_nan.mean()  # 选中当前为nan的位置，把值赋值为nan的均值
    return t1


if __name__ == '__main__':
    t1 = np.arange(12).reshape((3, 4)).astype(float)
    t1[1, 2:] = np.nan
    print(t1)
    t1 = fill_ndarray(t1)
    print(t1)
