#!/usr/bin/python
# -*- coding: UTF-8 -*-

def outfunc(func,x,y):
    c=func(x,y)
    print(c)

outfunc(lambda x,y:x+y,1,2)


