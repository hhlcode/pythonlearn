import time
"""
定义一个计时器去计算时间
"""
class MyTimer():
    def __init__(self):
        # 属性不能跟方法名冲突,属性名会覆盖方法名
        self.start=0
        self.end=0
        self.prompt=""
        self.lasted=[]
    
    def __str__(self):
        return self.prompt

    __rper__=__str__
    def __begin__(self):
        print("开始计时")
        self.start= time.localtime()
    
    def __stop__(self):
        self.__begin__()
        print("计时结束")
        self.end=time.localtime()
        self.__cal__()
    
    
    def __cal__(self):
       self.prompt="程序运行了"
       for index in range(6):
          self.lasted.append(self.end[index]-self.start[index])
          self.prompt+=(str(self.lasted[index]))
    
        #   将数组转为字符类型
       self.start=0
       self.end=0
mytime=MyTimer()
mytime.__stop__()

