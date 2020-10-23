class A :
  pass
class B(A):
    pass
print(issubclass(B,A))
print(issubclass(A,object))
# issubclass(b,a)判断a是不是b的子类
# 所有的类都是object类的子类
# isinstance (b,B)判断是不是该类的实例化对象,第二个元素可以是一个元组
class C:
  def __init__(self,x,y):
    self.x=x
    self.y=y
b=B()
print(isinstance(b,B))
print(isinstance(b,C))
print(isinstance(b,(A,B,C)))
# hasattr判断是否为该类的属性,用双引号标记，区分大小写
c1= C(1,2)
print(hasattr(c1, 'x'))
# getattr获取类中的属性
print(getattr(c1,'y',"你访问的属性不存在"))
# delattr 删除类中的属性
print(delattr(c1,'y'))
# print(delattr(c1,'y')) 删除不存在的属性会报错
class D:
  def __init__(self,size=100):
     self.size=size
  def getSize(self):
    return self.size
  def setSize(self,size):
     self.size=size
  def delSize(self):
     del self.size
  x=property(getSize,setSize,delSize)
d=D()
print(d.x)
d.x=11
print(d.x)
del d.x
# 把属性删除了，再打印会报错
# print(d.x)
"""
 对象实例化的第一个方法__new__(cls),第一个参数默认为cls一般情况下不需要重写，
 是一个静态方法，当继承不可变类型时才需要重写这个类方法，会返回一个实例化对象
"""
class CapStr(str):  
  def __new__(cls, string):
    string=string.upper()
    return str.__new__(cls,string)
ss=CapStr("I like njucm.")
print(ss)
# 演示方法__init__()和__del__()
class Show():
  def __init__(self):
    print("调用init方法")

  def __del__(self):
    print("del的方法")
    # 这个方法是最后调用的，当程序运行结束时回收内存
show=Show()
s1=show
del s1
