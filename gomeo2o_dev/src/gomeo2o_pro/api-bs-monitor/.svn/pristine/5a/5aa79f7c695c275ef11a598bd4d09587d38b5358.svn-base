# vim: fileencoding=utf-8 ts=4 sw=4 sts=4 et

from base import TesterBase, leaders
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class ItemTester(TesterBase):
    def shop_list(self):
        o = self.comm_get_v1('homepageshop/shop_list.json?sortType=1&order=1&longitude=1&latitude=1&')
        return self.ret(o, lambda: o['data']['list'][0]['vshopId'] > -2)

    def get_product_detail(self):
        o = self.comm_get_v1('product/get_product_detail.json?shopId={shopid}&proId={proid}&locId=1&',
                             shopid=self.cfg['shopId'], proid=self.cfg['proId'])
        return self.ret(o, lambda: o['data']['id'] > 0)

    def around_shop_list(self):
        o = self.comm_get_v1('around/around_shop_list.json?longitude=116.461&latitude=39.9581&sortType=3&order=1&')
        return self.ret(o, lambda: True )

    def special_market(self):
        o = self.comm_get_v1('around/special_market.json?type=1&')
        return self.ret(o, lambda: o['data'][0]['marketId'] > 0)

    def careful_choose_list(self):
        o = self.comm_get_v1('carefulChoose/careful_choose_list.json?')
        return self.ret(o, lambda: o['data'][0]['productId'] > 0)


    # v2
    #商品的详细信息(原子接口)
    def get_item_detail_v2(self):
        c, o = self.comm_get_v2('item/item?id={itemId}&integrity=full&', itemId=self.cfg['proId'])
        return self.ret_v2(c, o, lambda: o['data']['id'] == int(self.cfg['proId']))

    #商品的详细信息
    def get_product_detail_v2(self):
        c, o = self.comm_get_v2('combo/item?itemId={itemId}&shopId={shopId}&', itemId=self.cfg['proId'],
                                shopId=self.cfg['shopId'])
        return self.ret_v2(c, o, lambda: o['data']['item']['id'] == int(self.cfg['proId']))

    #获取后台类目的子类目信息
    def back_category_childlist_v2(self):
        c, o = self.comm_get_v2('category/backCategories?parentId={parentId}&', parentId=self.cfg['parentId'])
        return self.ret_v2(c, o, lambda: o['data']['backCategories'][0]['id'] > 0)

    #后台类目(原子接口查询)
    def back_item_search_category_v2(self):
        c, o = self.comm_get_v2('item/category?itemId={itemId}&', itemId=self.cfg['proId'])
        return self.ret_v2(c, o, lambda: o['data']['categoryId'] > 0)

    #获得当前后台类目信息
    def back_category_current_v2(self):
        c, o = self.comm_get_v2('category/backCategory?id={bcId}&', bcId=self.cfg['bcId'])
        return self.ret_v2(c, o, lambda: o['data']['id'] > 0)

    #获得前台类目列表
    def website_category_current_v2(self):
        c, o = self.comm_get_v2('category/frontCategoryTree?rootId={rootId}&', rootId=self.cfg['rootId'])
        return self.ret_v2(c, o, lambda: o['data']['children'] > 0)

    #商品搜索(详情和分类结果)ext
    def item_search_v2(self):
        c, o = self.comm_get_v2('ext/item/searchItems?categoryId={bcId}&keyword={keyword}&sort={sort}&'
                                'order={orderby}&pageNum={pageNum}&pageSize={pageSize}&'
                                'spellcheck={spellcheck}&shopId={shopId}&',
                                bcId=self.cfg['search']['bcId'], keyword=self.cfg['search']['keyword'],
                                sort=self.cfg['search']['sort'], orderby=self.cfg['search']['orderby'],
                                pageNum=self.cfg['search']['pageNum'], pageSize=self.cfg['search']['pageSize'],
                                spellcheck=self.cfg['search']['spellcheck'], shopId=self.cfg['search']['shopId'])
        return self.ret_v2(c, o, lambda: o['data']['items'] > 0)

    #商品搜索(特色市场)ext
    def item_search_special_market_v2(self):
        c, o = self.comm_get_v2('ext/item/searchItemsByCategory?categoryId={bcId}&keyword={keyword}&'
                                'sort={sort}&order={orderby}&longitude={longitude}&latitude={latitude}&'
                                'pageNum={pageNum}&pageSize={pageSize}&', bcId=self.cfg['search']['bcId'],
                                keyword=self.cfg['search']['keyword'], sort=self.cfg['search']['sort'],
                                orderby=self.cfg['search']['orderby'], longitude=self.cfg['search']['longitude'],
                                latitude=self.cfg['search']['latitude'], pageNum=self.cfg['search']['pageNum'],
                                pageSize=self.cfg['search']['pageSize'])
        return self.ret_v2(c, o, lambda: o['data']['items'] > 0)

    #推荐-PC端商品详情页商品推荐接口
    def commend_item_detail_pc_v2(self):
        c, o = self.comm_get_v2('ext/recommendation/items4Pc?itemId={itemId}&shopId={shopId}&'
                                'pageSize={pageSize}&pageNum={pageNum}&',
                                itemId=self.cfg['commend']['itemId'], shopId=self.cfg['commend']['shopId'],
                                pageNum=self.cfg['commend']['pageNum'], pageSize=self.cfg['commend']['pageSize'])
        return self.ret_v2(c, o, lambda: o['data']['items'] > 0)

    #推荐-h5评价完成为你推荐接口
    def commend_evaluation_finish_h5_v2(self):
        c, o = self.comm_get_v2('ext/recommendation/items4EvaluationCompleted?userId={userId}&'
                                'pageSize={pageSize}&',
                                userId=self.cfg['commend']['userId'], pageSize=self.cfg['commend']['pageSize'])
        return self.ret_v2(c, o, lambda: o['data']['items'] > 0)

    # 推荐-商品详情接口用-更多推荐
    def commend_more_v2(self):
        c, o = self.comm_get_v2('ext/recommendation/itemsDetailMore4H5?itemId={itemId}&shopId={shopId}&'
                                'pageSize={pageSize}&pageNum={pageNum}&order={orderby}&'
                                'orderType={orderType}&',
                                itemId=self.cfg['commend']['itemId'], shopId=self.cfg['commend']['shopId'],
                                pageNum=self.cfg['commend']['pageNum'], pageSize=self.cfg['commend']['pageSize'],
                                orderby=self.cfg['commend']['orderby'],
                                orderType=self.cfg['commend']['orderType'])
        return self.ret_v2(c, o, lambda: o['data']['items'] > 0)

    # 推荐-PC端购物车为你推荐
    def commend_shopping_car_pc_v2(self):
        c, o = self.comm_get_v2('ext/recommendation/items4PcShoppingCart?userId={userId}&'
                                'pageSize={pageSize}&',
                                userId=self.cfg['commend']['userId'], pageSize=self.cfg['commend']['pageSize'])
        return self.ret_v2(c, o, lambda: o['data']['items'] > 0)

    # 推荐-h5端商品详情页商品推荐接口
    def commend_item_detail_h5_v2(self):
        c, o = self.comm_get_v2('ext/recommendation/items4H5ItemDetail?itemId={itemId}&shopId={shopId}&'
                                'pageSize={pageSize}&pageNum={pageNum}&',
                                itemId=self.cfg['commend']['itemId'], shopId=self.cfg['commend']['shopId'],
                                pageNum=self.cfg['commend']['pageNum'], pageSize=self.cfg['commend']['pageSize'])
        return self.ret_v2(c, o, lambda: o['data']['items'] > 0)

    # 推荐-PC支付成功为你推荐
    def commend_pay_success_pc_v2(self):
        c, o = self.comm_get_v2('ext/recommendation/items4PcPaymentPage?userId={userId}&'
                                'pageSize={pageSize}&',
                                userId=self.cfg['commend']['userId'], pageSize=self.cfg['commend']['pageSize'])
        return self.ret_v2(c, o, lambda: o['data']['items'] > 0)

    # 推荐-搜索无果时为你推荐
    def commend_search_nothing_v2(self):
        c, o = self.comm_get_v2('ext/recommendation/items4SearchNoResult?userId={userId}&'
                                'pageSize={pageSize}&',
                                userId=self.cfg['commend']['userId'], pageSize=self.cfg['commend']['pageSize'])
        return self.ret_v2(c, o, lambda: o['data']['items'] > 0)

    # 推荐-个人主页界面的为你推荐
    def commend_myself_v2(self):
        c, o = self.comm_get_v2('ext/recommendation/items4PcPersonal?userId={userId}&'
                                'pageSize={pageSize}&',
                                userId=self.cfg['commend']['userId'], pageSize=self.cfg['commend']['pageSize'])
        return self.ret_v2(c, o, lambda: o['data']['items'] > 0)

    # 运费模版查询(原子接口)
    def freight_templates_v2(self):
        c, o = self.comm_get_v2('item/freightTemplates?userId={userId}&',
                                userId=self.cfg['userId'])
        return self.ret_v2(c, o, lambda: o['data'] > 0)

    # 最新优惠ext
    def item_search_preferential_v2(self):
        c, o = self.comm_get_v2('ext/item/preferentialItems?sort={sort}&'
                                'order={orderby}&pageNum={pageNum}&pageSize={pageSize}&',
                                sort=self.cfg['search']['sort'], orderby=self.cfg['search']['orderby'],
                                pageNum=self.cfg['search']['pageNum'], pageSize=self.cfg['search']['pageSize'])
        return self.ret_v2(c, o, lambda: o['data']['items'] > 0)

    # spu查询(原子接口)
    def get_spu_detail_v2(self):
        c, o = self.comm_get_v2('item/spu?id={spuId}&',
                                spuId=self.cfg['spuId'])
        return self.ret_v2(c, o, lambda: o['data'] > 0)

