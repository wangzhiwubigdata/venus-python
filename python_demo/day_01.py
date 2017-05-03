# coding=utf-8
def add(num1, num2):
    '''
    第一个函数
    :param num1:
    :param num2:
    :return:
    '''
    return num1 + num2


"第一个函数调用"
"""
print("哈哈")
print(add(1,2))


# print(add.__code___)
print(add.__doc__)
print(add.__sizeof__())

"""


def func1(i):
    if i < 100:
        return i + func1(i + 1)
    return i


import threadtest


