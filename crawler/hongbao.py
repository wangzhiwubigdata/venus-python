
import random
def weixin_divide_hongbao(money, n):
    divide_table = [random.randint(1, money) for x in xrange(0, n)]
    sum_ = sum(divide_table)
    return [x*money/sum_ for x in divide_table]
print weixin_divide_hongbao(100,5)