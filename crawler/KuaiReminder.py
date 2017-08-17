# encoding: utf-8
import json
import easygui
import requests
import time

url = 'http://yfcp807.com/tools/ssc_ajax.ashx?A=GetLotteryOpen&S=yfvip&U=xxxx'


header = {
    'Host': 'yfcp807.com',
    'Origin': 'http://yfcp807.com',
    'Referer': 'http://yfcp807.com/lottery/K3/1407',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie':'route=134217aa4e8e12a08665fba45d9ec79f; token=94b04c7bfa75e1886efde9beaee135e4; random=2580; C_SessionId=e55fa638-1bcc-4d49-aca3-3fd4cabb83a5',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

postdata = {
    'A': 'GetLotteryOpen',
    'S': 'yfvip',
    'U':'xxxx',
    'Action' : 'GetLotteryOpen',
    'LotteryCode': 1407,
    'IssueNo' : 0,
    'DataNum' : 6,
    'SourceName' : 'PC'
}

def log_in():
    pass

def get_data():
    addslist = []
    response = requests.post(url,postdata,headers=header)
    html = response.text
    jsons = json.loads(html)
    ar = jsons.get('BackData')
    for key in ar:
        sv = key['LotteryOpen'].split(',')
        adds = sum(int(a) for a in sv)
        #adds = adds // 11
        print adds
        addslist.append(adds)
    addslist = [1,1,1,1,1,1]
    print '最近6次的值为： ' + str(addslist)
    return addslist

def should_alert_u(list):
    big , small , jishu , oushu = [],[],[],[]
    big = (i >10 for i in list)
    print (i for i in big)
    small = (i<10 for i in list)
    print small
    jishu = (i%2==1 for i in list)
    oushu = (i%2==0 for i in list)
    if big:
        if len(big)==len(list):
            return True
    if small:
        if len(small) == len(list):
            return True
    if jishu:
        if len(jishu) == len(list):
            return True
    if oushu:
        if len(oushu) == len(list):
            return True
    return False

def auto_bet(name, money):
    pass

if __name__ == '__main__':
    # account = 'xxxxx'
    # pwd = 'xxxxxx'
    # money = 5
    # while 1==1:
    #     l = get_data()
    #     time.sleep(30)
    #     if should_alert_u(l):
    #         print l
    #         #auto_bet(account,money)
    #         easygui.msgbox(u'6连大龙出现了!', u'注意捡钱!')

    should_alert_u(get_data())



