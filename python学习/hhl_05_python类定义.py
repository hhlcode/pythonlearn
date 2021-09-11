class Cat():
    # def eat(self):
    #     print("%s吃鱼" %self.name)

    # def drink(self):
    #     print("%s猫喝水" %self.name) 
    
    def __init__(self,name):
        self.name=name
        print("我是%s" % self.name)
        #类的初始化函数

    def __del__(self):
        print("%s被回收了 " %self.name)
        # 类的回收机制，运行结束实行，回收内存空间

    def __str__(self):
        return "我是字符%s"% self.name
        # 返回一个字符串
Tom=Cat("tom")
print(Tom)

