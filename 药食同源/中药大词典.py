import pandas  as pd 
with open ('新建文本文档.txt') as f:
    txt =[]
    for i in f.readlines():
        
        i= i.lstrip()
        print(i)
        # if 
