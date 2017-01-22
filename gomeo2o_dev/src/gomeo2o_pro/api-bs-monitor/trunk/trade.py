# vim: fileencoding=utf-8 ts=4 sw=4 sts=4 et

from base import TesterBase, leaders
import sys
import urllib
reload(sys)
sys.setdefaultencoding('utf-8')


class TradeTester(TesterBase):
    def get_home_redpack_list(self):
        o = self.comm_get_v1('cheap/get_home_redpack_list.json?')
        return self.ret(o, lambda: len(o['data'][0]['shopName']) > 0)

    def get_more_redpacket_list(self):
        o = self.comm_get_v1('cheap/get_more_redpacket_list.json?')
        return self.ret(o, lambda: True)

    def new_preferential(self):
        o = self.comm_get_v1('carefulChoose/new_preferential.json?')
        return self.ret(o, lambda: o['data'][0]['vShopId'] > 0)

    def u_query_order_count(self):
        o = self.user_get_v1('user/query_order_count.json?')
        return self.ret(o, lambda: o['data']['pendPayment'] >= 0)

    def u_get_shopcart_list(self):
        o = self.user_get_v1('cart/get_shopcart_list.json?')
        return self.ret(o, lambda: True)

    def u_nocomment_product_list(self):
        o = self.user_get_v1('order/nocomment_product_list.json?')
        return self.ret(o, lambda: True)

    def u_comment_product_list(self):
        o = self.user_get_v1('order/comment_product_list.json?')
        return self.ret(o, lambda: True)

    def u_order_list(self):
        o = self.user_get_v1('order/order_list.json?orderStatus=1&hasComment=1&shopType=1&referenceId=1&')
        return self.ret(o, lambda: True)

    def u_get_after_sale_list(self):
        o = self.user_get_v1('manage/order/get_after_sale_list.json?shopType=1&referenceId=1&')
        return self.ret(o, lambda: True)

    def u_check_logistics(self):
        o = self.user_get_v1('order/check_logistics.json?orderId=6865&shopType=1&type=1&')
        return self.ret(o, lambda: True)

    def u_account_detail_list(self):
        o = self.user_get_v1('account/account_detail_list.json?')
        return self.ret(o, lambda: True)

    def u_account_detail(self):
        o = self.user_get_v1('account/account_detail.json?detailId=1021&type=1&')
        return self.ret(o, lambda: True)

    def u_nocomment_product_detail(self):
        o = self.user_get_v1('order/nocomment_product_detail.json?orderItemId=7687&')
        return self.ret(o, lambda: True)

    def u_order_detail(self):
        o = self.user_get_v1('order/order_detail.json?orderId=6865&shopType=1&')
        return self.ret(o, lambda: True)

    def u_get_logistic_list(self):
        o = self.user_get_v1('order/get_logistic_list.json?logName=1&')
        return self.ret(o, lambda: True)

    def u_query_vshop_order_count(self):
        o = self.user_get_v1('user/query_vshop_order_count.json?vshopId=1&')
        return self.ret(o, lambda: True)

    def u_redpacket_list(self):
        o = self.user_get_v1('account/redpacket_list.json?state=1&')
        return self.ret(o, lambda: True)

    def u_score_info(self):
        o = self.user_get_v1('account/score_info.json?')
        return self.ret(o, lambda: True)

    def u_score_list(self):
        o = self.user_get_v1('account/score_list.json?scoreType=0&')
        return self.ret(o, lambda: True)

    def u_score_explain(self):
        o = self.user_get_v1('account/score_explain.json?')
        return self.ret(o, lambda: True)

    def u_add_shopcart(self):
        o = self.user_get_v1('cart/add_shopcart.json?shopId=411&kId=1&skuId=1323&proNum=1&')
        return self.ret(o, lambda: True)

    def u_del_shopcart_product(self):
        o = self.user_get_v1('cart/del_shopcart_product.json?deleteIds=' + urllib.quote("1323@1#411") + '&')
        return self.ret(o, lambda: True)

    # v2
    def v2_shoppingCart(self):
        c, o = self.user_get_v2('trade/shoppingCart?')
        return self.ret_v2(c, o, lambda: type(o['data']['shopingCartItems']) == type([]))

    def v2_personalOrderStastics(self):
        c, o = self.user_get_v2('trade/personalOrderStastics?userType=1&')
        return self.ret_v2(c, o, lambda: type(o['data']['pendPayment']) == type(1))

    def v2_mshopOrderStastics(self):
        c, o = self.user_get_v2('trade/mshopOrderStastics?mshopId=13213&')
        return self.ret_v2(c, o, lambda: type(o['data']['pendPayment']) == type(1))

    def v2_buyerOrders(self):
        c, o = self.user_get_v2('trade/buyerOrders?orderStatus=1&hasComment=0&pageSize=1&')
        return self.ret_v2(c, o, lambda: True)

    def v2_sellerOrders(self):
        c, o = self.user_get_v2('trade/sellerOrders?orderStatus=1&hasComment=0&shopType=1&pageSize=1&')
        return self.ret_v2(c, o, lambda: True)

    def v2_afterSalesOrders(self):
        c, o = self.user_get_v2('trade/afterSalesOrders?&pageSize=1&')
        return self.ret_v2(c, o, lambda: True)

    def v2_sellerAfterSalesOrders(self):
        c, o = self.user_get_v2('trade/sellerAfterSalesOrders?&pageSize=1&shopType=1&')
        return self.ret_v2(c, o, lambda: True)

    def v2_logisticsVendors(self):
        c, o = self.user_get_v2('trade/logisticsVendors?pageSize=1&')
        return self.ret_v2(c, o, lambda: True)

    def v2_orderLogistics(self):
        c, o = self.user_get_v2('trade/orderLogistics?orderId=6865&shopType=1&type=1&')
        return self.ret_v2(c, o, lambda: True)

    def v2_itemCommentCount(self):
        c, o = self.user_get_v2('trade/itemCommentCount?&itemId=1&')
        return self.ret_v2(c, o, lambda: True)

    # def v2_buyerOrderDetail(self):
    # c, o = self.user_get_v2('trade/shoppingCart?')
    # return self.ret_v2(c, o, lambda: True)

    # def v2_sellerOrderDetail(self):
    # c, o = self.user_get_v2('trade/shoppingCart?')
    # return self.ret_v2(c, o, lambda: True)

    #def v2_afterSalesOrderDetail(self):
    #    c, o = self.user_get_v2('trade/shoppingCart?')
    #    return self.ret_v2(c, o, lambda: type(o['data']['shopingCartItems']) == type([]))

    #def v2_sellerAfterSalesOrderDetail(self):
     #   c, o = self.user_get_v2('trade/shoppingCart?')
    #    return self.ret_v2(c, o, lambda: type(o['data']['shopingCartItems']) == type([]))

    def v2_shopPromotionMark(self):
        c, o = self.user_get_v2('trade/shopPromotionMark?&shopId=1&')
        return self.ret_v2(c, o, lambda: True)

    def v2_boughtItems(self):
        c, o = self.user_get_v2('trade/boughtItems?pageSize=1&')
        return self.ret_v2(c, o, lambda: True)

    def v2_commentedItems(self):
        c, o = self.user_get_v2('trade/commentedItems?shopType=1&pageSize=1&')
        return self.ret_v2(c, o, lambda: True)

    def v2_shoppingCartItemQuantity(self):
        c, o = self.user_get_v2('trade/shoppingCartItemQuantity?')
        return self.ret_v2(c, o, lambda: True)

    def v2_ext_itemComments(self):
        c, o = self.user_get_v2('ext/trade/itemComments?itemId=1&pageSize=1&')
        return self.ret_v2(c, o, lambda: True)
    # A1.我的账户首页
    def v2_account_assets(self):
        c, o = self.user_get_v2('account/accountAssets?')
        return self.ret_v2(c, o, lambda: o['data']['gomeMoneyAmount'] >= 0)
    # A2.收支明细列表
    def v2_balance_details(self):
        c, o = self.user_get_v2('account/balanceDetails?pageSize=10&')
        return self.ret_v2(c, o, lambda: len(o['data']['balanceDetails']) >= 0)
    # A3.收支明细详情
    # def V2_balance_detail(self):
    #     c, o = self.user_get_v2('account/balanceDetail?id=1&type=1&')
    #     print o
    #     return self.ret_v2(c, o, lambda: len(o['data']['message']) > 0)
    # A4.用户是否绑定过银行卡
    def v2_bank_card_bound(self):
        c, o = self.user_get_v2('account/bankCardBound?')
        return self.ret_v2(c, o, lambda: len(str(o['data']['isBound'])) > 0)
    # A6.校验支付密码是否存在
    def v2_payment_password_existence(self):
        c, o = self.user_get_v2('account/paymentPasswordExistence?')
        return self.ret_v2(c, o, lambda: len(str(o['data']['isExist'])) > 0)
    # A9.提现卡列表
    def v2_withdrawal_bank_cards(self):
        c, o = self.user_get_v2('account/withdrawalBankCards?')
        return self.ret_v2(c, o, lambda: len(o['data']['withdrawalBankCards']) >= 0)
    # A10.获取支持银行列表
    def v2_supported_banks(self):
        c, o = self.comm_get_v2('account/supportedBanks?')
        return self.ret_v2(c, o, lambda: len(o['data']['supportedBanks']) >= 0)
    # # A11.获取用户开户行姓名和身份证号码
    # def V2_bankcard_account_info(self):
    #     c, o = self.user_get_v2('account/bankcardAccountInfo?')
    #     return self.ret_v2(c, o, lambda: len(o['data']['bankcardAccountInfo']) >= 0)
    # A14.用户资产信息 combo
    def v2_user_assets_info(self):
        c, o = self.user_get_v2('combo/userAssetsInfo?')
        return self.ret_v2(c, o, lambda: o['data']['gomeMoneyAmount'] >= 0)
    # A15.用户银行卡个数
    def v2_user_bank_card_number(self):
        c, o = self.user_get_v2('account/userBankCardNumber?')
        return self.ret_v2(c, o, lambda: o['data']['count'] >= 0)
    # # A16.短信验证码
    # def V2_SMS_verification_code(self):
    #     c, o = self.user_get_v2('account/SMSVerificationCode?')
    #     return self.ret_v2(c, o, lambda: len(o['data']['verifyToken']) >= 0)