yangjun =      [(u"杨军",   "15718820398"),]
zhaochenyu =   [(u"赵宸宇", "13146609395"),]
shangpengfei = [(u"上鹏飞", "18729903831"),]

item_cases_v1 = [
    ('shop_list',            u'19_首页店铺列表', leaders + yangjun),
    ('around_shop_list',     u'17_商圈店铺列表', leaders),
    ('special_market',       u'15_特色市场', leaders + zhaochenyu),
    ('get_product_detail',   u'29_商品的详细信息', leaders),
    ('careful_choose_list',  u'5_精选列表', leaders + shangpengfei),
]

item_cases_v2 = [
    ('get_item_detail_v2',   u'v2商品的详细信息(原子接口)', leaders),
    ('get_product_detail_v2', u'v2商品的详细信息', leaders),
    ('back_category_childlist_v2', u'v2获取后台类目的子类目信息', leaders),
    ('back_item_search_category_v2', u'v2后台类目(原子接口查询)', leaders),
    ('back_category_current_v2', u'v2获得当前后台类目信息', leaders),
    ('website_category_current_v2', u'v2获得前台类目列表', leaders),
    ('item_search_v2', u'v2商品搜索(详情和分类结果)ext', leaders),
    ('item_search_special_market_v2', u'v2商品搜索(特色市场)ext', leaders),
    ('commend_item_detail_pc_v2', u'v2推荐-PC端商品详情页商品推荐接口', leaders),
    ('commend_evaluation_finish_h5_v2', u'v2推荐-h5评价完成为你推荐接口', leaders),
    ('commend_more_v2', u'v2推荐-商品详情接口用-更多推荐', leaders),
    ('commend_shopping_car_pc_v2', u'v2推荐-PC端购物车为你推荐', leaders),
    ('commend_item_detail_h5_v2', u'v2推荐-h5端商品详情页商品推荐接口', leaders),
    ('commend_pay_success_pc_v2', u'v2推荐-PC支付成功为你推荐', leaders),
    ('commend_search_nothing_v2', u'v2推荐-搜索无果时为你推荐', leaders),
    ('commend_myself_v2', u'v2推荐-个人主页界面的为你推荐', leaders),
    ('freight_templates_v2', u'v2运费模版查询(原子接口)', leaders),
    ('item_search_preferential_v2', u'v2最新优惠ext', leaders),
    ('get_spu_detail_v2', u'v2spu查询(原子接口)', leaders),
]