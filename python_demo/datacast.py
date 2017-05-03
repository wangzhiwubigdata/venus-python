# coding=utf-8
"""
x='1'
y=int(x,10)
print y,type(y)

x='1.0'
print x,type(x),id(x)
y=float(x)
print y,type(y),id(y)

x=1
y=complex(x,10)
print x,type(x)
print y,type(y)


x=[1,2,3,4]
y=str(x)
print x,type(x)
print y,type(y)


x='1+2'
y=repr(x)
z=eval(y)
print x,type(x)
print y,type(y)
#print z,type(z)


x='angelababy'  #字符串属于序列
y=tuple(x)
z=list(x)
print x,type(x),id(x)
print y,type(y),id(y)
print z,type(z),id(z)


x=97
y=chr(x)    #整型转字符
z=unichr(x)
o=ord('a')
print y,type(y)
print z,type(z)
print o,type(o)


x=10
y=hex(x)
z=oct(x)
print y,type(y)
print z,type(z)

"""