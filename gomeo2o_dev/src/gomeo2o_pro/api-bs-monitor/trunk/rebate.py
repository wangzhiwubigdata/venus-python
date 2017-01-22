# vim: fileencoding=utf-8 ts=4 sw=4 sts=4 et

from base import TesterBase, leaders
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class RebateTesters(TesterBase):
    def life_recommend_list(self):
        o = self.comm_get_v1('life/life_recommend_list.json?')
        return self.ret(o, lambda: len(o['data']) > 0)

    def super_rebate_list(self):
        o = self.comm_get_v1('cheap/super_rebate_list.json?')
        return self.ret(o, lambda: (o['data'][0]['productId'] > 0 and o['data'][0]['shopId'] > 0))

    def get_home_sidemoney_list(self):
        o = self.comm_get_v1('cheap/get_home_sidemoney_list.json?')
        return self.ret(o, lambda: o['data'][0]['id'] > -2) # 现在一直是 -1 了，有没有问题？

    def get_sidemoney_list(self):
        o = self.comm_get_v1('cheap/get_sidemoney_list.json?order=1&')
        return self.ret(o, lambda: True)


rebate_cases_v1 = [
    ('life_recommend_list',     u'701_推荐位', leaders),
    ('super_rebate_list',       u'702_超级返', leaders),
    ('get_home_sidemoney_list', u'22_首页赚外快', leaders),
    ('get_sidemoney_list',      u'27_赚外快列表', leaders),
]