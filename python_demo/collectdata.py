# coding=utf-8

""" """

"""
nums=[1,2,3,4,5]
list=['a','bcd',1,20.2]

print list[1]
print "nums[0]:",nums[0]
print "nums[2:5]:", nums[2:5]
print "nums[2:5]:", nums[2:7]   #超出范围不报错
print "nums[1:]:", nums[1:]
print "nums[:-3]:", nums[:-3]
print "nums[:]:", nums[:]


nums=[1,2,3,4,5]
#更新列表
nums[0]="ljq"
print nums[0]


#删除列表元素
del nums[0]
print nums.__sizeof__()   #40 ?
print len(nums)
print "nums[:]:", nums[:]

#列表对+和*的操作符与字符串相似。+号用于组合列表，*号用于重复列表
x=[1, 2, 3]
print len(x)
y=[1, 2, 3] + [4, 5, 6]
print y     #[1, 2, 3, 4, 5, 6]
print ['Hi!'] * 4         #['Hi!', 'Hi!', 'Hi!', 'Hi!']
print 3 in [1, 2, 3]     #Truefor x in [1, 2, 3]: print x, #1 2 3


list=[2,1,'a']
list.append(2) #在列表末尾添加新的对象
list.count(2) #统计某个元素在列表中出现的次数
list.extend((6,7)) #在列表末尾一次性追加另一个序列中的多个值(用新列表扩展原来的列表)
list.index(2) #从列表中找出某个值第一个匹配项的索引位置，索引从0开始
list.insert(3, "insertobj") #将对象插入列表
print list
list.pop() #移除列表中的一个元素(默认最后一个元素)，并且返回该元素的值
list.remove(1) #移除列表中某个值的第一个匹配项
list.reverse() #反转列表中元素，倒转
print list
list.sort() #对原列表进行排序
print list


"""

##列表解析，用于生成列表
ra = range(1,4)
print ra,type(ra)
newlist=[2**i for i in (1,2,3)]
newlist2=[2**i for i in range(1,3)]
print newlist
print newlist2

import os
files = os.listdir("c:/test")
logfile=[f for f in files if f.endswith('.log') ]
print logfile

list1=['x','y','z']
list2=[1,23]
list3=[(i,j) for i in list1 for j in list2]
print list3


