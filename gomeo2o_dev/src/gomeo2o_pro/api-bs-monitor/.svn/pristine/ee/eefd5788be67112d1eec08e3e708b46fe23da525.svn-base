# vim: fileencoding=utf-8 ts=4 sw=4 sts=4 et

import json
import urllib
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

requests.packages.urllib3.disable_warnings()

COMM_QUERY_PLUS = 'userId=0&clientOs={clientos}&clientOsVersion=4.3&appType=1&appVersion=1.0&phoneType=GomeplusBSMonitor&' \
                  'ip=192.12.33.22&mac=ac+as+23+3d&netType=4G&devId=IPhone1234567890&' \
                  'otherDevInfo=someInfo&loginToken=&pageNum=1&numPerPage=10&lastRecordId=1000001'
USER_QUERY_PLUS = 'userId={userid}&clientOs={clientos}&clientOsVersion=4.3&appType=1&appVersion=1.0&' \
                  'phoneType=GomeplusBSMonitor&ip=192.12.33.22&mac=ac+as+23+3d&netType=4G&devId=IPhone1234567890&' \
                  'otherDevInfo=someInfo&loginToken={token}&pageNum=1&numPerPage=10&lastRecordId=1000001'
V2_PARAM = "&device=IOS/9.3.2/iPhone/1&app=00{clientos}/bs&appVersion=1.0.5"
HEADERS = {'content-type': 'application/json;charset=utf-8', 'Accept':'application/json'}


def dump(o, asc=False):
    print json.dumps(o, indent=4, sort_keys=True, ensure_ascii=asc, encoding='utf-8')


class Requester:
    def __init__(self, host=None, user=None, pwd=None, clientos=None):
        self.verify = (host is None)
        self.host = host or 'api-bs.gomeplus.com'
        self.user = user
        self.pwd = pwd
        self.param = V2_PARAM.format(clientos=clientos);
        self.comm_query_plus = COMM_QUERY_PLUS.format(clientos=clientos)
        self.user_query_plus0 = USER_QUERY_PLUS.format(clientos=clientos, userid='{userid}', token='{token}')
        self.user_query_plus = None
        self.timeout = 5

    def url(self, base, **kwargs):
        schema = "https"
        if ":" in self.host:
            schema = "http"
        return '{schema}://{host}/{base}'.format(schema=schema, host=self.host, base=base).format(**kwargs)

    def url_v1(self, base, **kwargs):
        return self.url('api/' + base, **kwargs)

    def url_v2(self, base, **kwargs):
        return self.url('v2/' + base, **kwargs)

    def get(self, base, **kwargs):
        return requests.get(self.url_v1(base, **kwargs), verify=self.verify, timeout=self.timeout)

    def comm_get_v1(self, base, **kwargs):
        r = requests.get(self.url_v1(base, **kwargs) + self.comm_query_plus, verify=self.verify, timeout=self.timeout)
        return r.json()

    def user_get_v1(self, base, **kwargs):
        r = requests.get(self.url_v1(base, **kwargs) + self.user_query_plus, verify=self.verify, timeout=self.timeout)
        return r.json()

    def login(self):
        ep = self.get('dsp/get_encrypt_password.json?password={pwd}', pwd=self.pwd).text

        o = self.comm_get_v1('user/login.json?loginName={user}&password={ep}&verifyCode=1&', user=self.user,
                             ep=urllib.quote(ep))

        dump(o)
        self.user_query_plus = self.user_query_plus0.format(userid=o['data']['userId'], token=o['data']['token'])
        return o

    def comm_get_v2(self, base, **kwargs):
        r = requests.get(self.url_v2(base, **kwargs) + self.comm_query_plus + self.param, verify=self.verify, timeout=self.timeout)
        return r.status_code, r.json()

    def user_get_v2(self, base, **kwargs):
        r = requests.get(self.url_v2(base, **kwargs) + self.user_query_plus + self.param, verify=self.verify, timeout=self.timeout)
        return r.status_code, r.json()

    def login_v2(self):
        r = requests.post(self.url_v2('user/login?') + self.comm_query_plus + self.param,
                          verify=self.verify,
                          headers={'Content-Type': 'application/json'},
                          data=json.dumps({'loginName': self.user, 'password': self.pwd}))
        c, o = r.status_code, r.json()
        dump(o)
        self.user_query_plus = self.user_query_plus0.format(userid=o['data']['user']['id'], token=o['data']['loginToken'])
        return c, o


class TesterBase:
    def __init__(self, test_cfg):
        self.cfg = test_cfg
        req = Requester(test_cfg['host'], test_cfg['user'], test_cfg['pwd'], test_cfg['clientos'])
        self.req = req
        self.env = test_cfg['name']
        self.sms_send = test_cfg['sms_send']
        self.comm_get_v1 = req.comm_get_v1
        self.user_get_v1 = req.user_get_v1
        self.comm_get_v2 = req.comm_get_v2
        self.user_get_v2 = req.user_get_v2
        self.login_user_id = 0

    def login(self):
        o = self.req.login()
        self.login_user_id = o['data']['userId']
        return self.ret(o, lambda: True)

    def login_v2(self):
        c, o = self.req.login_v2()
        self.login_user_id = o['data']['user']['id']
        return self.ret_v2(c, o, lambda: True)

    def ret(self, o, expr):
        success = False
        try:
            success = o['success'] and expr()
        except Exception as e:
            pass

        if not success:
            dump(o)

        return success

    def ret_v2(self, c, o, expr):
        success = False
        try:
            success = (c == 200) and expr()
        except Exception as e:
            pass

        if not success:
            dump(o)

        return success


leaders = [
    (u"赵青",   "18611864109"),
    (u"王云鹏", "13711719724"),
    (u"张羽翼", "18610503003"),
    (u"李佳欢", "13811664749"),
    (u"刘太明", "13426010572"),
    (u"尚升方", "18701689171"),
    (u"贾彦伟", "18612519552"),
    (u"单杰",   "18071116226"),
]
