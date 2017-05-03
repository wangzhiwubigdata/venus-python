#coding=utf-8

def funca01():
    print 'in module a... funca01...'


def funca02():
    print 'in module a... funca02...'


##函数名加下划线，别的地方使用import * 导入时，该函数默认不会导入
def _funca03():
    print 'in module a... funca03...'