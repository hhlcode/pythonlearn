import pandas as pd   
import thulac
import sys
import time
df = pd.read_csv('人工分词的药食同源.csv',encoding = 'utf-8')
def vob ():
    """
    Python 消除换行符一定.replace('\n','').replace('\r','') 
    将词表转化为一个list
    """
    with open ('中药大词典合集.txt','r') as f:
        vocabL = f.readlines() #读取的结果是list 
        vocabSet = []
        for i in vocabL:#删除换行符
            try:
                i = i.replace('\n','').replace('\r','')
                vocabSet.append(i)
            except:
                continue
        f.close()
        return  vocabSet 

vocabSet = vob()
abstract = df['摘要']
# print(abstract) #打印正确，没啥问题
def cut (abstract,vocabSet):
    time_start = time.time()
    # thul = thulac.thulac(seg_only=True)
    thul = thulac.thulac(user_dict ='中药大词典合集.txt', seg_only=True)  #只进行分词，不进行词性标注
    c = []
    for ab in abstract:#把每个文章的摘要单独提取出来
        strs = [] #把每个文章的用到的药材提取出来放在列表中
        # print(ab)
        contents = thul.cut(str(ab),text=True)#默认模式进行分词
        
        # print(contents)判断是否分词了
        # exit()
        for content in contents.split():
            # print(content)
        # exit()
            if content  in vocabSet and content != '药食同源' and content not in strs:  #判断是否在词表里面，提取中药材的关键词
                # print(content)
                strs.append(content)
                # print(strs)
                # exit()
        strs = str(strs).replace("'",'').replace('[','').replace(']','')#将其转化为一个一维的列表目的就是为转化为DataFrame类型
        c.append(strs)#将每一行分词结果添加进list
        strs = []
    time_end = time.time()
    time_sum = time_end-time_start
    print(time_sum)
    # 没引进词表的分词时间 18.486303329467773
    # 引进词表的分词时间  30.582738161087036
    return  c
text = cut(abstract,vocabSet)
# print(text)
thulacResult = pd.DataFrame(text)
df['thulac引进词表的分词'] = thulacResult
df.to_csv('人工分词的药食同源.csv',encoding = 'utf-8')
print('写入成功')