#!/usr/bin/python
# -*- coding: UTF-8 -*-
import collections
import string

L = [1, 2, 3, 4, 5]
print len(L)
for i in range(1, 3):
    print i
print "--------------------"
for m in range(1, len(L)):
    print m


class Person(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_grade(self):
        if self.__score >= 80:
            return u"A->优秀"
        elif self.__score >= 60:
            return u"B->及格"
        else:
            return u"C-> 不及格"

p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)

print p1.get_grade()
print p2.get_grade()
print p3.get_grade()

L = collections.Counter(string.ascii_lowercase*100);
print L
K = "".join([chr(i) for i in range(ord("a"),ord("z")+1)])
print K
