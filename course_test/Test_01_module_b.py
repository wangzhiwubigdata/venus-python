#coding=utf-8

import Test_01_module_a
Test_01_module_a.print_func("haha")


from Test_01_module_a import  *
print_func("heihei")


from Test_01_module_a import print_func as pf
pf("xixi")

print 'in module b,' ,__name__