miaomiao =     [(u"苗苗",   "18210723398"),]
wangzhenpeng =     [(u"王振鹏",   "18510590464"),]
fengxin =     [(u"冯鑫",   "18610905809"),]

trade_cases_v1 = [
    ('get_home_redpack_list',    u'21_首页红包', leaders + miaomiao),
    ('get_more_redpacket_list',  u'24_更多抢红包', leaders + miaomiao),
    ('new_preferential',         u'3_最新优惠', leaders + miaomiao),
    ('u_query_order_count',      u'608_获取用户各订单状态下的订单数量', leaders + miaomiao),
    ('u_get_shopcart_list',      u'*85_购物车列表', leaders + miaomiao),
    ('u_nocomment_product_list', u'*163_待评价商品列表', leaders + miaomiao),
    ('u_comment_product_list',   u'*164_已评价商品列表', leaders + miaomiao),
    ('u_order_list',             u'*151_我的订单列表', leaders + miaomiao),
    ('u_get_after_sale_list',    u'*210_退款/退货/换货单列表', leaders + miaomiao),
    ('u_check_logistics', u'*156_查看物流', leaders + miaomiao),
    ('u_account_detail_list', u'*167_查看收支明细列表', leaders + miaomiao),
    ('u_account_detail', u'*168_查看收支明细详情', leaders + miaomiao),
    ('u_nocomment_product_detail', u'*313_待评价商品详情', leaders + miaomiao),
    # ('u_order_detail', u'*158_订单详情', leaders + tangfeng),
    ('u_get_logistic_list', u'*314_获取物流公司列表', leaders + wangzhenpeng),
    ('u_query_vshop_order_count', u'*627_获取美店用户各订单状态下的订单数量', leaders + miaomiao),
    ('u_redpacket_list', u'*173_我的红包列表', leaders + miaomiao),
    ('u_score_info', u'*175_我的积分信息', leaders + miaomiao),
    ('u_score_list', u'*176_我的积分列表', leaders + miaomiao),
    ('u_score_explain', u'*177_我的积分说明', leaders + miaomiao),
    ('u_add_shopcart', u'*87_加入购物车', leaders + miaomiao),
    ('u_del_shopcart_product', u'*89_删除购物车', leaders + miaomiao),
]

