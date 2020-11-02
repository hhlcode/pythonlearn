from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
# 倒入k近邻算法的那个包J
def knn():
    """

    用k紧邻算法预测用户签到数据 
    retun None
    """
    # 读取数据
    data= pd.read_csv("/home/hhl/Desktop/Python3天快速入门机器学习项目资料/机器学习day2资料/02-┤·┬δ/FBlocation/train.csv").head(1)
    # print(data.head(5))
    # 处理数据
    # 缩小数据查询数据信息
    data=data.query("x>1.0 & x<1.25 & y>2.5 & y<2.75")
    # 处理时间数据
    time_value=pd.to_datetime(data['time'],unit='s')
    print(time_value)
    # 将时间格式转化为字典
    time_value=pd.DatetimeIndex(time_value)
    # 构造一些特征
    data['day']=time_value.day
    data['hour']=time_value.hour
    data['weekday']=time_value.weekday
    # 把时间戳删除
    data.drop(['time'],axis=1)
    print(data)
    # 特征工程处理
 
    return  None
if __name__ == "__main__":
    knn()