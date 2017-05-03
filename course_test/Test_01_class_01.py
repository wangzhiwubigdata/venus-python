#coding=utf-8
import numpy

class Employee:
   """所有员工的基类
   哈哈
   """
   empCount = 0



   def __init__(self, name, salary,age):
      self.name = name
      self.salary = salary
      self.age = age

   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary



# emp01 = Employee("zhangsan",100000,18)
# print emp01.name
# print emp01.salary
# emp01.displayCount()
# emp01.displayEmployee()
emp01 = Employee("zhangsan",100000,18)
del emp01.age
# print emp01.age
attr = getattr(emp01,'age',None)
print attr


print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__
