#!/usr/bin/python
# -*- coding: UTF-8 -*-

TRUE = 1
FALSE = 0
def sq(x):
    return x * x
print "less than 50, this will stop!"
again = 1
while again:
    num = int(raw_input('enter your word\n'))
    print '结果为 %d' % (sq(num))
    if num >= 50:
        again = TRUE
    else:
        again = FALSE
