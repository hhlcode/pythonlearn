class CountList:
    """
    代码有点小问题,还没找到原因
    """
    def __init__(self, *args):
        print("hhh")
        # 从传递进来的参数中初始化一个value数组
        self.value=[x  for x in args]
    # 定义一个count字典来记录数组的访问次数
    # python range() 函数可创建一个整数列表，一般用在 for 循环中。
        self.count={}.fromkeys(range(len(self.value)),0)
    def __len__(self):
        # 返回数组的
        print("返回啥")
        return self.value

    def __getitem__(self,key):
        # 用字典记录数组中元素被访问的次数
        print("这个程序被执行了")
        self.count[key] +=1
        return  self.value[key]
# c1=CountList(1,2,3,4,5)
# c2=CountList(2,3,4,35,37)
# print(c1.value)
# print (c2.value)
# print(c1.value[1])
# print(c1.value[2])
# print(c1.count)