trade_cases_v2 = [
    ('v2_shoppingCart',      u'*T1_购物车列表', leaders + miaomiao),
    ('v2_personalOrderStastics', u'*T20_获取用户各订单状态下订单数量', leaders + miaomiao),
    ('v2_mshopOrderStastics', u'*T21_美店获取各订单状态下的订单数量', leaders + miaomiao),
    ('v2_buyerOrders', u'*T16_买家订单列表', leaders + wangzhenpeng),
    ('v2_sellerOrders', u'*T17_卖家订单列表', leaders + wangzhenpeng),
    #('v2_buyerOrderDetail', u'*T18_买家订单详情', leaders + wangzhenpeng),
    #('v2_sellerOrderDetail', u'*T19_卖家订单详情', leaders + wangzhenpeng),
    ('v2_afterSalesOrders', u'*T22_买家售后单列表', leaders + wangzhenpeng),
    ('v2_sellerAfterSalesOrders', u'*T23_卖家售后单列表', leaders + wangzhenpeng),
    #('v2_afterSalesOrderDetail', u'*T24_买家售后单详情', leaders + wangzhenpeng),
    #('v2_sellerAfterSalesOrderDetail', u'*T25_卖家售后单详情', leaders + wangzhenpeng),
    ('v2_logisticsVendors', u'*T9_获取物流公司列表', leaders + wangzhenpeng),
    ('v2_orderLogistics', u'*T11_订单物流信息', leaders + wangzhenpeng),
    ('v2_itemCommentCount', u'*T34_商品评论数', leaders + wangzhenpeng),

    ('v2_shopPromotionMark', u'*T36_店铺是否有优惠券、直降', leaders + wangzhenpeng),
    ('v2_boughtItems', u'*T38_我要晒单列表', leaders + wangzhenpeng),
    ('v2_commentedItems', u'*T39_已评价的商品列表', leaders + wangzhenpeng),
    ('v2_ext_itemComments', u'*T40_商品评价列表 ext', leaders + wangzhenpeng),
    ('v2_shoppingCartItemQuantity', u'*T42_购物车商品总数量', leaders + wangzhenpeng),
    ('v2_account_assets', u'A01.我的账户首页', leaders + wangzhenpeng),
    ('v2_balance_details', u'A02.收支明细列表', leaders + wangzhenpeng),
    # ('v2_balance_detail', u'A03.收支明细详情', leaders + wangzhenpeng),
    ('v2_bank_card_bound', u'A04.用户是否绑定过银行卡', leaders + wangzhenpeng),
    ('v2_payment_password_existence', u'A06.校验支付密码是否存在', leaders + wangzhenpeng),
    ('v2_withdrawal_bank_cards', u'A09.提现卡列表', leaders + wangzhenpeng),
    ('v2_supported_banks', u'A10.获取支持银行列表', leaders + wangzhenpeng),
    # ('V2_bankcard_account_info', u'A11.获取用户开户行姓名和身份证号码', leaders + wangzhenpeng),
    ('v2_user_assets_info', u'A14.用户资产信息 combo', leaders + wangzhenpeng),
    ('v2_user_bank_card_number', u'A15.用户银行卡个数', leaders + wangzhenpeng),
    # ('V2_SMS_verification_code', u'A16.短信验证码', leaders + wangzhenpeng),

    #('get_home_redpack_list', u'21_首页红包', leaders + miaomiao),
    #('get_more_redpacket_list', u'24_更多抢红包', leaders + miaomiao),
    #('new_preferential', u'3_最新优惠', leaders + miaomiao),

    #('u_get_shopcart_list', u'*85_购物车列表', leaders + wangzhenpeng),
    #('u_nocomment_product_list', u'*163_待评价商品列表', leaders + wangzhenpeng),
    #('u_comment_product_list', u'*164_已评价商品列表', leaders + wangzhenpeng),

    #('u_check_logistics', u'*156_查看物流', leaders + wangzhenpeng),
    #('u_account_detail_list', u'*167_查看收支明细列表', leaders + wangzhenpeng),
    #('u_account_detail', u'*168_查看收支明细详情', leaders + wangzhenpeng),
    #('u_nocomment_product_detail', u'*313_待评价商品详情', leaders + wangzhenpeng),
    # ('u_order_detail', u'*158_订单详情', leaders + wangzhenpeng),
    #('u_get_logistic_list', u'*314_获取物流公司列表', leaders + wangzhenpeng),

    #('u_redpacket_list', u'*173_我的红包列表', leaders + wangzhenpeng),
    #('u_score_info', u'*175_我的积分信息', leaders + wangzhenpeng),
    #('u_score_list', u'*176_我的积分列表', leaders + wangzhenpeng),
    #('u_score_explain', u'*177_我的积分说明', leaders + wangzhenpeng),
    #('u_add_shopcart', u'*87_加入购物车', leaders + wangzhenpeng),
    #('u_del_shopcart_product', u'*89_删除购物车', leaders + wangzhenpeng),
]