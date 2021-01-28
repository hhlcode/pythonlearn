#!/usr/bin/env python 
#coding:utf-8 
import pandas as pd 
import thulac
df = pd.read_csv('分词以后的药食同源.csv',encoding = 'utf-8')
def vob ():
    """
    Python 消除换行符一定.replace('\n','').replace('\r','') 
    将词表转化为一个list
    """
    with open ('中药大词典合集.txt','r')as f:
        vocabL = f.readlines() #读取的结果是list 
        vocabSet = []
        for i in vocabL:#删除换行符
            i = i.replace('\n','').replace('\r','').replace('t','')
            vocabSet.append(i)
        f.close()
        return  vocabSet 

vocabset = vob()
abstract = df.iloc[:,-3]
print(abstract)
thul = thulac.thulac(seg_only=True)  #只进行分词，不进行词性标注
text = thul.cut('葛根营养丰富',text= True)
print(text)