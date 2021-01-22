
import pandas as pd
import xlwt
class frequence_algorithm :
    def datasource(self):
        """
        获取数据源，对数据进行频数处理
        """
        # 1 获取数据
        data = pd.read_csv("C:\\Users\Seablue\Desktop\李瑶数据和论文\中药面膜数据3.0.csv",encoding='utf-8')
        # print(data.info())获取数据信息
        # 处理数据，并且对数据进行筛选
        return data
        
    def  all_data(self):
        """
        对所有数据源的食材进行获取，并且进行频次分析
        """
        data = self.datasource()#获取所有的数据
        txt = data['食材']
        txt = txt.dropna(axis='rows',how='all').tolist()#转化为list
        # print (len(txt))
        txt = self.transform(txt)#调用降维函数将数据进行降维
        self.frequencyAnaly(txt,20)#调用频次分析函数

    def some_data(self):
        """
        对不同功效的数据进行频次分析
        """  
        functions = input('请输入要进行频次分析的功效名词：')
        data = self.datasource()
        function_required = data['功效'].map(lambda x:x==functions)#筛选出美白淡斑功效的作用的数据
        sources_required = data['食材'].map(lambda x:x !='')#将空值给筛选掉
        some_data = data[function_required & sources_required] #将筛选出来的值进行连接,是一个新的datafram
        txt = some_data['食材']
        txt = txt.dropna(axis='rows',how='all').tolist()#转化为list
        txt = self.transform(txt)
        self.frequencyAnaly(txt,10)
    def  transform(self,lists):
        """
        定义一个降维函数将二维的list s数据转化为一维的list数据
        """
        p = []
        try:
            for i in lists:
                for j in i.split('、'):
                    p.append(j)
        except:
            print('结束')
        return p

    def frequencyAnaly(self,lists,num):
        """
        利用pd 对数据进行频次分析
        """
        se = pd.Series(lists)
        countDict = dict(se.value_counts().iloc[:num])
        proportitionDict = dict(se.value_counts(normalize=True).iloc[:num])
        tablenames = input('请输入表名:')
        self.excel_write(countDict,proportitionDict,tablenames)
        # for i in countDict:
        #     # print(i,':',countDict[i])
        #     s = str(i+':'+str(countDict[i]))+'\n'
        #     f.write(s.encode('utf-8'))
        # for j in proportitionDict:
        #     # print(j,':',proportitionDict[j])
        #     s = str(j+':'+str(proportitionDict[j]))+'\n'
        #     f.write(s.encode('utf-8'))
        # f.close()
    def dict_transform(self,dict1,dict2):
        data_list = []
        # 将字典转化为list
        for data in dict1 and  dict2:
            # 循环得到data字典里的所有键值对的值
            # print (data)
            # print (countDict[data])
            data_list.append(data)
            data_list.append(dict1[data])
            data_list.append(dict2[data])
        return data_list
    def excel_write(self,dict1,dict2,name):
        # 这个列表生成式主要是将数据每8个作为一个新的元素存入新的列表中，即列表套列表
        # 将字典转化为列表
        data_list = self.dict_transform(dict1,dict2)
        new_list = [data_list[i:i + 3] for i in range(0, len(data_list), 3)]
        # 生成一个xlwt.Workbook对象
        xls = xlwt.Workbook()
        # 调用对象的add_sheet方法
        sheet = xls.add_sheet('sheet1', cell_overwrite_ok=True)
        # 创建我们需要的第一行的标头数据
        heads = ['药材名', '频数','频率']
        ls = 0
        # 将标头循环写入表中
        for head in heads:
            sheet.write(0, ls, head)
            ls += 1
        i = 1
        # 将数据分两次循环写入表中 外围循环行
        for list in new_list:
            j = 0
            # 内围循环列
            for data in list:
                sheet.write(i, j, str(data))
                # print(str(data))
                j += 1
            i += 1
        # 最后将文件save保存
        xls.save(name)   
if __name__ == "__main__":
    frequence = frequence_algorithm()
#    所有数据进行频次分析
    frequence.all_data()
    # 功效数据频次分析
    # frequence.some_data()
