#coding=utf-8

#定义函数
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4])
   mylist.extend([1,2,3,4])
   print "Values inside the function: ", mylist
   return

# 调用函数
mylist = [10,20,30]
changeme( mylist )       #python中的函数参数传递是：引用传递
print "Values outside the function: ", mylist