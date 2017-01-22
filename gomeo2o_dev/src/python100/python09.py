#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
from math import sqrt
from sys import stdout

myD = {1: 'a', 2: 'b'}
for key, value in myD.items():
    print key, value
    time.sleep(1)

h = 0
leap = 1
for m in range(101, 201):
    k = int (sqrt(m+1))
    for i in range(2, k+1):
        if m % i == 0:
            leap = 0
            break
    if leap == 1:
        print '%-4d' % m
        h +=1
        if h % 10 == 0:
            print ''
    leap = 1

print 'the total is %d' % h