"""

tup0=()
tup1=(5,) #元组中只有一个元素时，需要在元素后面添加逗号，例如：tup1 = (50,)
tup2 = ('physics', 'chemistry', 1997, 2000)
tup3 = (1, 2, 3, 4, 5 )
tup4 = "a", "b", "c", "d"

#访问元组
tup1 = ('physics', 'chemistry', 1997, 2000)
print "tup1[0]: ", tup1[0]
print "tup1[1:5]: ", tup1[1:3]

#元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，例如:
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
# 以下修改元组元素操作是非法的。
# tup1[0] = 100;
# 创建一个新的元组
tup3 = tup1 + tup2
print tup3


#元组中的元素值是不允许删除的，可以使用del语句来删除整个元组，例如:
tup = ('physics', 'chemistry', 1997, 2000)
print tup
del tup

#元组运算符，跟字符串类似
tup = ('physics', 'chemistry', 1997, 2000)
print len(tup)
print (1,2,3)+(4,5,6)
print ('hi')*4
print 3 in (1,2,3)
for x in (1,2,3):
    print x



#元组内置函数
tup = ('physics', 'chemistry', 1997, 2000)
print cmp((1,2), (1,2))  #比较两个元组元素。
print len(tup) #计算元组元素个数。
print max(tup) #返回元组中元素最大值。
print min(tup) #返回元组中元素最小值。
print ([1,2,3]) #将列表转换为元组。


##字典
#字典是无序的对象集合。字典由键和对应的值组成。字典也被称作关联数组或哈希表

dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
#也可如此创建字典：
dict1 = { 'abc': 456 }
dict2 = { 'abc': 123, 98.6: 37 }
dict3= {'abc':1,"cc":[1,2,3]}

#访问字典，修改元素
dict3["cc"].append([5,6])
dict3["cc"].extend([7,8])
print dict3["cc"]
dict3["dd"]=888
print dict3

del dict['name']  # 删除键是'name'的条目
dict.clear()   # 清空词典所有条目
del dict    # 删除词典





#字典内置函数&方法
dict1={'a':1,'b':2}
dict2={'a':1,'b':2,'c':3}
# print cmp(dict1, dict2) #比较两个字典元素。
# print len(dict1) #计算字典元素个数，即键的总数。
# print str(dict1) #输出字典可打印的字符串表示。
# print type(dict1) #返回输入的变量类型，如果变量是字典就返回字典类型。
# dict1.clear()  #删除字典内所有元素
# print dict1
# dict0 = dict1.copy()   #返回一个字典的浅复制
# print dict0,id(dict0),id(dict1)
# dict3 = dict.fromkeys(("a","b","c"))   #创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
# print dict3
# print dict1.get('a', None)  #返回指定键的值，如果值不在字典中返回default值
# print dict1.get('d', 0)  #返回指定键的值，如果值不在字典中返回default值
# print dict1.has_key('a')  #如果键在字典dict里返回true，否则返回false
# entry = dict1.items()   #以列表返回可遍历的(键, 值) 元组列表
# print type(entry)
# for ent in entry:
#    print ent,ent[0],ent[1]
#
# keyset = dict1.keys()   #以列表返回一个字典所有的键list
# print type(keyset),keyset
# print dict1.values()   #以列表返回字典中的所有值list
#
dict1.setdefault('f',None)   #和get()类似, 但如果键不已经存在于字典中，将会添加键并将值设为default
print dict1
print dict1.update(dict2)   #把字典dict2的键/值对更新到dict里
print dict1


#获取当前时间，例如：
import time, datetime;
localtime = time.localtime(time.time())
#Local current time : time.struct_time(tm_year=2014, tm_mon=3, tm_mday=21, tm_hour=15, tm_min=13, tm_sec=56, tm_wday=4, tm_yday=80, tm_isdst=0)
print "Local current time :",localtime
#说明：time.struct_time(tm_year=2014, tm_mon=3, tm_mday=21, tm_hour=15, tm_min=13, tm_sec=56, tm_wday=4, tm_yday=80, tm_isdst=0)属于struct_time元组
#
#获取格式化的时间
#可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime():
#日期转换为字符串
#首选：
print time.strftime('%Y-%m-%d %H:%M:%S')
#其次：
print datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
#最后：
print str(datetime.datetime.now())[:19]
#字符串转换为日期
expire_time = "2013-05-21 09:50:35"
d = datetime.datetime.strptime(expire_time,"%Y-%m-%d %H:%M:%S")
print d

#获取日期差
#
oneday = datetime.timedelta(days=1)
print oneday
print datetime.timedelta(milliseconds=1), #1毫秒
print datetime.timedelta(seconds=1), #1秒
#print datetime.timedelta(minutes=1), #1分钟
##1:00:00
#print datetime.timedelta(hours=1), #1小时
##1 day, 0:00:00
#print datetime.timedelta(days=1), #1天
##7 days, 0:00:00
#print datetime.timedelta(weeks=1)
##今天
today = datetime.date.today()
#昨天
yesterday = datetime.date.today() - oneday
##明天
tomorrow = datetime.date.today() + oneday
#上周
other = datetime.date.today()- datetime.timedelta(weeks=1)
print today,yesterday,tomorrow
print "other: ",other
##获取今天零点的时间，2014-03-21 00:00:00
today_zero_time = datetime.datetime.strftime(today, '%Y-%m-%d %H:%M:%S')
print today_zero_time


"""
import time, datetime
#获取上个月最后一天
last_month_last_day = datetime.date(datetime.date.today().year,datetime.date.today().month,1)-datetime.timedelta(1)
print last_month_last_day
#字符串日期格式化为秒数，返回浮点类型：
expire_time = "2016-05-21 09:50:35"
d = datetime.datetime.strptime(expire_time,"%Y-%m-%d %H:%M:%S")
time_sec_float = time.mktime(d.timetuple())
print time_sec_float