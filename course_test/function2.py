#!/usr/bin/python
# -*- coding: UTF-8 -*-

def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print "Output is: "
   print arg1
   print '可变参数类型是：',type(vartuple)
   for var in vartuple:
      print var
   return
# 调用
printinfo( 10 )
printinfo( 70, 60, 50 )