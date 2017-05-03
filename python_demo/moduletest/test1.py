#coding=utf-8
def func1(arg):
    print "in func1: %s" %arg

def func2(arg):
    print "in func2: %s" %arg

def _func3(arg):
    print "in func3: %s" %arg


def func4(arg):
    print "in func4: %s" %arg

import os
a=os.listdir("c:/")
print a
# os.makedirs("c:/pythontest/test")
os.removedirs("c:/pythontest/test")
