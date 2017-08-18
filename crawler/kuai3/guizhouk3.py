# encoding: utf-8
import json
import easygui
import requests
import time

url = 'http://yfcp807.com/tools/ssc_ajax.ashx?A=GetLotteryOpen&S=yfvip&U=132974199455'

header = {
    'Host': 'yfcp807.com',
    'Origin': 'http://yfcp807.com',
    'Referer': 'http://yfcp807.com/lottery/K3/1409',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': 'route=134217aa4e8e12a08665fba45d9ec79f; token=94b04c7bfa75e1886efde9beaee135e4; random=2580; C_SessionId=e55fa638-1bcc-4d49-aca3-3fd4cabb83a5',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

postdata = {
    'A': 'GetLotteryOpen',
    'S': 'yfvip',
    'U': '132974199455',
    'Action': 'GetLotteryOpen',
    'LotteryCode': 1409,
    'IssueNo': 0,
    'DataNum': 6,
    'SourceName': 'PC'
}

s = requests.session()


def log_in():
    pass

def get_data():
    dsList = []
    dxlist = []
    arrayList = []
    response = requests.post(url, postdata, headers=header)
    html = response.text
    jsons = json.loads(html)
    ar = jsons.get('BackData')
    for key in ar:
        sv = key['LotteryOpen'].split(',')
        adds = sum(int(a) for a in sv)
        arrayList.append(adds)
        ds = adds % 2
        dx = adds // 11

        dsList.append(ds)
        dxlist.append(dx)

    print '甘肃最近6次的值为： ' + str(arrayList)
    return dsList, dxlist


if __name__ == '__main__':
    while 1 == 1:
        time.sleep(200)
        dslist, dxlist = get_data()
        print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if len(list(set(dxlist))) == 1:
            #playSound();
            easygui.msgbox(u'贵州6连大小', u'注意快3')

        if len(list(set(dslist))) == 1:
            #playSound();
            easygui.msgbox(u'贵州6连单双', u'注意快3')
