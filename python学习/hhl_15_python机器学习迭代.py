from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression,SGDRegressor
from sklearn.metrics import mean_squared_error
from sklearn.externals import joblib

def linear1():
    """
    用线性方程对波士顿房价进行预测
    """
    # 1 获取数据集
    boston = load_boston()
     
    # 2 对数据进行划分
    x_train, x_test,y_train, y_test = train_test_split(boston.data,boston.target,random_state=22)
    # 3 标准化
    # 实例化一个转换器、
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.fit_transform(x_test)
     
    # 4 预估器
    estimator = LinearRegression()
    estimator.fit(x_train,y_train)

    # 5 得出模型
    print("线性方程的权重系数",estimator.coef_)
    print("线性方程偏置为",estimator.intercept_)
  
    # 6 模型评估
    y_predict = estimator.predict(x_test)
    print("预测的房价", y_predict)
    error = mean_squared_error(y_test,y_predict)
    print("线性方程的均方差",error)

    return None
def linear2():
    """
    # 梯度下降的方法对波士顿房价进行预
    """
    # 1 获取数据
    boston = load_boston()
     
    # 2 数据进行划分
    x_train,x_test,y_train,y_test = train_test_split(boston.data,boston.target,random_state=22)

# 3 标准化 ,实例化一个转化器类
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
# 4 模型预估器
    estimator = SGDRegressor(learning_rate="constant", eta0=0.01, max_iter=10000, penalty="l1")
    estimator.fit(x_train,y_train)

# 5 得出模型
    print("梯度下降权重",estimator.coef_)
    print("梯度下降偏置度",estimator.intercept_)
# 6 模型评估
# 方法一直接对比真实值和预估值
    y_predict = estimator.predict(x_test)
    print("预测房价",y_predict)
    error = mean_squared_error(y_test,y_predict)
    print("梯度下降均方误差",error)
    return None
def linear3():
    """
    用岭回归对波士顿房价进行预测
    """
    # 1 获取数据
    boston = load_boston()
    #  2 对数据集 进行划分
    x_train,x_test,y_train,y_test = train_test_split(boston)
    # 3 标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    
    # 4 模型预估器
    estimator = Ridge(alpha=0.5,max_iter=10000)
    estimator.fit(x_train,y_train)

    # 保存模型

    # joblib.dump(estimator, "my_ridge.pkl")
    # 加载模型
    estimator = joblib.load("my_ridge.pkl")

    # 5）得出模型
    print("岭回归-权重系数为：\n", estimator.coef_)
    print("岭回归-偏置为：\n", estimator.intercept_)

    # 6）模型评估
    y_predict = estimator.predict(x_test)
    print("预测房价：\n", y_predict)
    error = mean_squared_error(y_test, y_predict)
    print("岭回归-均方误差为：\n", error)


    return None 

if __name__=="__main__":
    #  用线性方程对波士顿房价进行预测
    # linear1()
    # 用梯度下降对波士顿房价进行预测
    # linear2()
    # 用岭回归对波士顿房价进行预测
    linear3()