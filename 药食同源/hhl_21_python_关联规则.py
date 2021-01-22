from efficient_apriori import apriori

import pandas as pd 
import operator

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
    txt = data['食材'].dropna(axis = 'rows', how='all').tolist()
    txt = data_transform(txt)
    
    # print(data)
    # exit()
    apriori_ana(txt)
    
def data_transform(txt):
    data = []
    for i in txt:
        new_list=[]
        for j in i.split('、'):
            new_list.append(j)
        data.append(new_list)
    return data

def some_data():
    """
    对不同功效的数据进行频次分析
    """  
    functions = input('请输入要进行频次分析的功效名词：')
    # functions ='美白淡斑'
    data = datasource()
    function_required = data['功效'].map(lambda x:x==functions)#筛选出美白淡斑功效的作用的数据
    sources_required = data['食材'].map(lambda x:x !='')#将空值给筛选掉
    some_data = data[function_required & sources_required] #将筛选出来的值进行连接,是一个新的datafrom
    txt = some_data['食材'].dropna(axis='rows',how='all').tolist()
    txt = data_transform(txt)
    apriori_ana(txt)

def apriori_ana(data):
    # print(data)
    # exit()
    print("数据的长度",len(data))
    support  = float(input("请输入支持度："))
    confidence  = float(input("请输入置信度："))
    
    itemsets, rules = apriori(data, support,  confidence)
    """
    将频繁项集
    """
    print(itemsets)
    print(rules)
    yn = input('是否将结果写入文件，不是的话输入n:')
    if yn == 'n':
        exit()

    ws={}
    for i in itemsets:
        dicts ={}
        for j in itemsets[i]:
            strs= str(j).replace('(','').replace(')','').replace("'",'').replace(',','')
            dicts[strs] = itemsets[i][j]
        dicts=sorted(dicts.items(),key=lambda x:x[1],reverse=True)
        ws[i]= dicts

    # 将结果写入txt文件
    names = input ('请输入文件名：')
    f = open(names,'wb')
    ss = '支持度为:'+str(support)+'置信度为:'+str(confidence)+'\n'
    f.write(ss.encode('utf-8'))
    for i in ws :
        s = '频繁'+str(i)+'项集'+'\n'
        f.write(s.encode('utf-8'))
        for j in ws[i]:
            s = str(j).replace('(','').replace(')','').replace("'",'').replace(',',':')+'\n'
            f.write(s.encode('utf-8'))
         
    s = '关联规则'
    f.write(s.encode('utf-8'))
    for i in rules:
        i = str(i).replace('(','').replace(')','').replace('{','').replace('}','')+'\n'
        f.write(i.encode('utf-8'))
    f.close()
if __name__ == "__main__":
    some_data()
# 所有数据
    # all_data()
# 根据功效来分析数据
    