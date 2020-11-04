from sklearn.datasets import load_iris, fetch_20newsgroups
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier,export_graphviz

from pandas import pandas as pd

def knn_ieis():
    """
用KNN算法对鸢尾花进行分类
return None
    """
    # 1 获取数据
    iris = load_iris()
    # 2 划分数据集 特征值和目标值
    x_train,x_test,y_train,y_test =train_test_split(iris.data,iris.target,random_state=22)
    # 3特征工程 标准化
    # 实例化一个转换器
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    # 为什么这里只要transform
    x_test = transfer.transform(x_test)
 
    # KNN 算法预估器
    # 找到最近的3个坐标来确定自己的坐标
    estimator = KNeighborsClassifier (n_neighbors=3)
    estimator.fit(x_train,y_train)

      # 5）模型评估
    # 方法1：直接比对真实值和预测值
    # 用评估器进行预测
    y_predict = estimator.predict(x_test)
    print("输出预测值", y_predict)
    print("直接比对真实值和预测值:\n", y_test == y_predict)

    # 方法2：计算准确率
    # 利用评估器对特征检验值和目标检验值进行打分,得出来打分率
    score = estimator.score(x_test,y_test)
    print("准确率为：\n", score)

    return None
def knn_iris_gscv():
    """
    用KNN算法对鸢尾花进行分类，添加网格搜索和交叉验证

    :return:
     """
    #  1 获取数据
    iris = load_iris()

    # 2 进行数据划分
    # 训练集和测试集划分
    x_train, x_test,y_train,y_test = train_test_split(iris.data,iris.target,random_state=22)
    #  3 特征工程标准化

     # 实例化一个转化器
    transfer = StandardScaler()
    # 对特征值的训练集进行标准化处理
    x_train  = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    
    # 4 KNN算法预估器

    estimator = KNeighborsClassifier()

      # 加入网格搜索与交叉验证
    # 参数准备
    param_dict = {"n_neighbors": [1, 3, 5, 7, 9, 11]}
    # 加入网格搜索
    estimator = GridSearchCV(estimator, param_grid=param_dict, cv=10)
    # 拟合数据
    estimator.fit(x_train, y_train)
    # 5 模型评估
    # 方法1 ： 直接跟真实值对比
    y_pridect = estimator.predict(x_test)
    print(y_pridect==y_test)
   
  #  方法2 计算准确率
    score = estimator.score(x_test,y_test)
    print(score)

    # 最佳参数：best_params_
    print("最佳参数：\n", estimator.best_params_)
    # 最佳结果：best_score_
    print("最佳结果：\n", estimator.best_score_)
    # 最佳估计器：best_estimator_
    print("最佳估计器:\n", estimator.best_estimator_)
    # 交叉验证结果：cv_results_
    print("交叉验证结果:\n", estimator.cv_results_)

    return None
def nb_news():
    """
    用朴素贝叶斯算法对新闻进行分类
    :return:
    """
    # 1 获取数据
    news = fetch_20newsgroups(subset="all")

    # 2 数据集的划分
    x_train, x_test, y_train, y_test = train_test_split(news.data,news.target)
   
  #  3 特征工程：文本特征抽取-tfidf
  # 实例化一个转换器类
    transfer = TfidfVectorizer()
    # 调用fit_transform
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

# 4朴素贝叶斯算法预估器流程
    estimator = MultinomialNB()
    estimator.fit(x_train,y_train)
  
  # 5 模型评估
  # 方法一 预测值和真实值进行对比
    y_predict = estimator.predict(x_test)
    print("打印预测值", y_predict)
    print("打印比较结果", y_predict==y_test)

    # 方法2 计算准确率
    score = estimator.score(x_test, y_test)
    print("打印准确率",score)
   
    return None

def decision_iris():
    """
    用决策树对鸢尾花进行分类
    :return:None
    """
    # 1 获取数据集
    iris = load_iris()

# 2 划分数据集
    x_train, x_test, y_train, y_test = train_test_split(iris.data,iris.target, random_state= 22)
   
  #  3 决策树预估器
    estimator = DecisionTreeClassifier(criterion="entropy")
    estimator.fit(x_train,y_train)
    # 4 模型评估
    # 方法一比较预测值和真实值
    y_predict = estimator.predict(x_test)
    print("打印预测值",y_predict)
    print("对比真实值和预测值",y_predict==y_test)

    # 方法2 计算准确率
    score = estimator.score(x_test,y_test)
    print("打印准确率",score)
  # 可视化决策树
    export_graphviz(estimator,out_file = "iris_tree.dot",feature_names = iris.feature_names)

    return None

if __name__ == "__main__":
  # 用KNN算法对鸢尾花进行分类
    #  knn_ieis()
    #  用KNN算法对鸢尾花进行分类,添加网格搜索和交叉验证
    #  knn_iris_gscv()
    # 用朴素贝叶斯算法对新闻进行分类
    # nb_news()
    # 用决策树对鸢尾花进行分类
    decision_iris()
