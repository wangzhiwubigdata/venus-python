# coding=utf-8
# str1='this is string';
# print str1;
#
#
# str2="this is string";
# print str2;
#
#
# str3='''this is string
# this is python string
# this is string'''
# print str3;




#格式化输出字符串
sss ="Hello,%s,%s enough for ya?"
values =('world','Hot')
print sss %values

from string import Template
s =Template("There are ${howmany} ${lang} Quotation Symbols")
print s.substitute(lang='Python',howmany=3)

##字符串 join
list=['1','2','3','4']
print list
print "##".join(("a","b"))

# bool=False;
# print bool;
# bool=True;
# print bool;

int=20
#print int

float=2.3
#print float

a=1
b=2
c=3
#print a,b,c
del a
#print a;   #删除a变量后，再调用a变量会报错