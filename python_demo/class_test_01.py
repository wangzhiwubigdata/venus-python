#coding=utf-8
class MyFirstTestClass:
  classSpec="itis a test class"
  def __init__(self,word):
    print "say "+ word
  def hello(self,name):
    print"hello "+name

first = MyFirstTestClass("tom")
first.hello("jerry")



class MethodTest():
  count= 0
  def addCount(self):
    MethodTest.count+=1
    print "I am an instance method,my count is"+str(MethodTest.count),self
  @staticmethod
  def staticMethodAdd():
    MethodTest.count+=1
    print "I am a static methond,my count is"+str(MethodTest.count)
  @classmethod
  def classMethodAdd(cls):
    MethodTest.count+=1
    print "I am a class method,my count is"+str(MethodTest.count),cls

a=MethodTest()
a.addCount()
a.staticMethodAdd()
MethodTest.staticMethodAdd()
a.classMethodAdd()
MethodTest.classMethodAdd()
# MethodTest.addCount()   #调用报错

class subMethodTest(MethodTest):
  pass

# 如果父类中定义有静态方法a(),在子类中没有覆盖该方法的话，Sub.a()仍然指的是父类的a（）方法。
# 而如果a()是类方法的情况下，Sub.a()指向的是子类。
# b=subMethodTest()
# b.staticMethodAdd()
# b.classMethodAdd()
# a.classMethodAdd()
