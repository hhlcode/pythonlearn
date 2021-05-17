import jieba
import math 
#encoding=utf-8


sentence1 = '我喜欢看电影，不喜欢看动漫'
sentence2 = '我不喜欢看动漫，也不喜欢看电影'
stops = ['的','，']
segs1 = jieba.cut(sentence1)#这是一个迭代器
segs2 = jieba.cut(sentence2)
#过滤停用词的思想就是二次分词，把所有的停用词过滤以后再进行分词
def stopword(segs,stops):
    """
    函数功能：过滤停用词
    segs  分词完的句子
    stops: 停用词
    s:返回过滤完停用词的句子
    """
    s = ''
    for i  in  segs:
        # print(i)
        if i not  in stops:
            s += i
    return s
            
s1 = stopword(segs1,stops)
s2 = stopword(segs2,stops) 
# print(s1)
ss1 = jieba.cut(s1)
ss2 = jieba.cut(s2)
v1 = []
v2 = []
def cut (s):
    """
    函数功能：消除停用词的句子再进行分词
    s：分好词的句子
    return：返回词向量
    """
    v = []
    for  i in s :
        # print(i)
        v.append(i)
    return  v
v1 = cut(ss1)
v2 = cut(ss2)
v = []
for i  in v1:
    if i not in  v:
        v.append(i)
for j in v2:
    if j not in v:
        v.append(j)
# print(v1)
[1, 2, 2, 1, 1, 2, 2, 1, 1, 0]
[1, 2, 2, 1, 2, 2, 2, 1, 1, 1]

# print(v)
# print(v2)
# print(len(v1))
# print(len(v2))
#构建词典库

# print(v1)
# print(v2)
# print(v)
# print(len(v2))
def svm(v,sv):
    """
    计算单词向量出现的频次
    v:句子中的词
    sv:词典库
    """
    q = [0]*len(sv)
    # print(v)
    # print(q)
    for i in range(len(sv)):#找出总的词表中的每一个词，初始赋值为0
        for j in v:#出现次数加1
            # print("是否一致",sv[i],j)
            if sv[i] == j :
                q[i] += 1
                # print(i,q[i],j)
    return q

q1 = svm(v1,v)
q2 = svm(v2,v)
# print(v)
print(q1)
# # print(q2)
sum,m1,m2 = 0,0,0
for i in range(len(q1)):
    sum += q1[i]*q2[i]
    m1 += pow(q1[i],2)
    m2 += pow(q1[i],2)
m = 0
cos = sum/(math.sqrt(13)*math.sqrt(17))
print(cos)