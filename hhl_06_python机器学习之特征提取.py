from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

import jieba
import numpy as np
def datasets_demo():
    """
    retutn None
    sklearn 数据集的使用
    """
    # 第一步获取数据集
    iris=load_iris()
    # print("打印鸢尾花的数据集",iris)
    # print("打印数据集描述",iris['DESCR'])
    # print("查看特征名称",iris.feature_names)
    # print("查看特征值",iris.data,iris.data.shape)

#  # 
#     x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)
#     print("训练集的特征值：\n", x_train, x_train.shape)
    # 第二步数据集划分，划分为特征值和目标值的测试集和训练集
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)
# #    这里的random_state就是为了保证程序每次运行都分割一样的训练集和测试集。否则，同样的算法模型在不同的训练集和测试集上的效果不一样。
# train_data：所要划分的样本特征集
# train_target：所要划分的样本结果
# test_size：样本占比，如果是整数的话就是样本的数量,这里测试集占验证集20%
# random_state：是随机数的种子。
    print("打印训练集的特征：", x_train, x_train.shape)
    return None
def ditvect():
    """
    字典特征数据抽取
    return none
    """
    # 第一步 实例化一个转换器类，sparse 稀疏矩阵，如果将sparse矩阵转化为false ,就是普通矩阵吧 
    dict=DictVectorizer(sparse=True)
    # 调用fit_transform的方法，将集合中的数据提取,为sparse矩阵
    data =dict.fit_transform([{'city':'北京', 'temperature':100},
    {'city':'上海','temperature':77},{'city':'广州','temperature':33}])

    print("获取特征名",dict.get_feature_names())#获取特征名 ['city=上海', 'city=北京', 'city=广州', 'temperature']
    print(data.toarray(),type(data))
#  [[  0.   1.   0. 100.]
#  [  1.   0.   0.  77.]
#  [  0.   0.   1.  33.]]
    return None

def countdev():
    # """
    # 文本特征提取
    # return None CountVectorizer
    # """
    cv= CountVectorizer()
    # 中文字符应该用空格隔开
    data= cv.fit_transform(["人生苦短，我用Python","一万年太久，只争朝夕"])
    print(cv.get_feature_names())
    print(data.toarray())
    return None

def cut_word():
    """
    将很长的文本字符进行切割，用空格隔开，
    进行字符切割
    """
    con1=jieba.cut("久居南国，春夏秋冬就剩下了夏冬。春和秋，匆匆而过，仿佛中转的客人，在你还没有来得及深谈之前，她已经悄然溜走。")
    con3=jieba.cut("于是，每到秋风渐起的时候，心中都会涌起一丝遗憾。为了一睹秋色，有的人不惜驱车千里，只为一睹心中秋色，只为不错过一年的精彩。")
    con2=jieba.cut("然而，就在你彻底忘记秋的时候，秋天与你撞了个满怀。")
    # 将字符转化为列表
    content1=list(con1)
    content2=list(con2)
    content3=list(con3)
    # 将列表转为空格分割的字符
    c1=' '.join(content1)
    c2=' '.join(content2)
    c3=' '.join(content3)
    return c1,c2,c3

def hanzidev():
    c1,c2,c3=cut_word()
    cv=CountVectorizer()
    data= cv.fit_transform([c1,c2,c3])
    print(cv.get_feature_names())
    print(data.toarray())
    return None

def tfidfdev():
    # 文本频率特征提取
    c1,c2,c3=cut_word()
    tf=TfidfVectorizer()
    data= tf.fit_transform([c1,c2,c3])
    print(tf.get_feature_names())
    print(data.toarray())
    return None

# 文本归一化预处理
def mm():
    m=MinMaxScaler(feature_range=(2,3))
    data=m.fit_transform([[11,23,565,34],[45,54,55,54],[55,340,66,78]])

    print(data)

    return None

def stand():
    """
    对数据进行标准差预处理
    return None
    """

    stand=StandardScaler()
    data=stand.fit_transform([[1,2,-3],[3,2,2],[1,0,-2]])
    print(data)
    return None
def var():
     """
     特征选择，删除低方差特征
     return None
     """
     var=VarianceThreshold(threshold=0.0)
    #  将特征值相同的一列删除
     data= var.fit_transform([[0,2,0,3],[0,1,4,3],[0,1,-1,3]])
     print(data)
     return None
    # 运行当前文件
def pca():
    """
    主成分分析进行特征降维
    """
    pca=PCA(n_components=0.96)
    data=pca.fit_transform([[1,2,-3],[3,2,2],[1,0,-2]])
    # 将4个特征转化为2个
    print(data)
    return None
if __name__ == "__main__":
    # ditvect()
    # pca()
    # 测试数据集
    # datasets_demo()
    # 字典特征提取
    ditvect()