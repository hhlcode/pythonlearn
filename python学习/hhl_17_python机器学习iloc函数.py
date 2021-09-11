import pandas as pd
data  = pd.DataFrame({'A':[1,2,3],'B':[4,5,6],'C':[7,8,9]},index=["a","b","c"])
# print(data)
#    A  B  C
# a  1  4  7
# b  2  5  8
# c  3  6  9
# 打印5 的两种方法,也说明这两种函数的区别
# print(data.loc["b","B"]  )  #行标签为b，列标签为B 5
# print(data.iloc[1,1] )   #5是第2行第2列，索引从0开始 5
print(data.loc['b':'c','B':'C'])
#    B  C
# b  5  8
# c  6  9
print(data.iloc[1:3,1:3])  #区间前闭后是指从前面的包括后面的不包括,1到2
#    B  C
# b  5  8
# c  6  9