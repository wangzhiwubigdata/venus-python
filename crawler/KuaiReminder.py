# encoding: utf-8
import json
import easygui
import requests
import time

url = 'http://yfcp807.com/tools/ssc_ajax.ashx?A=GetLotteryOpen&S=yfvip&U=xxxxxxxx'


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
    'U':'wchy2827873682',
    'Action' : 'GetLotteryOpen',
    'LotteryCode': 1407,
    'IssueNo' : 0,
    'DataNum' : 6,
    'SourceName' : 'PC'
}

s = requests.session()
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
        addslist.append(adds)

    #addslist = [1,1,1,1,1,1]
    print '最近6次的值为： ' + str(addslist)
    return addslist
    #return len(list(set(addslist)))

def alert_u():
    pass


if __name__ == '__main__':
    while 1==1:
        l = get_data()
        time.sleep(5)
        if len(list(set(l))) == 1:
            print l
            easygui.msgbox(u'6个连续出现了', u'注意快3')

