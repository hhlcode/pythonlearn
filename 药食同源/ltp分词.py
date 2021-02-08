from ltp import LTP
import pandas as pd 

df = pd.read_csv('分词以后的药食同源.csv',encoding = 'utf-8')

ltp = LTP()

# user_dict.txt 是词典文件， max_window是最大前向分词窗口
ltp.init_dict(path="中药大词典合集.txt", max_window=4)
# segment, _ = ltp.seg(["他叫汤姆去拿外衣。"])
print(segment)