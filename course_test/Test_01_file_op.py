#coding=utf-8

# fileHandler = open('c:/a.txt', 'a+')	#以读写方式处理文件IO
# fileHandler.seek(0)
# line = fileHandler.readline()
# while line:
# 	print line
# 	line = fileHandler.readline()
# fileHandler.close


# fileHandler = open('c:/a.txt', 'a+')	#以读写方式处理文件IO
# fileHandler.seek(0)
# #读取整个文件
# contents = fileHandler.read()
# print type(contents)
# print contents
#
#
# #读取所有行,再逐行输出
# fileHandler.seek(0)
# lines = fileHandler.readlines()
# print type(lines)
# for line  in lines:
# 	print line
# #当前文件指针的位置
# print fileHandler.tell()
#
# fileHandler.close



fileHandler = file('c:/a.txt','a+')   #或者调用open()函数
fileHandler.write("\r\n")
fileHandler.write("thank you")

fileHandler.seek(0)
contents = fileHandler.read()
print contents

fileHandler.close

