# coding=utf-8
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4])
   # print "Values inside the function: ", mylist
   return

# 调用函数
mylist = [10,20,30]
changeme( mylist )
# print "Values outside the function: ", mylist


sum=lambda x,y:(x+1,y+1)
(a,b)=sum(2,3)
c=sum(2,3)
# print a,b
# print c[0],c[1]