#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Parent:        # 定义父类
   def myMethod(self):
      print '调用父类方法'

class Child(Parent): # 定义子类
   def myMethod(self):
      print '调用子类方法'

c = Child()          # 子类实例
c.myMethod()         # 子类调用重写方法

a=tuple(range(1,10,2))
print(a)

b=tuple("hello")
print b

c=complex(1,2)
print c

d=repr(1+2)
print d

x=1
e=eval('x+1')
print e

f=dict([(1,2),(3,4),('a',100)])
print f.keys()
print f.values()
print f[1]
print f

y=list([1,2,3,4,5])
z=(1,2,3,4,5)
print repr(y)
print repr(z)