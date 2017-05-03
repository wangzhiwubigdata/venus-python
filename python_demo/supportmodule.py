# coding=utf-8

#导入模块
import python_demo.support
# 使用导入的模块中的函数
python_demo.support.print_func("Zara")

#------------------------------------------------
#或者
from python_demo.support import print_func

print_func("Zara")


###从任意路径引入
import sys
import os

print sys.path
workpath = os.path.dirname(os.path.abspath(sys.argv[0]))
sys.path.insert(0, os.path.join(workpath, 'x:\\other'))
print sys.path
import othermodule
print othermodule.sum(1,2)