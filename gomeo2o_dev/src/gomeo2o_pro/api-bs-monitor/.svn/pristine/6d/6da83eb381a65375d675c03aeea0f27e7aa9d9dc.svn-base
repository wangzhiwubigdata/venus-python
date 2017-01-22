#!/usr/bin/env python
# vim: fileencoding=utf-8 ts=4 sw=4 sts=4 et

import datetime
import sys
import traceback
import urllib
import optparse

from base import Requester
from trade import TradeTester, trade_cases_v1, trade_cases_v2
from item import ItemTester, item_cases_v1, item_cases_v2
from rebate import RebateTesters, rebate_cases_v1
from social import SocialTester, social_cases_v1
from user import UserTester, user_cases_v1, user_cases_v2

reload(sys)
sys.setdefaultencoding('utf-8')


class Tester (UserTester, RebateTesters, TradeTester, ItemTester, SocialTester):
    pass


cases_v1 = user_cases_v1 + rebate_cases_v1 + trade_cases_v1 + item_cases_v1 + social_cases_v1
#cases_v2 = user_cases_v2 + trade_cases_v2 + item_cases_v2
cases_v2 = item_cases_v2

def sms_send(num, txt):
    req = Requester(host='api.bs.dev.gomeplus.com', user='servertest', pwd='gome1234567')
    encoded_txt = urllib.quote(txt.encode('utf-8'))
    # req.get('innerwork/send_warning_sms.json?phone={num}&content={txt}', host='api.bs.dev.gomeplus.com',
    # num=num, txt=encoded_txt)


def dummy_send(num, txt):
    pass


def do_test(tester, version):
    print ''
    d = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    fails = 0
    print u'{date} {env}环境测试开始'.format(env=tester.env, date=d)
    test_cases = cases_v1
    if version == 'v2':
        test_cases = cases_v2
    elif version == 'v1':
        test_cases = cases_v1
    else:
        test_cases = cases_v2 + cases_v1

    for case in test_cases:
        try:
            r = getattr(tester, case[0])()
        except:
            print traceback.format_exc()
            r = 0
        if r == 1:
            print case[1], ' OK'
            continue
        fails += 1
        txt = u'{date} 接口【{info}】调用失败，请检查。' .format(date=d, info=case[1])
        cont = (len(case) <= 3)
        if len(case) > 3:
            txt += case[3]
        for user in case[2]:
            print user[1], txt
            tester.sms_send(user[1], txt)
        if not cont:
            break

    print ''
    print u'{env}环境测试完毕，{fails} 项目失败。'.format(env=tester.env, fails=fails)
    return fails

test_configs = {
    'pro': {
        'spuId': '101',
        'clientos': 3,
        'user': 'bs_server',
        'pwd': 'gome1234567',
        'host': None,
        'userId': '1425',
        'imId': 'b_1425',
        'gimid': 'b_2937',
        'gid': '141627228529098768',
        'topicId': '56cd8cdd799d0d127473ed22',
        'shopId': '141',
        'proId': '489',
        'vshopId': '571',
        'addrId': '6343',
        'sms_send': sms_send,
        'name': '生产',
        'parentId': '1',
        'bcId': '100',
        'rootId': '0',
        'search':{
            'bcId':'1',
            'keyword': '',
            'sort': '',
            'orderby': '',
            'pageNum': '1',
            'pageSize': '10',
            'spellcheck': '',
            'shopId': '-1',
            'longitude': '',
            'latitude': '',
        },
        'commend': {
            'itemId': '1',
            'shopId': '1',
            'userId': '1',
            'pageNum': '1',
            'pageSize': '10',
            'orderby': '0',
            'orderType': '1',
        },
    },
    'pre': {
        'spuId': '100',
        'clientos': 3,
        'user': 'servertest',
        'pwd': 'gome1234567',
        'host': 'api-bs-pre.gomeplus.com',
        'userId': '832',
        'imId': 'b_832',
        'gimid': 'b_578',
        'gid': '142584646859751472',
        'topicId': '',
        'shopId': '141',
        'proId': '489',
        'vshopId': '571',
        'sms_send': dummy_send,
        'name': '预生产',
        'parentId': '1',
        'bcId': '1',
        'rootId': '0',
        'search': {
            'bcId': '1',
            'keyword': '',
            'sort': '',
            'orderby': '',
            'pageNum': '1',
            'pageSize': '10',
            'spellcheck': '',
            'shopId': '-1',
            'longitude': '',
            'latitude': '',
        },
    },
    'dev': {
        'spuId': '100',
        'clientos': 3,
        'user': 'servertest',
        'pwd': 'gome1234567',
        'host': 'api.bs.dev.gomeplus.com',
        'userId': '583',
        'imId': 'b_583',
        'gimid': 'b_583',
        'gid': '1451381645504927',
        'topicId': '',
        'shopId': '14',
        'proId': '120',
        'vshopId': '571',
        'sms_send': dummy_send,
        'name': '开发',
        'parentId': '1',
        'bcId': '1',
        'rootId': '0',
        'search': {
            'bcId': '1',
            'keyword': '',
            'sort': '',
            'orderby': '',
            'pageNum': '1',
            'pageSize': '10',
            'spellcheck': '',
            'shopId': '-1',
            'longitude': '',
            'latitude': '',
        },
    }
}

def parse_args(args=None):
    global test_configs
    args = args or sys.argv[1:]

    parser = optparse.OptionParser("usage: %prog [options] args")
    parser.set_defaults(env="pro", version="")
    parser.add_option("-e", "--env", dest="env",
                        help="set enviroment, default pro")
    parser.add_option("-H", "--host", dest="host",
                        help="set host")
    parser.add_option("-v", "--version", dest="version",
                        help="set version, default \"\"")
    options, _ = parser.parse_args(args)

    if options.env not in test_configs:
        print "there is no `%s' enviroment" \
            " config" % options.env
        sys.exit(127)
    host = options.host or test_configs[options.env].get("host")
    if options.version not in ["v1", "v2", ""]:
        print "invalid `version'"
        sys.exit(127)

    print "host: %s" % host
    cfg = test_configs[options.env]
    cfg["host"] = host
    return cfg, options.version

if __name__ == '__main__':
    cfg, version = parse_args()
    #sys.exit(do_test(Tester(cfg), version))
    sys.exit(do_test(Tester(cfg), 'v2'))

