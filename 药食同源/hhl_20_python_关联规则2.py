# -*- coding: utf-8 -*-
"""
"""
import pandas as pd 
# coding=utf-8 
def datasource():
        """
        获取数据源，对数据进行频数处理
        """
        # 1 获取数据
        data = pd.read_csv("C:\\Users\Seablue\Desktop\李瑶数据和论文\中药面膜数据3.0.csv",encoding='utf-8')
        
        # print(data.info())获取数据信息
        # 处理数据，并且对数据进行筛选
        return data
def  all_data():
        """
        对所有数据源的食材进行获取，
        """
        data = datasource()#获取所有的数据
        data = data['食材'].dropna(axis = 'rows', how='all').tolist()
        data = data_transform(data)
        # print (data)
        # exit()
        return data
def data_transform(txt):
        data = []
        for i in txt:
            new_list=[]
            for j in i.split('、'):
                new_list.append(j)
            data.append(new_list)
        # print(data)
        # exit()
        return data
def some_data():
    """
    对不同功效的数据进行频次分析
    """  
    functions = input('请输入要进行频次分析的功效名词：')
    data = datasource()
    function_required = data['功效'].map(lambda x:x==functions)#筛选出美白淡斑功效的作用的数据
    sources_required = data['食材'].map(lambda x:x !='')#将空值给筛选掉
    some_data = data[function_required & sources_required] #将筛选出来的值进行连接,是一个新的datafram
    txt = some_data['食材'].tolist()
    txt = data_transform(txt)
    return txt

def createC1(dataSet):                  #构建所有候选项集的集合  
    C1 = [] 
    try:
        for transaction in dataSet:  
            for item in transaction:
                if item not  in C1:
                    # # print(item)  
                    # # item =  item.encode('raw_unicode_escape')
                    # item = item.decode()
                    C1.append(item)       #C1添加的是列表，对于每一项进行添加，{1},{3},{4},{2},{5}  
    except:
        print("结束")
    print(C1)
    exit()
    C1.sort()  
    return map(frozenset, C1)      #使用frozenset，被“冰冻”的集合，为后续建立字典key-value使用。  用map 是为了找到这个集合的映射  
  
def scanD(D,Ck,minSupport):             #由候选项集生成符合最小支持度的项集L。参数分别为数据集list、候选项集列表map，最小支持度  
     # 关于map对象的遍历，在内循环中遍历完最后一个元素后
     #再次访问时会放回空列表，所以外循环第二次进入的时候是空的，需要将其转为list处理
    ssCnt = {}
    ck= list(Ck)                       #字典,在这里要将map 集合转化为list ,否则循环会出错
    for tid in D: 
        # print(tid)                      #对于数据集里的每一条记录  
        for can in ck:                 #每个候选项集can  
            # print(ck[can])
            if can.issubset(tid):       #若是候选集can是作为记录的子集，那么其值+1,对其计数  
                # print(ck[can],"是",tid,"子集")
                if can not in ssCnt:       #ssCnt[can] = ssCnt.get(can,0)+1一句可破，没有的时候为0,加上1,有的时候用get取出，加1  
                    ssCnt[can] = 1  
                    
                else:  
                    ssCnt[can] +=1  #记录出现的次数
    numItems = len(list(D))#求总的项集
    # for i in ssCnt:
    #     print(ssCnt[i])
    # exit()
    retList  = []  
    supportData = {}  
    for key in ssCnt:  
        support = ssCnt[key]/numItems   #除以总的记录条数，即为其支持度  
        # print("key，value,support",key,ssCnt[key],support)
        if support >= minSupport:  
            retList.insert(0,key)       #超过最小支持度的项集，将其记录下来。  
        supportData[key] = support 
    
   
    return retList, supportData  
  
def aprioriGen(Lk, k):                  #创建符合置信度的项集Ck,  
    retList = []  
    lenLk   = len(Lk)  
    for i in range(lenLk):  
        for j in range(i+1, lenLk):     #k=3时，[:k-2]即取[0],对{0,1},{0,2},{1,2}这三个项集来说，L1=0，L2=0，将其合并得{0,1,2}，当L1=0,L2=1不添加，  
            L1 = list(Lk[i])[:k-2]  
            L2 = list(Lk[j])[:k-2]  
            L1.sort()  
            L2.sort()  
            if L1==L2:  
                retList.append(Lk[i]|Lk[j])  
    return retList  
  
def apriori(dataSet, minSupport):  
    C1 = createC1(dataSet)  
    D  = dataSet 
    L1, supportData = scanD(D,C1,minSupport)  
    L  = [L1]                           #L将包含满足最小支持度，即经过筛选的所有频繁n项集，这里添加频繁1项集  
    k  = 2  
    while (len(L[k-2])>0):              #k=2开始，由频繁1项集生成频繁2项集，直到下一个打的项集为空  
        Ck = aprioriGen(L[k-2], k)  
        Lk, supK = scanD(D, Ck, minSupport)  
        supportData.update(supK)        #supportData为字典，存放每个项集的支持度，并以更新的方式加入新的supK  
        L.append(Lk)  
        k +=1  
    return L,supportData  
if  __name__ == "__main__":
    #所有的数据进行关联规则算法
    dataSet = all_data()  
    # 根据功效对数据进行挖掘
    # dataSet = some_data()
    C1 = createC1(dataSet)  
    L1, supportData0 = scanD(dataSet,C1, 0.5)  
    print ("符合最小支持度的频繁1项集L1:\n",L1 )
    
    L, suppData = apriori(dataSet,0.5)  
    print("所有符合最小支持度0.5的项集L：\n",L  ) 
    print ("频繁2项集：\n",aprioriGen(L[0],2)  )
    L, suppData = apriori(dataSet, 0.7)  
    print ("所有符合最小支持度为0.7的项集L：\n",L )